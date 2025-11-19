from .dto import GetProjectDTO, GetProjectResponseDTO

def get_project_handler(dict_projects: dict, data: GetProjectDTO):
    
    project = dict_projects.get(data.id)

    if project is None:
        return {"error": "Project not found"}, 404
    return project