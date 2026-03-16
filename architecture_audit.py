import os

PROJECT_ROOT = "backend"

FORBIDDEN_IMPORTS = {
    "domain": [
        "sqlalchemy",
        "fastapi",
        "infrastructure",
        "orm",
        "session",
    ],
    "application": [
        "sqlalchemy",
        "orm",
    ],
}

VIOLATIONS = []


def scan_file(filepath, layer):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        for forbidden in FORBIDDEN_IMPORTS.get(layer, []):
            if f"import {forbidden}" in line or f"from {forbidden}" in line:
                VIOLATIONS.append(
                    f"{filepath}:{line_number} forbidden import '{forbidden}'"
                )


def detect_layer(path):
    if "domain" in path:
        return "domain"
    if "application" in path:
        return "application"
    if "infrastructure" in path:
        return "infrastructure"
    if "interface" in path:
        return "interface"
    return None


def run_audit():
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:

            if not file.endswith(".py"):
                continue

            filepath = os.path.join(root, file)

            layer = detect_layer(filepath)

            if layer is None:
                continue

            scan_file(filepath, layer)

    print("\nARCHITECTURE AUDIT REPORT\n")

    if not VIOLATIONS:
        print("No architecture violations detected.")
        return

    for violation in VIOLATIONS:
        print("Violation:", violation)

    print("\nTotal violations:", len(VIOLATIONS))


if __name__ == "__main__":
    run_audit()
