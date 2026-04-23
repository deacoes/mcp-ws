from mcp.server.fastmcp import FastMCP
from ddgs import get_results
import logging

mcp = FastMCP("WebSearch")

@mcp.tool()
def search_web(query: str, max_results: int = 5) -> str:
    """
    Performs a web search using DuckDuckGo to get up-to-date information.
    Args:
        query: The search string.
        max_results: Number of results to return (default 5).
    """
    try:
        results = list(get_results(query, max_results=max_results))
        if not results:
            return "No results found."

        formatted_results = []
        for r in results:
            formatted_results.append(f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}\n---")

        return "\n".join(formatted_results)
    except Exception as e:
        return f"Error during search: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")