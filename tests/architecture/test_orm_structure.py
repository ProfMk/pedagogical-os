import pathlib


PROJECT_ROOT = pathlib.Path("backend")
THIS_FILE = pathlib.Path(__file__).resolve()


def _read_file(file: pathlib.Path) -> str:
    return file.read_text(encoding="utf-8", errors="ignore")


def test_single_base_import_policy():
    """
    Ensure no relative Base imports exist.
    """
    for file in PROJECT_ROOT.rglob("*.py"):
        if file.resolve() == THIS_FILE:
            continue

        content = _read_file(file)

        if "from .base import Base" in content:
            raise AssertionError(f"Relative Base import found in {file}")


def test_no_mixed_infrastructure_root_imports():
    """
    Ensure no mixed 'infrastructure.' imports exist.
    """
    for file in PROJECT_ROOT.rglob("*.py"):
        if file.resolve() == THIS_FILE:
            continue

        content = _read_file(file)

        if "from infrastructure." in content:
            raise AssertionError(f"Mixed infrastructure import found in {file}")


def test_base_defined_only_once():
    """
    Ensure declarative_base() is defined only once
    and only inside backend.infrastructure.orm.base
    """
    base_files = []

    for file in PROJECT_ROOT.rglob("*.py"):
        if file.resolve() == THIS_FILE:
            continue

        content = _read_file(file)

        if "declarative_base(" in content:
            base_files.append(file)

    assert base_files == [
        pathlib.Path("backend/infrastructure/orm/base.py")
    ], f"Unexpected declarative_base definitions found: {base_files}"
