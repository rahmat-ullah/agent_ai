"""Adaptive Learning Agent module for personalized learning experiences."""

from praisonaiagents import Agent, Task, PraisonAIAgents
from ai_agents_hub.config import get_agent_config
from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional, Union, Any
from pathlib import Path
from datetime import datetime
import time

class PerformanceMetric(BaseModel):
    """Model for tracking performance metrics."""
    score: float
    topic: str
    timestamp: datetime
    difficulty: str
    completion_time: Optional[int] = None
    feedback: Optional[str] = None

class StudentProfile(BaseModel):
    """Model for tracking student progress and preferences."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    student_id: str
    current_level: str
    learning_style: str
    performance_history: List[PerformanceMetric]
    strengths: List[str]
    areas_for_improvement: List[str]
    last_assessment: datetime

class Exercise(BaseModel):
    """Model for learning exercises."""
    question: str
    answer: Optional[str] = None
    difficulty: str
    type: str
    hints: List[str] = []

class LearningContent(BaseModel):
    """Model for structured learning content."""
    topic: str
    difficulty: str
    content_type: str
    materials: List[str]
    exercises: List[Exercise]
    estimated_duration: int

def assess_student_level() -> str:
    """Simulates student assessment."""
    levels = ["beginner", "intermediate", "advanced"]
    current_time = int(time.time())
    return levels[current_time % 3]

def generate_content(level: str) -> Dict[str, str]:
    """Generates appropriate learning content based on level."""
    content_types = {
        "beginner": "basic concepts and examples",
        "intermediate": "practice problems and applications",
        "advanced": "complex scenarios and projects"
    }
    return {"content": content_types.get(level, "basic concepts")}

def evaluate_performance() -> str:
    """Evaluates student performance."""
    scores = ["low", "medium", "high"]
    current_time = int(time.time())
    return scores[current_time % 3]

def adapt_difficulty(performance: str) -> str:
    """Adapts content difficulty based on performance."""
    adaptations = {
        "low": "decrease",
        "medium": "maintain",
        "high": "increase"
    }
    return adaptations.get(performance, "maintain")

def create_adaptive_learning_agent():
    """Create an adaptive learning agent that personalizes content and tracks progress.
    
    This agent provides:
    - Student assessment and profiling
    - Personalized content generation
    - Performance tracking
    - Dynamic difficulty adjustment
    
    Returns:
        Agent: An adaptive learning agent with comprehensive learning capabilities.
    """
    config = get_agent_config()
    root_dir = Path(__file__).parent.parent.parent.parent
    docs_path = root_dir / "docs" / "resources" / "adaptive_learning_docs.md"
    
    # Create specialized sub-agents
    assessor = Agent(
        name="Student Assessor",
        instructions="""Evaluate student's current knowledge level and learning style:
        1. Assess understanding of core concepts
        2. Identify knowledge gaps
        3. Determine learning preferences
        4. Track progress over time""",
        tools=[assess_student_level],
        knowledge_config=config,
        user_id="assessor",
        llm="mistral:latest"
    )
    
    generator = Agent(
        name="Content Generator",
        instructions="""Create personalized learning content:
        1. Match content to student level
        2. Incorporate learning preferences
        3. Design engaging exercises
        4. Include practical examples""",
        tools=[generate_content],
        knowledge_config=config,
        user_id="generator",
        llm="mistral:latest"
    )
    
    evaluator = Agent(
        name="Performance Evaluator",
        instructions="""Track and analyze student performance:
        1. Monitor progress metrics
        2. Identify improvement areas
        3. Measure learning outcomes
        4. Generate progress reports""",
        tools=[evaluate_performance],
        knowledge_config=config,
        user_id="evaluator",
        llm="mistral:latest"
    )
    
    adapter = Agent(
        name="Content Adapter",
        instructions="""Dynamically adjust learning experience:
        1. Scale difficulty appropriately
        2. Optimize content delivery
        3. Adjust learning pace
        4. Recommend next steps""",
        tools=[adapt_difficulty],
        knowledge_config=config,
        user_id="adapter",
        llm="mistral:latest"
    )
    
    # Create workflow tasks
    assessment_task = Task(
        name="assess_level",
        description="Assess student's current level",
        expected_output="Student's proficiency level",
        agent=assessor,
        is_start=True,
        next_tasks=["generate_content"]
    )
    
    generation_task = Task(
        name="generate_content",
        description="Generate appropriate content",
        expected_output="Learning content",
        agent=generator,
        next_tasks=["evaluate_performance"]
    )
    
    evaluation_task = Task(
        name="evaluate_performance",
        description="Evaluate student's performance",
        expected_output="Performance assessment",
        agent=evaluator,
        next_tasks=["adapt_difficulty"]
    )
    
    adaptation_task = Task(
        name="adapt_difficulty",
        description="Adapt content difficulty",
        expected_output="Difficulty adjustment",
        agent=adapter,
        task_type="decision",
        condition={
            "decrease": ["generate_content"],
            "maintain": "",
            "increase": ["generate_content"]
        }
    )
    
    # Create workflow
    workflow = PraisonAIAgents(
        agents=[assessor, generator, evaluator, adapter],
        tasks=[assessment_task, generation_task, evaluation_task, adaptation_task],
        process="workflow",
        verbose=True
    )
    
    return workflow

def process_learning(student_id: str, topic: str) -> Dict[str, any]:
    """Process a learning session for a student.
    
    Args:
        student_id: Unique identifier for the student
        topic: The topic to learn
        
    Returns:
        Dict containing the learning session results and recommendations
    """
    workflow = create_adaptive_learning_agent()
    
    try:
        # Run the adaptive learning workflow
        results = workflow.start()
        
        # Process and structure the results
        session_results = {
            "student_id": student_id,
            "topic": topic,
            "timestamp": datetime.now(),
            "assessment": None,
            "content": None,
            "performance": None,
            "adaptation": None
        }
        
        # Extract results from each task
        for task_id, result in results["task_results"].items():
            if result:
                if task_id == "assess_level":
                    session_results["assessment"] = result.raw
                elif task_id == "generate_content":
                    session_results["content"] = result.raw
                elif task_id == "evaluate_performance":
                    session_results["performance"] = result.raw
                elif task_id == "adapt_difficulty":
                    session_results["adaptation"] = result.raw
        
        return session_results
        
    except Exception as e:
        return {
            "error": str(e),
            "student_id": student_id,
            "topic": topic,
            "timestamp": datetime.now()
        }

if __name__ == "__main__":
    # Example usage
    student_id = "student123"
    topic = "Python Programming"
    results = process_learning(student_id, topic)
    print("\nAdaptive Learning Results:")
    print("=" * 50)
    for key, value in results.items():
        print(f"{key}: {value}")
