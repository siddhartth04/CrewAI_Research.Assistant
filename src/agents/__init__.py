# src/agents/__init__.py
"""REAL Agent Definitions"""
from .research_agent import ResearchAgent
from .data_analyst import DataAnalyst
from .content_synthesizer import ContentSynthesizer
from .citation_manager import CitationManager
from .reviewer import ReviewerAgent

__all__ = [
    'ResearchAgent',
    'DataAnalyst',
    'ContentSynthesizer',
    'CitationManager',
    'ReviewerAgent'
]