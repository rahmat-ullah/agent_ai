"""Knowledge Agent module for processing PDFs and answering questions."""

from praisonaiagents import Agent
from ai_agents_hub.config import get_agent_config
from pathlib import Path

def create_knowledge_agent():
    """Create a knowledge agent specifically for handling PDF and knowledge-based queries"""
    config = get_agent_config()
    root_dir = Path(__file__).parent.parent.parent.parent
    docs_path = root_dir / "docs" / "resources" / "Efficient Document Retrieval with Vision Language Models.pdf"
    return Agent(
        name="Knowledge Agent",
        instructions="You answer questions based on the provided knowledge.",
        knowledge=[str(docs_path)],
        knowledge_config=config,
        user_id="user1",
        llm="deepseek-r1:1.5b"
    )
