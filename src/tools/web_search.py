 # src/tools/web_search.py
from langchain.tools import tool
import time
import sys

def perform_web_search(query: str, max_results: int = 5) -> str:
    """
    Perform a real web search using DuckDuckGo.
    """
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        return "Error: Please install duckduckgo-search: pip install duckduckgo-search"

    print(f"🔍 REAL web search: {query}")

    try:
        with DDGS() as ddgs:
            results = []
            # Use a timeout and handle potential errors
            for i, r in enumerate(ddgs.text(query, max_results=max_results)):
                title = r.get('title', 'No title')
                body = r.get('body', 'No description')
                href = r.get('href', '#')

                result = f"""
### Result {i+1}: {title}
**Description:** {body[:300]}...
**URL:** {href}
"""
                results.append(result)
                time.sleep(1)  # Be respectful to the API

            if results:
                return "## 🌐 REAL Web Search Results\n\n" + "\n---\n".join(results)
            else:
                return f"No results found for: {query}"

    except Exception as e:
        # Catch and return a clear error message
        return f"Web search error: {str(e)}. This may be due to network issues or DuckDuckGo blocking the request. Try again later."

# Create a LangChain tool (for potential agent use)
web_search_tool = tool(perform_web_search)

# Class for easy use in the Streamlit app
class WebSearchTool:
    def search(self, query: str, max_results: int = 5) -> str:
        return perform_web_search(query, max_results)