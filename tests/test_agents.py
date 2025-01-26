"""Test cases for AI agents."""

import unittest
from ai_agents_hub.agents.knowledge_agent import create_knowledge_agent
from ai_agents_hub.agents.code_analysis_agent import create_code_analysis_agent
from ai_agents_hub.agents.code_review_agent import create_code_review_agent

class TestAgents(unittest.TestCase):
    """Test cases for agent creation and basic functionality."""
    
    def test_knowledge_agent_creation(self):
        """Test knowledge agent creation."""
        agent = create_knowledge_agent()
        self.assertIsNotNone(agent)
        self.assertEqual(agent.name, "Knowledge Agent")
    
    def test_code_analysis_agent_creation(self):
        """Test code analysis agent creation."""
        agent = create_code_analysis_agent()
        self.assertIsNotNone(agent)
        self.assertEqual(agent.name, "Code Analysis Agent")
    
    def test_code_review_agent_creation(self):
        """Test code review agent creation."""
        agent = create_code_review_agent()
        self.assertIsNotNone(agent)
        self.assertEqual(agent.name, "Code Review Agent")

if __name__ == '__main__':
    unittest.main()
