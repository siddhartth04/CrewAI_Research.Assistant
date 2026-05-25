# src/agents/content_synthesizer.py 
from crewai import Agent
from src.models.hf_models import HuggingFaceModel

class ContentSynthesizer:
    """ Content Writer that actually synthesizes information into coherent content"""
    
    @staticmethod
    def create(llm=None, verbose=True):
        """Create a REAL content synthesis agent"""
        
        if llm is None:
            llm = HuggingFaceModel.get_llm("gpt2-medium")
        
        return Agent(
            role='Content Synthesis Specialist',
            goal='Transform REAL research findings into well-structured, accurate, and engaging content',
            backstory="""You are a REAL technical writer with 15 years of experience.
            You have written for publications like Wired, TechCrunch, and academic journals.
            You take REAL research findings and turn them into clear, readable content.
            You never add fictional information - you only synthesize what the research found.
            Your writing is engaging, accurate, and tailored to the target audience.""",
            llm=llm,
            verbose=verbose,
            allow_delegation=False,
            max_iterations=4
        )
