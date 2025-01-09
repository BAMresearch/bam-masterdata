import importlib.util
import inspect
import os

import click


def import_module(module_path: str):
    """
    Dynamically imports a module from the given file path.

    Args:
        module_path (str): Path to the Python module file.

    Returns:
        module: Imported module object.
    """
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def entities_to_json(module_path: str, export_dir: str) -> None:
    """
    Export entities to JSON files. The Python modules are imported using the function `import_module`,
    and their contents are inspected (using `inspect`) to find the classes in the datamodel containing
    `defs` and with a `to_json` method defined.

    Args:
        module_path (str): Path to the Python module file.
        export_dir (str): Path to the directory where the JSON files will be saved.
    """
    module = import_module(module_path=module_path)
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `to_json` method
        if not hasattr(obj, 'defs') or not callable(getattr(obj, 'to_json')):
            continue

        try:
            # Instantiate the class and call the method
            json_data = obj().to_json(indent=2)

            # Write JSON data to file
            output_file = os.path.join(export_dir, f'{obj.defs.code}.json')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(json_data)

            click.echo(f'Saved JSON for class {name} to {output_file}')
        except Exception as err:
            click.echo(f'Failed to process class {name} in {module_path}: {err}')
