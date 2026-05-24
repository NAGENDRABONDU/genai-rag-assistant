sessions = {}


def get_history(session_id):

    return sessions.get(
        session_id,
        []
    )


def save_message(
    session_id,
    role,
    message
):

    if session_id not in sessions:

        sessions[session_id] = []

    sessions[session_id].append(
        {
            "role": role,
            "message": message
        }
    )

    sessions[session_id] = (
        sessions[session_id][-10:]
    )


def history_to_text(
    session_id
):

    history = get_history(
        session_id
    )

    return "\n".join(
        [
            f"{item['role']}: "
            f"{item['message']}"
            for item in history
        ]
    )