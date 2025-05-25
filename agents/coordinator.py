from agents.tools import search_tool, summarize_tool

def orchestrate_task(query):
    result = search_tool(query)
    summary = summarize_tool(result)
    return {"original": result, "summary": summary}