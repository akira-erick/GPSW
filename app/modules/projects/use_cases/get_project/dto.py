from dataclasses import dataclass

@dataclass

class GetProjectDTO:
    id: str

class GetProjectResponseDTO:
    id: str
    name: str
    description: str
    category: str
