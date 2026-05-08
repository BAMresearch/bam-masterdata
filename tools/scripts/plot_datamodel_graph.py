import argparse
import importlib
from pathlib import Path

from graphviz import Digraph

from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


def get_label(cls) -> str:
    """Create label based on property types."""
    props = [
        name
        for name, val in vars(cls).items()
        if isinstance(val, PropertyTypeAssignment)
    ]
    return f"{cls.__name__}\\n" + "\\n".join(props)


def add_subclasses(dot: Digraph, cls):
    """Add all subclasses to the graph."""
    dot.node(cls.__name__, label=get_label(cls), shape="box")
    for subcls in cls.__subclasses__():
        dot.edge(cls.__name__, subcls.__name__)
        add_subclasses(dot, subcls)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root_class",
        help="Root class to plot (e.g. bam_masterdata.datamodel.v2.base.BaseEntity)",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Output file name (without extension). By default uses the root class name.",
    )

    args = parser.parse_args()

    module = args.root_class.rsplit(".", 1)[0]
    class_name = args.root_class.rsplit(".", 1)[1]

    root_class = getattr(importlib.import_module(module), class_name)

    filename = args.output or root_class.__name__

    dot = Digraph()
    add_subclasses(dot, root_class)

    out_path = Path(__file__).parent / filename
    dot.render(str(out_path), format="png")


if __name__ == "__main__":
    main()
