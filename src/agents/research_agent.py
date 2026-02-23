# src/agents/research_agent.py s
from crewai import Agent
from src.tools.web_search import WebSearchTool
from src.tools.arxiv_search import ArxivSearchTool
from src.models.hf_models import HuggingFaceModel

class ResearchAgent:
    """REAL Research Agent that actually searches and gathers information"""
    
    @staticmethod
    def create(llm=None, verbose=True):
        """Create a REAL research agent"""
        
        if llm is None:
            llm = HuggingFaceModel.get_llm("gpt2-medium")
        
        # Initialize REAL tools
        web_search = WebSearchTool()
        arxiv_search = ArxivSearchTool()
        
        return Agent(
            role='Senior Research Analyst',
            goal='Find comprehensive, accurate, and REAL information from the web and academic sources',
            backstory="""You are a REAL research analyst with a PhD in Information Science.
            You have 20 years of experience in academic and market research.
            You NEVER make up information - you only use REAL data from your search tools.
            You verify facts across multiple sources and always cite where you found information.
            Your research is thorough, accurate, and reliable.""",
            tools=[
                web_search.search,
                arxiv_search.search
            ],
            llm=llm,
            verbose=verbose,
            allow_delegation=True,
            max_iterations=5,
            max_rpm=10
        )