import os


DOMAIN_PATH = "backend/domain"
APPLICATION_PATH = "backend/application"


FORBIDDEN_DOMAIN_IMPORTS = [
    "sqlalchemy",
    "fastapi",
    "session",
    "repository"
]

FORBIDDEN_APPLICATION_IMPORTS = [
    "backend.infrastructure",
    "sqlalchemy",
    "session"
]


def check_forbidden_imports(directory, forbidden_list):

    violations = []

    for root, _, files in os.walk(directory):
        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            for forbidden in forbidden_list:
                if forbidden in content:
                    violations.append(f"{path} imports {forbidden}")

    return violations


def test_domain_layer_is_pure():

    violations = check_forbidden_imports(
        DOMAIN_PATH,
        FORBIDDEN_DOMAIN_IMPORTS
    )

    assert not violations, f"Domain layer violations: {violations}"


def test_application_does_not_import_infrastructure():

    violations = check_forbidden_imports(
        APPLICATION_PATH,
        FORBIDDEN_APPLICATION_IMPORTS
    )

    assert not violations, f"Application layer violations: {violations}"
