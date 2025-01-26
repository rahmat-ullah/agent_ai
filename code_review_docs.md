# Code Review Agent Documentation

## Overview
The Code Review Agent is an automated system that performs comprehensive code reviews through a multi-agent workflow. It combines automated issue detection, fix suggestions, and automated fixes while intelligently routing complex issues for manual review.

## Key Features

### 1. Automated Issue Detection
- Identifies code issues automatically
- Categorizes issues by type:
  - Style issues
  - Security vulnerabilities
  - Performance problems
  - Best practices violations
- Assigns severity levels (low, medium, high)
- Tracks issues by file location

### 2. Intelligent Fix Suggestions
- Generates context-aware fix suggestions
- Provides detailed explanations
- References best practices
- Includes code examples
- Considers:
  - Code style (PEP 8 for Python)
  - Security best practices
  - Performance optimizations
  - Design patterns

### 3. Automated Fix Application
- Automatically applies fixes when possible
- Handles common issues:
  - Code formatting
  - Simple refactoring
  - Documentation updates
  - Import organization
- Reports success/failure status

### 4. Manual Review Routing
- Identifies complex issues requiring human review
- Provides detailed context for reviewers
- Maintains review history
- Supports iterative improvements

## Implementation

### 1. Agent Structure
The system consists of three specialized agents:

1. **Code Analyzer Agent**
   ```python
   analyzer = Agent(
       name="Code Analyzer",
       role="Code analysis",
       goal="Analyze code changes and identify issues",
       instructions="Review code changes and report issues"
   )
   ```

2. **Fix Suggester Agent**
   ```python
   fix_suggester = Agent(
       name="Fix Suggester",
       role="Solution provider",
       goal="Suggest fixes for identified issues",
       instructions="Provide appropriate fix suggestions"
   )
   ```

3. **Fix Applier Agent**
   ```python
   fix_applier = Agent(
       name="Fix Applier",
       role="Fix implementation",
       goal="Apply suggested fixes automatically when possible",
       instructions="Implement suggested fixes and report results"
   )
   ```

### 2. Workflow Tasks

1. **Analysis Task**
   - Analyzes code changes
   - Identifies issues
   - Categorizes problems
   - Assigns severity levels

2. **Suggestion Task**
   - Generates fix suggestions
   - Provides implementation details
   - Includes best practices
   - References documentation

3. **Fix Application Task**
   - Attempts automated fixes
   - Reports success/failure
   - Routes to manual review if needed
   - Maintains fix history

## Usage Guide

### 1. Basic Usage
```python
# Initialize workflow
workflow = PraisonAIAgents(
    agents=[analyzer, fix_suggester, fix_applier],
    tasks=[analysis_task, suggestion_task, fix_task],
    process="workflow",
    verbose=True
)

# Start review
results = workflow.start()
```

### 2. Review Output
The review process generates structured output including:
- Identified issues
- Suggested fixes
- Applied fixes
- Manual review requirements

### 3. Configuration Options
- Customize severity thresholds
- Define review rules
- Set automated fix preferences
- Configure manual review routing

## Best Practices

### 1. Review Process
- Run reviews frequently
- Address high-severity issues first
- Document manual review decisions
- Track fix success rates

### 2. Integration Tips
- Integrate with CI/CD pipeline
- Use with version control
- Combine with automated testing
- Include in code review process

### 3. Customization
- Define custom review rules
- Add project-specific checks
- Create specialized fix templates
- Configure review thresholds

## Requirements
- Python 3.10 or higher
- PraisonAI Agents package
- Basic Python knowledge

## Integration Examples

### 1. CI/CD Integration
```python
# Example CI/CD integration
def ci_cd_review():
    workflow = initialize_review_workflow()
    results = workflow.start()
    return process_results(results)
```

### 2. Git Hook Integration
```python
# Example pre-commit hook
def pre_commit_review():
    changes = get_staged_changes()
    workflow = initialize_review_workflow()
    results = workflow.start(changes)
    return verify_results(results)
```

### 3. IDE Integration
```python
# Example IDE integration
def ide_review(file_content):
    workflow = initialize_review_workflow()
    results = workflow.start(file_content)
    return display_results(results)
```

## Troubleshooting

### Common Issues
1. **Failed Automated Fixes**
   - Check fix compatibility
   - Verify code context
   - Review error messages

2. **Manual Review Routing**
   - Understand routing criteria
   - Check issue complexity
   - Review documentation

3. **Performance Issues**
   - Optimize review scope
   - Configure caching
   - Adjust batch sizes
