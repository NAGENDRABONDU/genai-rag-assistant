from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

documents = []


def fit_embeddings(texts):
    global vectorizer
    global documents

    documents = texts

    vectorizer.fit(texts)


def create_embedding(text):

    return vectorizer.transform(
        [text]
    ).toarray()[0]


def create_embeddings(texts):

    return vectorizer.transform(
        texts
    ).toarray()