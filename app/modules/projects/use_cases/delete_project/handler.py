from .dto import DeleteProjectDTO
from flask import jsonify

def delete_project_handler(dict_projects: dict, data: DeleteProjectDTO):
    project = dict_projects.get(data.id)

    if project is None:
        return jsonify({"error": f"Project with ID '{data.id}' not found"}), 404

    del dict_projects[data.id]
    return '', 204