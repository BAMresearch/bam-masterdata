import pytest

from bam_masterdata.workflows.validation import (
    ResolvedTarget,
    select_value,
    validate_workflow_graph,
    validate_workflow_specification,
)


def locator(identifier, selector=None):
    return {"kind": "object", "identifier": identifier, "selector": selector}


def link(name, identifier="DATA", selector=None):
    return {"name": name, "target": locator(identifier, selector)}


def reference(identifier, *, task_id="ref", relation="reference", **kwargs):
    return {
        "kind": "reference",
        "id": task_id,
        "name": task_id,
        "target": locator(identifier),
        "relation": relation,
        **kwargs,
    }


def graph(tasks=(), **kwargs):
    return {"schema_version": "1", "tasks": list(tasks), **kwargs}


def test_missing_target_and_selector_fail_closed():
    value = graph(inputs=[link("system")])
    with pytest.raises(ValueError, match="Unresolved object"):
        validate_workflow_graph(value, lambda target: {}[target.identifier])
    with pytest.raises(ValueError, match="did not resolve"):
        validate_workflow_graph(value, lambda target: "DATA")
    with pytest.raises(ValueError, match="Unresolved selector"):
        validate_workflow_graph(
            graph(inputs=[link("system", selector="/missing")]),
            lambda target: ResolvedTarget("DATA", {}),
        )


def test_json_pointer_resolves_escaped_names_and_arrays():
    assert select_value({"a/b": {"~": [4]}}, "/a~1b/~0/0") == 4
    for pointer in ["/a~1b/~0/01", "/a~1b/~0/-", "/a~1b/~0/1"]:
        with pytest.raises(ValueError, match="Unresolved selector"):
            select_value({"a/b": {"~": [4]}}, pointer)


def test_reference_boundary_matches_actual_execution():
    child = graph(outputs=[link("final", "FINAL")])
    resources = {
        "CHILD": ResolvedTarget(
            "CHILD", {}, workflow_graph=child, category="execution"
        ),
        "FINAL": ResolvedTarget("FINAL", {}),
        "ALIAS": ResolvedTarget("FINAL", {}),
        "WRONG": ResolvedTarget("WRONG", {}),
    }
    resolve = lambda target: resources[target.identifier]
    validate_workflow_graph(
        graph([reference("CHILD", outputs=[link("final", "ALIAS")])]), resolve
    )
    with pytest.raises(ValueError, match="contradicts"):
        validate_workflow_graph(
            graph([reference("CHILD", outputs=[link("final", "WRONG")])]), resolve
        )


def test_connections_compare_canonical_identities():
    value = graph(
        [
            {
                "kind": "execution",
                "id": "a",
                "name": "a",
                "outputs": [link("out", "ALIAS")],
            },
            {"kind": "execution", "id": "b", "name": "b", "inputs": [link("in")]},
        ],
        connections=[
            {
                "source_task": "a",
                "source_port": "out",
                "target_task": "b",
                "target_port": "in",
            }
        ],
    )
    validate_workflow_graph(
        value, lambda target: ResolvedTarget("CANONICAL", {"energy": 4})
    )
    with pytest.raises(ValueError, match="same data target"):
        validate_workflow_graph(
            value, lambda target: ResolvedTarget(target.identifier, {})
        )


def test_function_reference_category_and_declared_ports():
    value = graph(
        [
            {
                "kind": "execution",
                "id": "a",
                "name": "a",
                "function": locator("FUNCTION"),
                "inputs": [link("input")],
            }
        ]
    )
    resources = {
        "FUNCTION": ResolvedTarget(
            "FUNCTION",
            {
                "function_specification": {
                    "schema_version": "1",
                    "inputs": [{"name": "input"}],
                }
            },
            category="function",
        ),
        "DATA": ResolvedTarget("DATA", {}),
    }
    validate_workflow_graph(value, lambda target: resources[target.identifier])
    resources["FUNCTION"] = ResolvedTarget("FUNCTION", {}, category="data")
    with pytest.raises(ValueError, match="workflow function"):
        validate_workflow_graph(value, lambda target: resources[target.identifier])
    resources["FUNCTION"] = ResolvedTarget(
        "FUNCTION",
        {
            "function_specification": {
                "schema_version": "1",
                "inputs": [{"name": "different"}],
            }
        },
        category="function",
    )
    with pytest.raises(ValueError, match="input ports"):
        validate_workflow_graph(value, lambda target: resources[target.identifier])


def test_existing_data_cannot_be_referenced_as_execution():
    with pytest.raises(ValueError, match="resolve to an execution"):
        validate_workflow_graph(
            graph([reference("DATA")]), lambda target: ResolvedTarget("DATA", {})
        )


def test_nested_containment_cycles_rejected_with_aliases():
    outer = graph([reference("INNER", relation="contains")])
    inner = graph([reference("OUTER_ALIAS", relation="contains")])
    resources = {
        "INNER": ResolvedTarget(
            "INNER", {}, workflow_graph=inner, category="execution"
        ),
        "OUTER_ALIAS": ResolvedTarget(
            "OUTER", {}, workflow_graph=outer, category="execution"
        ),
    }
    with pytest.raises(ValueError, match="Recursive workflow containment"):
        validate_workflow_graph(
            outer, lambda target: resources[target.identifier], root_identifier="OUTER"
        )


def test_execution_reuse_is_allowed_and_nested_data_checked():
    child = graph(inputs=[link("input")])
    resources = {
        "CHILD": ResolvedTarget(
            "CHILD", {}, workflow_graph=child, category="execution"
        ),
        "DATA": ResolvedTarget("DATA", {}),
    }
    outer = graph([reference("CHILD", task_id="a"), reference("CHILD", task_id="b")])
    validate_workflow_graph(
        outer, lambda target: resources[target.identifier], root_identifier="ROOT"
    )
    del resources["DATA"]
    with pytest.raises(ValueError, match="Unresolved object"):
        validate_workflow_graph(
            outer, lambda target: resources[target.identifier], root_identifier="ROOT"
        )


def test_definition_function_targets_are_resolved():
    value = {
        "schema_version": "1",
        "tasks": [{"id": "a", "name": "a", "function": locator("FN")}],
    }
    validate_workflow_specification(
        value, lambda target: ResolvedTarget("FN", {}, category="function")
    )
    with pytest.raises(ValueError, match="workflow function"):
        validate_workflow_specification(value, lambda target: ResolvedTarget("FN", {}))
