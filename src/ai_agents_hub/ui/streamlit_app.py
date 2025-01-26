"""Streamlit UI for AI Agents Hub."""

import streamlit as st
from rich.console import Console
import sys
import tracemalloc
import warnings

from ai_agents_hub.agents.code_analysis_agent import create_code_analysis_agent
from ai_agents_hub.agents.code_review_agent import create_code_review_agent
from ai_agents_hub.agents.knowledge_agent import create_knowledge_agent
from ai_agents_hub.agents.chat_agent import create_chat_agent, process_chat
from ai_agents_hub.agents.adaptive_learning_agent import create_adaptive_learning_agent, process_learning

# Enable tracemalloc for better resource tracking
tracemalloc.start()

# Filter ResourceWarnings about unclosed sockets
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*socket")

# Disable Rich's live display for streamlit compatibility
console = Console(force_terminal=False)
sys.stdout = console.file

def init_session_state():
    """Initialize Streamlit session state."""
    if "agents_initialized" not in st.session_state:
        st.session_state.messages = []
        st.session_state.agents_initialized = True
        st.session_state.knowledge_agent_initialized = False
        st.session_state.code_analysis_agent_initialized = False
        st.session_state.code_review_agent_initialized = False
        st.session_state.chat_agent_initialized = False
        st.session_state.adaptive_learning_initialized = False
        st.session_state.current_student_id = None

def handle_knowledge_agent():
    """Handle Knowledge Agent interactions."""
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

def handle_code_analysis():
    """Handle Code Analysis Agent interactions."""
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

def handle_code_review():
    """Handle Code Review Agent interactions."""
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

def handle_chat_agent():
    """Handle Chat Agent interactions."""
    if not st.session_state.get("chat_agent_initialized"):
        with st.spinner("Initializing Chat Agent..."):
            try:
                st.session_state.chat_agent = create_chat_agent()
                st.session_state.chat_agent_initialized = True
            except Exception as e:
                st.error(f"Error initializing Chat Agent: {str(e)}")
                st.stop()

    prompt = st.chat_input("Type your message here...")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    response = process_chat(prompt).content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error processing request: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

def handle_adaptive_learning():
    """Handle Adaptive Learning Agent interactions."""
    if not st.session_state.get("adaptive_learning_initialized"):
        with st.spinner("Initializing Adaptive Learning Agent..."):
            try:
                st.session_state.adaptive_learning_agent = create_adaptive_learning_agent()
                st.session_state.adaptive_learning_initialized = True
            except Exception as e:
                st.error(f"Error initializing Adaptive Learning Agent: {str(e)}")
                st.stop()
    
    # Student ID input
    if not st.session_state.current_student_id:
        student_id = st.text_input("Enter Student ID:")
        if student_id:
            st.session_state.current_student_id = student_id
    
    if st.session_state.current_student_id:
        # Topic selection
        topic = st.text_input("Enter Learning Topic:")
        
        if topic:
            if st.button("Start Learning Session"):
                with st.spinner("Processing learning session..."):
                    try:
                        results = process_learning(st.session_state.current_student_id, topic)
                        
                        # Display results in an organized way
                        st.subheader("Learning Session Results")
                        
                        # Assessment
                        if results.get("assessment"):
                            st.write("📊 Current Level:", results["assessment"])
                        
                        # Content
                        if results.get("content"):
                            st.write("📚 Learning Content:", results["content"])
                        
                        # Performance
                        if results.get("performance"):
                            st.write("📈 Performance:", results["performance"])
                        
                        # Adaptation
                        if results.get("adaptation"):
                            st.write("🔄 Next Steps:", results["adaptation"])
                        
                        # Error handling
                        if results.get("error"):
                            st.error(f"Error during learning session: {results['error']}")
                        
                        # Add to message history
                        message = f"""Learning Session Summary:
                        Topic: {topic}
                        Level: {results.get('assessment', 'N/A')}
                        Performance: {results.get('performance', 'N/A')}
                        Next Steps: {results.get('adaptation', 'N/A')}
                        """
                        st.session_state.messages.append({"role": "assistant", "content": message})
                        
                    except Exception as e:
                        st.error(f"Error during learning session: {str(e)}")
        
        # Option to reset student
        if st.button("Change Student"):
            st.session_state.current_student_id = None
            st.rerun()

def main():
    """Main application entry point."""
    st.title("AI Agents Hub")
    
    init_session_state()

    # Agent selection
    agent_type = st.sidebar.selectbox(
        "Select Agent Type",
        ["General Chat", "Knowledge Agent", "Code Analysis", "Code Review", "Adaptive Learning"],
        index=0  # Make General Chat the default
    )

    # Display chat history
    if "messages" in st.session_state:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Handle different agent types
    if agent_type == "General Chat":
        handle_chat_agent()
    elif agent_type == "Knowledge Agent":
        handle_knowledge_agent()
    elif agent_type == "Code Analysis":
        handle_code_analysis()
    elif agent_type == "Code Review":
        handle_code_review()
    else:  # Adaptive Learning
        handle_adaptive_learning()

if __name__ == "__main__":
    main()
