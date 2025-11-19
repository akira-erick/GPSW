from .dto import DeleteProjectDTO

def delete_project_handler(dict_projects: dict, data: DeleteProjectDTO):
    project = dict_projects.get(data.id)

    if project is None:
        return {"error": "Project not found"}, 404

    del dict_projects[data.id]
    return