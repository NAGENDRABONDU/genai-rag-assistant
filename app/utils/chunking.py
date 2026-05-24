def chunk_text(
    text: str,
    chunk_size: int = 300
):
    """
    Split long text into chunks
    """

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks