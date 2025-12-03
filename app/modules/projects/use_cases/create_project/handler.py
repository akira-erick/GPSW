import uuid
from .dto import CreateProjectResponseDTO, CreateProjectDTO, ProjectDTO
from flask import jsonify
from dataclasses import asdict

def create_project_handler(connection, data: CreateProjectDTO):

    cur = connection.cursor()

    id = uuid.uuid4()

    project: ProjectDTO = ProjectDTO(
        id=str(id),
        name=data.name,
        description=data.description,
        category=data.category
    )

    cur.execute(
        """
        INSERT INTO projects (id, name, description, category)
        VALUES (%s, %s, %s, %s)
        """,
        (project.id, project.name, project.description, project.category)
    )

    response_dto: CreateProjectResponseDTO = CreateProjectResponseDTO(id=str(id))

    return jsonify(response_dto), 201
    