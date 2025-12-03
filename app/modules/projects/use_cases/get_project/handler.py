from .dto import GetProjectDTO
from flask import jsonify

def get_project_handler(connection, data: GetProjectDTO):
    cur = connection.cursor()

    cur.execute(
        """
        SELECT id, name, description, category
        FROM projects
        WHERE id = %s
        """,
        (data.id,)
    )

    project = cur.fetchone()

    if project is None:
        return jsonify({"error": f"Project with ID '{data.id}' not found"}), 404
    
    return jsonify(project), 200