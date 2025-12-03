from flask import Blueprint, request

from .use_cases.create_project.handler import create_project_handler
from .use_cases.create_project.dto import CreateProjectDTO

from .use_cases.get_project.handler import get_project_handler
from .use_cases.get_project.dto import GetProjectDTO

from .use_cases.delete_project.handler import delete_project_handler
from .use_cases.delete_project.dto import DeleteProjectDTO

from .use_cases.get_all_projects.handler import get_all_projects_handler

from ...db_service import get_db_connection

projects_bp = Blueprint('projects', __name__, url_prefix='/projects/')

@projects_bp.route('/', methods=['POST'])
def create_project():
    conn = get_db_connection()

    data = request.get_json()
    if not data:
        return {"error": "Missing data"}, 400
    
    try:
        name = data['name']
        description = data['description']
        category = data['category']

        dto: CreateProjectDTO = CreateProjectDTO(
            name=name,
            description=description,
            category=category
        )

        response = create_project_handler(conn, data = dto)

        return response
    
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400
    
@projects_bp.route('/<id>', methods=['GET'])
def get_project(id):
    conn = get_db_connection()
    try:
        dto: GetProjectDTO = GetProjectDTO(id=id)
        response = get_project_handler(conn, data = dto)
        return response
    
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400

@projects_bp.route('/<id>', methods=['DELETE'])
def delete_project(id):
    conn = get_db_connection()
    try:
        dto: DeleteProjectDTO = DeleteProjectDTO(id=id)
        response = delete_project_handler(conn, data = dto)
        return response
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400
    

@projects_bp.route('/all', methods=['GET'])
def get_all_projects():
    conn = get_db_connection()
    response = get_all_projects_handler(conn)
    return response, 200