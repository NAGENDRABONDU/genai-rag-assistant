import json


def load_documents(file_path: str):
    """
    Load all documents from docs.json
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        documents = json.load(file)

    return documents