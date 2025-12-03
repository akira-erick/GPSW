import uuid

from flask import jsonify

from .dto import ApplicateCandidateDTO, ApplicateCandidateResponseDTO

def applicate_candidate_handler(connection, data: ApplicateCandidateDTO):
    application_id = str(uuid.uuid4())

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO applications (id, candidate_id, project_id) VALUES (%s, %s, %s)",
        (application_id, data.candidate_id, data.project_id)
    )

    connection.commit()
    cursor.close()

    response = ApplicateCandidateResponseDTO(application_id=application_id)

    return jsonify(response), 201