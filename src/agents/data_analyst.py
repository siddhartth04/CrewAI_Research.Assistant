# src/agents/data_analyst.py - 100% REAL
from crewai import Agent
from src.tools.data_viz import DataVisualizationTool
from src.models.hf_models import HuggingFaceModel

class DataAnalyst:
    """REAL Data Analyst that actually analyzes numbers and creates visualizations"""
    
    @staticmethod
    def create(llm=None, verbose=True):
        """Create a REAL data analyst agent"""
        
        if llm is None:
            llm = HuggingFaceModel.get_llm("gpt2")
        
        # Initialize REAL tools
        viz_tool = DataVisualizationTool()
        
        return Agent(
            role='Senior Data Analyst',
            goal='Perform REAL statistical analysis and create accurate data visualizations',
            backstory="""You are a REAL data scientist with a Master's in Statistics.
            You have worked at top companies analyzing REAL data and finding insights.
            You never guess or make up numbers - you only analyze actual data provided.
            You can spot trends, outliers, and patterns that others miss.
            Your visualizations are clear, accurate, and informative.""",
            tools=[
                viz_tool.create_chart,
                viz_tool.analyze_trends
            ],
            llm=llm,
            verbose=verbose,
            allow_delegation=True,
            max_iterations=4
        )