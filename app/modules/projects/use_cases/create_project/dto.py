from dataclasses import dataclass

@dataclass
class CreateProjectDTO:
    name: str
    description: str
    category: str

@dataclass
class ProjectDTO:
    id: str
    name: str
    description: str
    category: str

@dataclass
class CreateProjectResponseDTO:
    id: str