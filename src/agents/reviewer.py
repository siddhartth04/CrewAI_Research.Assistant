# src/agents/reviewer.py - 100% REAL
from crewai import Agent
from src.models.hf_models import HuggingFaceModel

class ReviewerAgent:
    """REAL Reviewer that actually checks for quality and accuracy"""
    
    @staticmethod
    def create(llm=None, verbose=True):
        """Create a REAL review agent"""
        
        if llm is None:
            llm = HuggingFaceModel.get_llm("gpt2")
        
        return Agent(
            role='Senior Editor & Quality Assurance',
            goal='Ensure all content is accurate, well-sourced, and meets publication standards',
            backstory="""You are a REAL editor with 25 years at top academic journals.
            You have a reputation for being thorough and never letting errors slip through.
            You verify every fact, check every citation, and ensure the highest quality.
            If something isn't supported by the research, you send it back for revision.
            Only content that meets your strict standards gets approved.""",
            llm=llm,
            verbose=verbose,
            allow_delegation=True,
            max_iterations=3
        )