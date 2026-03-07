import os


INTERFACE_PATH = "backend/interface"


FORBIDDEN_PATTERNS = [
    "session.query(",
    "session.execute(",
    "session.get(",
    "from sqlalchemy",
]


def test_interface_layer_does_not_run_queries():

    violations = []

    for root, _, files in os.walk(INTERFACE_PATH):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            for forbidden in FORBIDDEN_PATTERNS:

                if forbidden in content:

                    violations.append(
                        f"{path} contains forbidden database operation: {forbidden}"
                    )

    assert not violations, f"Interface layer DB access detected: {violations}"