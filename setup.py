from setuptools import setup, find_packages

setup(
    name="ai-agents-hub",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit>=1.29.0",
        "praisonaiagents>=0.0.57",
        "rich>=13.7.0",
        "chromadb>=0.4.18",
    ],
    author="Infinitiflow Team",
    description="A multi-agent system for code analysis, review, and knowledge processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
