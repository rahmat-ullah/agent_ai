"""Code Review Agent module for performing comprehensive code reviews."""

from praisonaiagents import Agent
from ai_agents_hub.config import get_agent_config
from pydantic import BaseModel
from typing import List, Dict, Optional
from pathlib import Path

class CodeIssue(BaseModel):
    """Model for individual code issues found during review."""
    type: str
    severity: str
    file: str
    line_number: Optional[int]
    description: str
    suggested_fix: Optional[str]

class CodeReviewReport(BaseModel):
    """Comprehensive code review report model."""
    issues: List[CodeIssue]
    summary: str
    total_issues: int
    severity_counts: Dict[str, int]
    automated_fixes_applied: int
    manual_review_needed: List[str]

def create_code_review_agent():
    """Create a code review agent for detailed code analysis.
    
    Returns:
        Agent: A specialized agent for code review with comprehensive evaluation capabilities.
    """
    config = get_agent_config()
    root_dir = Path(__file__).parent.parent.parent.parent
    docs_path = root_dir / "docs" / "resources" / "code_review_docs.md"
    
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
        knowledge=[str(docs_path)] if docs_path.exists() else [],
        knowledge_config=config,
        user_id="code_reviewer",
        llm="deepseek-r1"
    )

def process_review(code_content: str) -> CodeReviewReport:
    """Process a code review request and generate a structured report.
    
    Args:
        code_content: The code to review
        
    Returns:
        CodeReviewReport: Structured review results with detailed analysis
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
    
    Provide the response in a structured format that can be parsed into a CodeReviewReport.
    """
    
    # Get the review results
    review_result = agent.start(prompt)
    
    # Parse and structure the results
    # Note: This is a placeholder. In a real implementation, you would need to
    # parse the agent's response into a proper CodeReviewReport structure
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
