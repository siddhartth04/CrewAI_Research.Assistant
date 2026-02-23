 # src/tools/arxiv_search.py
from langchain.tools import tool
import time

def perform_arxiv_search(query: str, max_results: int = 3) -> str:
    """
    Perform a real search on arXiv for academic papers.
    Args:
        query: Search term.
        max_results: Number of papers to return.
    Returns:
        Formatted string with paper details or error message.
    """
    try:
        import arxiv

        print(f"📚 REAL arXiv search: {query}")

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        for i, paper in enumerate(search.results()):
            authors = ', '.join(str(a) for a in paper.authors[:3])
            if len(paper.authors) > 3:
                authors += " et al."

            summary = paper.summary[:250] + "..." if len(paper.summary) > 250 else paper.summary

            result = f"""
### Paper {i+1}: {paper.title}
**Authors:** {authors}
**Published:** {paper.published.strftime('%Y-%m-%d')}
**Summary:** {summary}
**PDF:** {paper.pdf_url}
"""
            results.append(result)
            time.sleep(1)  # Be kind to the arXiv API

        if results:
            return "## 📚 REAL Academic Papers\n\n" + "\n---\n".join(results)
        else:
            return f"No papers found for: {query}"

    except ImportError:
        return "Error: Please install arxiv: pip install arxiv"
    except Exception as e:
        return f"ArXiv error: {str(e)}"

# Create a LangChain tool (for potential agent use)
arxiv_search_tool = tool(perform_arxiv_search)

# Class for easy use in the Streamlit app
class ArxivSearchTool:
    def search(self, query: str, max_results: int = 3) -> str:
        return perform_arxiv_search(query, max_results)