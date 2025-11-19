import uuid
from .dto import CreateProjectResponseDTO, CreateProjectDTO
from flask import jsonify
from dataclasses import asdict

def create_project_handler(dict_projects: dict, data: CreateProjectDTO):

    id = uuid.uuid4()
    dict_projects[str(id)] = asdict(data)
    response_dto: CreateProjectResponseDTO = CreateProjectResponseDTO(id=str(id))

    return jsonify(asdict(response_dto))
    