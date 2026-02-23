# src/crew_setup.py - 100% REAL
from crewai import Crew, Process, Task
from src.agents.research_agent import ResearchAgent
from src.agents.data_analyst import DataAnalyst
from src.agents.content_synthesizer import ContentSynthesizer
from src.agents.citation_manager import CitationManager
from src.agents.reviewer import ReviewerAgent
from src.models.hf_models import HuggingFaceModel
import time

class ResearchCrew:
    """REAL Research Crew that actually works together"""
    
    def __init__(self, topic, context="", audience="General Public", format_type="Detailed Report"):
        self.topic = topic
        self.context = context
        self.audience = audience
        self.format_type = format_type
        self.llm = HuggingFaceModel.get_llm("gpt2-medium")
        self.callbacks = []
        
    def add_callback(self, callback_func):
        """Add callback for progress updates"""
        self.callbacks.append(callback_func)
    
    def _notify(self, agent_name, status, message):
        """Notify all callbacks of progress"""
        for callback in self.callbacks:
            callback(agent_name, status, message)
    
    def setup_crew(self):
        """Setup the REAL agent crew"""
        
        # Create REAL agents
        self._notify("System", "starting", "Creating research agent...")
        research_agent = ResearchAgent.create(self.llm)
        
        self._notify("System", "starting", "Creating data analyst...")
        data_analyst = DataAnalyst.create(self.llm)
        
        self._notify("System", "starting", "Creating content writer...")
        content_writer = ContentSynthesizer.create(self.llm)
        
        self._notify("System", "starting", "Creating citation manager...")
        citation_manager = CitationManager.create(self.llm)
        
        self._notify("System", "starting", "Creating reviewer...")
        reviewer = ReviewerAgent.create(self.llm)
        
        # Define REAL tasks with clear instructions
        tasks = [
            Task(
                description=f"""
                CONDUCT REAL RESEARCH ON: {self.topic}
                
                Additional Context: {self.context}
                
                You MUST use your tools to find REAL information:
                1. Use 'web_search' tool to find recent articles and news
                2. Use 'arxiv_search' tool to find academic papers
                
                Find information about:
                - Latest developments and breakthroughs
                - Key statistics and data
                - Expert opinions and consensus
                - Controversies or debates
                - Future predictions
                
                For each source, note:
                - Where you found it
                - When it was published
                - Who wrote it
                - Key quotes or data points
                
                Return a comprehensive research summary with ALL your findings and sources.
                """,
                agent=research_agent,
                expected_output="Detailed research findings with multiple REAL sources"
            ),
            
            Task(
                description=f"""
                ANALYZE REAL DATA from the research about: {self.topic}
                
                Look for numerical data in the research findings:
                - Statistics and percentages
                - Growth rates and trends
                - Comparisons and rankings
                - Survey results
                
                For each set of numbers you find:
                1. Extract them into a comma-separated format
                2. Use 'analyze_trends' tool to get statistical analysis
                3. Use 'create_chart' tool to visualize the data
                
                If you find multiple datasets, analyze each one.
                If no numerical data exists, explain what data would be useful to collect.
                
                Return your analysis with charts and statistical insights.
                """,
                agent=data_analyst,
                expected_output="Data analysis with REAL charts and statistics"
            ),
            
            Task(
                description=f"""
                CREATE CONTENT from the REAL research about: {self.topic}
                
                Format: {self.format_type}
                Audience: {self.audience}
                
                Your content must include:
                1. Executive Summary
                2. Key Findings (with data support)
                3. Detailed Analysis
                4. Conclusions
                5. Recommendations
                
                Writing guidelines:
                - Use clear, engaging language appropriate for {self.audience}
                - Support every claim with research findings
                - Include relevant statistics and data
                - Organize information logically
                - Make it comprehensive but readable
                
                Return the complete {self.format_type}.
                """,
                agent=content_writer,
                expected_output=f"Complete {self.format_type} with all findings"
            ),
            
            Task(
                description=f"""
                ADD CITATIONS to all sources in the content about: {self.topic}
                
                You MUST:
                1. Identify every source mentioned in the content
                2. Format each source in APA style
                3. Create a References section at the end
                4. Add in-text citations where sources are used
                5. Ensure every claim has a citation
                
                APA format examples:
                - Book: Author, A. A. (Year). Title. Publisher.
                - Article: Author, A. A. (Year). Title. Journal, Volume(Issue), Pages.
                - Website: Author, A. A. (Year). Title. Site Name. URL
                
                Return the content with ALL citations properly formatted.
                """,
                agent=citation_manager,
                expected_output="Content with complete APA citations"
            ),
            
            Task(
                description=f"""
                REVIEW the entire research report on: {self.topic}
                
                Check for:
                1. Accuracy - Are all facts supported by sources?
                2. Citations - Are all sources properly cited?
                3. Completeness - Is anything missing?
                4. Clarity - Is it appropriate for {self.audience}?
                5. Format - Does it meet {self.format_type} standards?
                
                If you find ANY issues, list them with specific recommendations for fixes.
                If everything is correct, APPROVE the report.
                
                Return your review decision with justification.
                """,
                agent=reviewer,
                expected_output="Final approval or detailed revision requests"
            )
        ]
        
        # Create the crew
        crew = Crew(
            agents=[research_agent, data_analyst, content_writer, citation_manager, reviewer],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            cache=True
        )
        
        return crew
    
    def run(self):
        """Run the REAL research crew"""
        self._notify("System", "starting", f"Starting research on: {self.topic}")
        
        crew = self.setup_crew()
        
        self._notify("System", "working", "Crew assembled, beginning research...")
        
        try:
            # Run the crew
            result = crew.kickoff()
            
            self._notify("System", "completed", "Research complete!")
            
            return {
                'success': True,
                'output': str(result),
                'topic': self.topic,
                'format': self.format_type
            }
            
        except Exception as e:
            self._notify("System", "error", f"Error: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'topic': self.topic
            }