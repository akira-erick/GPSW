from .dto import ProjectDTO, GetAllProjectsResponseResponseDTO
from flask import jsonify

def get_all_projects_handler(connection):

    cur = connection.cursor()

    projects_list = []

    cur.execute(
        """
        SELECT id, name, description, category
        FROM projects
        """
    )

    dict_projects = {}
    for row in cur.fetchall():
        project_dict = {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "category": row[3]
        }
        dict_projects[row[0]] = project_dict
    for project in dict_projects.values():
        projects_list.append(ProjectDTO(**project))
    
    response_dto = GetAllProjectsResponseResponseDTO(projects=projects_list)
    
    return jsonify(response_dto)