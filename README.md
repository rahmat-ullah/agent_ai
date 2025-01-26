# AI Agents Hub

A powerful multi-agent system built with Streamlit that provides three specialized AI agents for different tasks: Knowledge Processing, Code Analysis, and Code Review.

## Features

### 1. Knowledge Agent
- Processes and answers questions based on provided PDF documents
- Uses advanced embeddings for accurate information retrieval
- Supports context-aware responses using the deepseek-r1 model

### 2. Code Analysis Agent
- Analyzes code quality and structure
- Provides detailed reports on:
  - Code maintainability
  - Performance considerations
  - Best practices
  - Potential improvements

### 3. Code Review Agent
- Performs comprehensive code reviews
- Identifies:
  - Code quality issues
  - Potential bugs
  - Security concerns
  - Performance bottlenecks
- Suggests specific improvements and fixes

## Prerequisites

- Python 3.8+
- Ollama with the following models:
  - deepseek-r1
  - nomic-embed-text

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Windows PowerShell
$env:OPENAI_BASE_URL="your-openai-base-url"
$env:OPENAI_API_KEY="your-openai-api-key"
```

## Usage

1. Start the application:
```bash
streamlit run deepseek-rag-agents-ui.py
```

2. Select an agent from the sidebar:
   - **Knowledge Agent**: For querying PDF documents
   - **Code Analysis**: For analyzing code quality
   - **Code Review**: For detailed code reviews

3. Based on the selected agent:
   - For Knowledge Agent: Type your question in the chat input
   - For Code Analysis/Review: Paste your code in the text area and click the respective button

## Project Structure

```
.
├── README.md
├── requirements.txt
├── deepseek-rag-agents-ui.py    # Main Streamlit UI
├── knowledge_agent.py           # Knowledge processing agent
├── code_analysis_agent.py       # Code analysis agent
├── code_review_agent.py         # Code review agent
├── code_analysis_docs.md        # Documentation for code analysis
└── code_review_docs.md          # Documentation for code review
```

## Configuration

Each agent can be configured through their respective files:

- `knowledge_agent.py`: Configure PDF processing and knowledge base settings
- `code_analysis_agent.py`: Customize code analysis parameters
- `code_review_agent.py`: Adjust code review preferences

## Error Handling

The application includes comprehensive error handling:
- Graceful handling of initialization errors
- Clear error messages for users
- Proper resource cleanup
- Timeout handling for long-running operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Uses [Ollama](https://ollama.ai/) for AI models
- Powered by the praisonaiagents package
