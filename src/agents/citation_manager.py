# src/agents/citation_manager.py - 

from crewai import Agent
from src.models.hf_models import HuggingFaceModel

class CitationManager:
    """ Citation Manager that actually formats references correctly"""
    
    @staticmethod
    def create(llm=None, verbose=True):
        """Create a Citation management agent"""
        
        if llm is None:
            llm = HuggingFaceModel.get_llm("gpt2")
        
        return Agent(
            role='Citation & Reference Manager',
            goal='Ensure every source is properly cited in correct academic format',
            backstory="""You are a REAL academic librarian with expertise in citation formats.
            You know APA, MLA, Chicago, IEEE, and Harvard referencing by heart.
            You have helped thousands of researchers publish papers in top journals.
            You never invent citations - you only format REAL sources correctly.
            Every citation you create is accurate and follows the proper format.""",
            llm=llm,
            verbose=verbose,
            allow_delegation=False,
            max_iterations=3
        )
