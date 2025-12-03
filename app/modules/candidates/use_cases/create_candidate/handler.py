import uuid

from flask import jsonify

from .dto import CreateCandidateDTO, CreateCandidateResponseDTO

def create_candidate_handler(connection, data: CreateCandidateDTO):
    id = str(uuid.uuid4())

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO candidates (id, name, email, resume) VALUES (%s, %s, %s, %s)",
        (id, data.name, data.email, data.resume)
    )

    connection.commit()
    cursor.close()

    response = CreateCandidateResponseDTO(id=id)

    return jsonify(response), 201