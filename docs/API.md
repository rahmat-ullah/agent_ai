# AI Agents Hub API Documentation

## Agents

### Knowledge Agent

The Knowledge Agent is responsible for processing PDF documents and answering questions based on their content.

```python
from ai_agents_hub.agents.knowledge_agent import create_knowledge_agent

agent = create_knowledge_agent()
response = agent.start("What is the main topic of the document?")
```

### Code Analysis Agent

The Code Analysis Agent evaluates code quality, structure, and maintainability.

```python
from ai_agents_hub.agents.code_analysis_agent import create_code_analysis_agent

agent = create_code_analysis_agent()
response = agent.start("Please analyze this code: ...")
```

### Code Review Agent

The Code Review Agent performs detailed code reviews and suggests improvements.

```python
from ai_agents_hub.agents.code_review_agent import create_code_review_agent

agent = create_code_review_agent()
response = agent.start("Please review this code: ...")
```

## Configuration

The agent configuration can be customized through the config module:

```python
from ai_agents_hub.config import get_agent_config

config = get_agent_config()
# Modify configuration as needed
config["llm"]["config"]["temperature"] = 0.5
```

## UI Components

The Streamlit UI components are available in the ui module:

```python
from ai_agents_hub.ui.streamlit_app import main

# Run the Streamlit application
main()
```

## Error Handling

All agents include comprehensive error handling:

```python
try:
    response = agent.start(prompt)
except Exception as e:
    print(f"Error: {str(e)}")
```

## Testing

Run tests using unittest:

```bash
python -m unittest discover tests
```
