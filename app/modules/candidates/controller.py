from flask import Blueprint, request

from .use_cases.create_candidate.handler import create_candidate_handler
from .use_cases.create_candidate.dto import CreateCandidateDTO

from .use_cases.applicate.handler import applicate_candidate_handler
from .use_cases.applicate.dto import ApplicateCandidateDTO

from ...db_service import get_db_connection

projects_bp = Blueprint('projects', __name__, url_prefix='/candidates/')

@projects_bp.route('/', methods=['POST'])
def create_candidate():
    conn = get_db_connection()
    data = request.get_json()
    if not data:
        return {"error": "Missing data"}, 400
    try:
        name = data['name']
        email = data['email']
        resume = data['resume']

        dto: CreateCandidateDTO = CreateCandidateDTO(
            name=name,
            email=email,
            resume=resume
        )

        response = create_candidate_handler(conn, data = dto)

        return response
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400
    
@projects_bp.route('/applicate', methods=['POST'])
def applicate_candidate():
    conn = get_db_connection()
    data = request.get_json()
    if not data:
        return {"error": "Missing data"}, 400
    try:
        candidate_id = data['candidate_id']
        project_id = data['project_id']

        dto: ApplicateCandidateDTO = ApplicateCandidateDTO(
            candidate_id=candidate_id,
            project_id=project_id
        )

        response = applicate_candidate_handler(conn, data = dto)

        return response
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400