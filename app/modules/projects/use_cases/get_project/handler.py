from .dto import GetProjectDTO
from flask import jsonify

def get_project_handler(dict_projects: dict, data: GetProjectDTO):

    project = dict_projects.get(data.id)

    print(project)
    if project is None:
        return jsonify({"error": f"Project with ID '{data.id}' not found"}), 404
    
    return project