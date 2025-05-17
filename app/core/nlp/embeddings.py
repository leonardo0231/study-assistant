from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingService:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.passages = []
    
    def load_content(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.passages = content.split('\n')
        embeddings = self.model.encode(self.passages)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings.astype(np.float32))

    def search(self, query: str, k: int  = 1):
        query_embedding = self.model.encode([query])
        distance, indices = self.index.search(query_embedding.astype(np.float32), k)
        return [(self.passages[i], distance[0][j]) for j, i in enumerate(indices[0])]
    