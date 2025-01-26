from praisonaiagents import Agent

def create_knowledge_agent():
    """Create a knowledge agent specifically for handling PDF and knowledge-based queries"""
    config = {
        "vector_store": {
            "provider": "chroma",
            "config": {
                "collection_name": "praison",
                "path": ".praison"
            }
        },
        "llm": {
            "provider": "ollama",
            "config": {
                "model": "deepseek-r1:latest",
                "temperature": 0,
                "max_tokens": 8000,
                "ollama_base_url": "http://localhost:11434",
            },
        },
        "embedder": {
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text:latest",
                "ollama_base_url": "http://localhost:11434",
                "embedding_dims": 1536
            },
        },
    }
    
    return Agent(
        name="Knowledge Agent",
        instructions="You answer questions based on the provided knowledge.",
        knowledge=["Efficient Document Retrieval with Vision Language Models.pdf"],
        knowledge_config=config,
        user_id="user1",
        llm="deepseek-r1"
    )
