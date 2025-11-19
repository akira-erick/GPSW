import uuid
from .dto import CreateProjectResponseDTO, CreateProjectDTO, ProjectDTO
from flask import jsonify
from dataclasses import asdict

def create_project_handler(dict_projects: dict, data: CreateProjectDTO):

    id = uuid.uuid4()

    project: ProjectDTO = ProjectDTO(
        id=str(id),
        name=data.name,
        description=data.description,
        category=data.category
    )

    dict_projects[str(id)] = asdict(project)
    response_dto: CreateProjectResponseDTO = CreateProjectResponseDTO(id=str(id))

    return jsonify(response_dto), 201
    