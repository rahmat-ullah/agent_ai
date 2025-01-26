"""Code Analysis Agent module for analyzing code quality and structure."""

from praisonaiagents import Agent
from ai_agents_hub.config import get_agent_config
from pydantic import BaseModel
from typing import List, Dict
from pathlib import Path

class CodeMetrics(BaseModel):
    """Model for code quality metrics."""
    category: str
    score: int
    findings: List[str]

class CodeAnalysisReport(BaseModel):
    """Comprehensive code analysis report model."""
    overall_quality: int
    code_metrics: List[CodeMetrics]
    architecture_score: int
    maintainability_score: int
    performance_score: int
    security_score: int
    test_coverage: int
    key_strengths: List[str]
    improvement_areas: List[str]
    tech_stack: List[str]
    recommendations: List[str]
    complexity_metrics: Dict[str, int]
    best_practices: List[Dict[str, str]]
    potential_risks: List[str]
    documentation_quality: int

def create_code_analysis_agent():
    """Create a code analysis agent for evaluating code quality.
    
    Returns:
        Agent: A specialized agent for code analysis with comprehensive evaluation capabilities.
    """
    config = get_agent_config()
    root_dir = Path(__file__).parent.parent.parent.parent
    docs_path = root_dir / "docs" / "resources" / "code_analysis_docs.md"
    
    return Agent(
        name="Code Analysis Expert",
        instructions="""Analyze code quality, maintainability, and security with these specific focuses:

        1. Quality Metrics (0-100 scale):
           - Overall code quality
           - Architecture design
           - Maintainability
           - Performance
           - Security
           - Test coverage
           - Documentation quality

        2. Technical Analysis:
           - Identify and list the tech stack
           - Calculate complexity metrics
           - Evaluate best practices adherence
           - Assess potential risks
           - Analyze code organization and structure

        3. Recommendations:
           - Provide specific improvement suggestions
           - Include line number references
           - Suggest refactoring opportunities
           - Highlight security considerations
           - Recommend performance optimizations

        4. Output Format:
           - Use structured sections
           - Include concrete examples
           - Reference specific code lines
           - Provide actionable feedback
           - Prioritize recommendations

        Always provide specific examples and line references in your analysis.""",
        knowledge=[str(docs_path)] if docs_path.exists() else [],
        knowledge_config=config,
        user_id="code_analyst",
        llm="deepseek-r1:1.5b"
    )
