import faiss
import numpy as np


class FAISSStore:

    def __init__(self, dimension=384):

        # Cosine similarity
        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.metadata = []

    def add(
        self,
        embedding,
        data
    ):

        vector = np.array(
            [embedding],
            dtype="float32"
        )

        # Normalize vector
        faiss.normalize_L2(
            vector
        )

        self.index.add(
            vector
        )

        self.metadata.append(
            data
        )

    def search(
        self,
        embedding,
        top_k=3
    ):

        query = np.array(
            [embedding],
            dtype="float32"
        )

        faiss.normalize_L2(
            query
        )

        scores, indices = (
            self.index.search(
                query,
                top_k
            )
        )

        results = []

        for idx, score in zip(
            indices[0],
            scores[0]
        ):

            if idx != -1:

                results.append(
                    {
                        "score":
                        float(score),

                        "metadata":
                        self.metadata[idx]
                    }
                )

        return results