import os


APPLICATION_PATH = "backend/application"


FORBIDDEN_IMPORTS = [
    "backend.infrastructure",
    "sqlalchemy",
    "Session",
    "session",
]


def test_application_layer_does_not_import_infrastructure():

    violations = []

    for root, _, files in os.walk(APPLICATION_PATH):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            for forbidden in FORBIDDEN_IMPORTS:

                if forbidden in content:

                    violations.append(
                        f"{path} imports forbidden dependency: {forbidden}"
                    )

    assert not violations, f"Application layer violations detected: {violations}"
