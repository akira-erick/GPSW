from dataclasses import dataclass

@dataclass
class ProjectDTO:
    id: str
    name: str
    description: str
    category: str

@dataclass 
class GetAllProjectsResponseResponseDTO:
    projects: list[ProjectDTO]