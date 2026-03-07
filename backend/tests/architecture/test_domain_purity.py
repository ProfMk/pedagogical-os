import os


DOMAIN_PATH = "backend/domain"


FORBIDDEN_IMPORTS = [
    "sqlalchemy",
    "fastapi",
    "Session",
    "session",
    "backend.infrastructure",
    "backend.interface",
]


def test_domain_layer_has_no_framework_dependencies():

    violations = []

    for root, _, files in os.walk(DOMAIN_PATH):

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

    assert not violations, f"Domain layer violations detected: {violations}"