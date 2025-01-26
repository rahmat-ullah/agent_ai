import streamlit as st
from code_analysis_agent import create_code_analysis_agent
from code_review_agent import create_code_review_agent
from knowledge_agent import create_knowledge_agent
import tracemalloc
import warnings
from rich.console import Console
import sys

# Enable tracemalloc for better resource tracking
tracemalloc.start()

# Filter ResourceWarnings about unclosed sockets
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*socket")

# Disable Rich's live display for streamlit compatibility
console = Console(force_terminal=False)
sys.stdout = console.file

st.title("AI Agents Hub")

# Initialize agents with proper resource management
if "agents_initialized" not in st.session_state:
    st.session_state.messages = []
    st.session_state.agents_initialized = True
    st.session_state.knowledge_agent_initialized = False
    st.session_state.code_analysis_agent_initialized = False
    st.session_state.code_review_agent_initialized = False

# Agent selection
agent_type = st.sidebar.radio(
    "Select Agent Type",
    ["Knowledge Agent", "Code Analysis", "Code Review"]
)

if "messages" in st.session_state:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input section based on agent type
if agent_type == "Knowledge Agent":
    if not st.session_state.get("knowledge_agent_initialized"):
        with st.spinner("Initializing Knowledge Agent..."):
            try:
                st.session_state.knowledge_agent = create_knowledge_agent()
                st.session_state.knowledge_agent_initialized = True
            except Exception as e:
                st.error(f"Error initializing Knowledge Agent: {str(e)}")
                st.stop()

    prompt = st.chat_input("Ask a question...")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                with st.spinner("Processing your question..."):
                    response = st.session_state.knowledge_agent.start(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error processing request: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

elif agent_type == "Code Analysis":
    if not st.session_state.get("code_analysis_agent_initialized"):
        with st.spinner("Initializing Code Analysis Agent..."):
            try:
                st.session_state.code_analysis_agent = create_code_analysis_agent()
                st.session_state.code_analysis_agent_initialized = True
            except Exception as e:
                st.error(f"Error initializing Code Analysis Agent: {str(e)}")
                st.stop()

    st.subheader("Code Analysis")
    code_input = st.text_area("Paste your code here for analysis", height=200)
    analyze_button = st.button("Analyze Code")
    
    if analyze_button and code_input:
        st.session_state.messages.append({"role": "user", "content": "Analyzing code:\n```\n" + code_input + "\n```"})
        with st.chat_message("user"):
            st.markdown("Analyzing code...")

        with st.chat_message("assistant"):
            try:
                with st.spinner("Analyzing code..."):
                    response = st.session_state.code_analysis_agent.start(
                        f"""Please analyze this code and provide a detailed report:
                        ```
                        {code_input}
                        ```
                        """
                    )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error analyzing code: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

else:  # Code Review
    if not st.session_state.get("code_review_agent_initialized"):
        with st.spinner("Initializing Code Review Agent..."):
            try:
                st.session_state.code_review_agent = create_code_review_agent()
                st.session_state.code_review_agent_initialized = True
            except Exception as e:
                st.error(f"Error initializing Code Review Agent: {str(e)}")
                st.stop()

    st.subheader("Code Review")
    code_input = st.text_area("Paste your code here for review", height=200)
    review_button = st.button("Review Code")
    
    if review_button and code_input:
        st.session_state.messages.append({"role": "user", "content": "Reviewing code:\n```\n" + code_input + "\n```"})
        with st.chat_message("user"):
            st.markdown("Reviewing code...")

        with st.chat_message("assistant"):
            try:
                with st.spinner("Reviewing code..."):
                    response = st.session_state.code_review_agent.start(
                        f"""Please review this code and provide detailed feedback:
                        ```
                        {code_input}
                        ```
                        Focus on:
                        1. Code quality and style
                        2. Potential bugs and issues
                        3. Security concerns
                        4. Performance improvements
                        5. Best practices
                        """
                    )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error reviewing code: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
