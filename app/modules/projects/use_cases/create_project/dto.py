from dataclasses import dataclass

@dataclass
class CreateProjectDTO:
    name: str
    description: str
    category: str

@dataclass
class CreateProjectResponseDTO:
    id: str