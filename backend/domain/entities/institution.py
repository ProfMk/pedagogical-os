from dataclasses import dataclass
from uuid import UUID


@dataclass
class Institution:
    id: UUID
    name: str

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Institution name cannot be empty")