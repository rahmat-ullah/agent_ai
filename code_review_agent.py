from praisonaiagents import Agent
from pydantic import BaseModel
from typing import List, Dict, Optional
import os

class CodeIssue(BaseModel):
    type: str
    severity: str
    file: str
    line_number: Optional[int]
    description: str
    suggested_fix: Optional[str]

class CodeReviewReport(BaseModel):
    issues: List[CodeIssue]
    summary: str
    total_issues: int
    severity_counts: Dict[str, int]
    automated_fixes_applied: int
    manual_review_needed: List[str]

def create_code_review_agent():
    config = {
        "vector_store": {
            "provider": "chroma",
            "config": {
                "collection_name": "code_review",
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
        name="Code Review Expert",
        instructions="""You are an expert code reviewer. For each code review request:

        1. Issue Detection:
           - Identify code issues (style, security, performance)
           - Assign severity (low, medium, high)
           - Note file and line numbers
           - Provide clear descriptions

        2. Fix Suggestions:
           - Suggest specific fixes for each issue
           - Include code examples
           - Reference best practices
           - Consider context and dependencies

        3. Automated vs Manual:
           - Identify issues suitable for automated fixing
           - Flag complex issues for manual review
           - Provide context for manual reviews

        4. Review Report:
           - Summarize findings
           - Count issues by severity
           - Track automated fixes
           - List manual review items

        Always provide specific examples and line references.""",
        knowledge=["code_review_docs.md"],
        knowledge_config=config,
        user_id="code_reviewer",
        llm="deepseek-r1"
    )

def process_review(code_content: str) -> CodeReviewReport:
    """
    Process a code review request and generate a structured report.
    
    Args:
        code_content: The code to review
        
    Returns:
        CodeReviewReport: Structured review results
    """
    agent = create_code_review_agent()
    
    # Format the review request
    prompt = f"""Please review this code and provide a detailed analysis:
    ```
    {code_content}
    ```
    Focus on:
    1. Code quality and style
    2. Potential bugs and issues
    3. Security concerns
    4. Performance improvements
    5. Best practices
    """
    
    # Get the review results
    review_result = agent.start(prompt)
    
    # Parse and structure the results
    # Note: In a real implementation, you would parse the agent's
    # response into a proper CodeReviewReport structure
    return review_result

if __name__ == "__main__":
    # Example usage
    code = """
    def process_data(data):
        for i in range(len(data)):
            if data[i] == None:
                continue
            # Process the data
            result = data[i] * 2
        return result
    """
    
    report = process_review(code)
    print(report)
