"""General Chat Agent module for handling various conversational tasks."""

from praisonaiagents import Agent
from ai_agents_hub.config import get_agent_config
from pydantic import BaseModel
from typing import List, Dict, Optional
from pathlib import Path
from datetime import datetime

class ChatMessage(BaseModel):
    """Model for chat messages."""
    content: str
    timestamp: datetime
    type: str  # 'user' or 'assistant'
    context: Optional[Dict[str, str]] = None

class ChatSession(BaseModel):
    """Model for tracking chat sessions."""
    session_id: str
    messages: List[ChatMessage]
    start_time: datetime
    last_activity: datetime
    metadata: Dict[str, str]

def create_chat_agent():
    """Create a general-purpose chat agent for handling various queries and tasks.
    
    This agent serves as the default conversational interface, capable of:
    - General knowledge queries
    - Task assistance
    - Information organization
    - Context-aware responses
    - Natural conversation
    
    Returns:
        Agent: A versatile chat agent with comprehensive conversational capabilities.
    """
    config = get_agent_config()
    root_dir = Path(__file__).parent.parent.parent.parent
    docs_path = root_dir / "docs" / "resources" / "chat_agent_docs.md"
    
    return Agent(
        name="General Assistant",
        instructions="""You are a versatile chat assistant. Your role is to:

        1. Communication:
           - Maintain natural, engaging conversation
           - Provide clear, concise responses
           - Use appropriate tone and formality
           - Maintain context awareness

        2. Knowledge & Assistance:
           - Answer general knowledge questions
           - Help with task planning and organization
           - Provide explanations and examples
           - Guide users through processes

        3. Context Management:
           - Track conversation context
           - Reference previous interactions
           - Maintain coherent dialogue flow
           - Adapt responses based on context

        4. Response Quality:
           - Ensure accuracy and relevance
           - Provide structured information
           - Include sources when appropriate
           - Maintain appropriate detail level

        5. Special Abilities:
           - Recognize when to defer to specialized agents
           - Handle multi-turn conversations
           - Manage topic transitions
           - Support various query types

        Always aim to be helpful while maintaining a professional and friendly demeanor.""",
        # knowledge=[str(docs_path)] if docs_path.exists() else [],
        knowledge_config=config,
        user_id="general_assistant",
        llm="deepseek-r1:1.5b"
    )

def process_chat(message: str, session: Optional[ChatSession] = None) -> ChatMessage:
    """Process a chat message and generate a response.
    
    Args:
        message: The user's input message
        session: Optional chat session for context
        
    Returns:
        ChatMessage: The agent's response with metadata
    """
    agent = create_chat_agent()
    
    # Format the chat request with context if available
    context = ""
    if session and session.messages:
        # Add relevant context from previous messages
        recent_messages = session.messages[-3:]  # Last 3 messages for context
        context = "\n".join([f"{m.type}: {m.content}" for m in recent_messages])
        
    prompt = f"""Previous context:
    {context}
    
    User message: {message}
    
    Please provide a helpful and contextually appropriate response."""
    
    # Get the response
    response = agent.start(prompt)
    
    # Create a chat message
    context_dict = None
    if session and session.session_id:
        context_dict = {"session_id": session.session_id}
    
    return ChatMessage(
        content=response,
        timestamp=datetime.now(),
        type="assistant",
        context=context_dict
    )

if __name__ == "__main__":
    # Example usage
    message = "Hello! Can you help me organize my tasks for today?"
    response = process_chat(message)
    print(f"User: {message}")
    print(f"Assistant: {response.content}")
