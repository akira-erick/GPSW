from .dto import DeleteProjectDTO
from flask import jsonify

def delete_project_handler(connection, data: DeleteProjectDTO):
    cur = connection.cursor()

    cur.execute(
        """
        SELECT id
        FROM projects
        WHERE id = %s
        """,
        (data.id,)
    )

    project = cur.fetchone()

    if project is None:
        return jsonify({"error": f"Project with ID '{data.id}' not found"}), 404

    cur.execute(
        """
        DELETE FROM projects
        WHERE id = %s
        """,
        (data.id,)
    )
    
    return '', 204