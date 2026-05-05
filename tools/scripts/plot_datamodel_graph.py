import argparse
import importlib
import inspect
from pathlib import Path

from graphviz import Digraph

from bam_masterdata.metadata.entities import ObjectType


def is_prop(obj):
    from bam_masterdata.metadata.definitions import PropertyTypeAssignment

    return isinstance(obj, PropertyTypeAssignment)


def load_module(module_path: str):
    return importlib.import_module(module_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module",
        help="Python module path (e.g. bam_masterdata.datamodel.v2.base)",
    )
    parser.add_argument(
        "--output",
        default="model_runtime",
        help="Output file name (without extension)",
    )

    args = parser.parse_args()

    mod = load_module(args.module)

    classes = [
        obj
        for _, obj in inspect.getmembers(mod, inspect.isclass)
        if issubclass(obj, ObjectType) and obj is not ObjectType
    ]

    dot = Digraph()

    for cls in classes:
        props = [name for name, val in vars(cls).items() if is_prop(val)]
        label = f"{cls.__name__}\\n" + "\\n".join(props)

        dot.node(cls.__name__, label=label, shape="box")

        for base in cls.__bases__:
            if issubclass(base, ObjectType):
                dot.edge(base.__name__, cls.__name__)

    out_path = Path(__file__).parent / args.output
    dot.render(str(out_path), format="png")


if __name__ == "__main__":
    main()
