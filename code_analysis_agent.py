from praisonaiagents import Agent
from pydantic import BaseModel
from typing import List, Dict
import os

class CodeMetrics(BaseModel):
    category: str
    score: int
    findings: List[str]

class CodeAnalysisReport(BaseModel):
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
    config = {
        "vector_store": {
            "provider": "chroma",
            "config": {
                "collection_name": "code_analysis",
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
        name="Code Analysis Expert",
        instructions="""Analyze code quality, maintainability, and security.
        Evaluate: quality(0-100), architecture, maintainability, performance, security, tests.
        Provide: tech stack, complexity, best practices, risks, and recommendations.
        Include specific examples and line references.""",
        knowledge=["code_analysis_docs.md"],
        knowledge_config=config,
        user_id="code_analyst",
        llm="deepseek-r1"
    )
