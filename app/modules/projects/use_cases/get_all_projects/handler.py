from .dto import ProjectDTO, GetAllProjectsResponseResponseDTO
from flask import jsonify
from dataclasses import asdict

def get_all_projects_handler(dict_projects: dict):
    projects_list = []
    
    for project_dict in dict_projects.values():
        project_dto = ProjectDTO(**project_dict)
        projects_list.append(project_dto)
    
    response_dto = GetAllProjectsResponseResponseDTO(projects=projects_list)
    
    return jsonify(response_dto)