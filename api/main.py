from fastapi import FastAPI
from agents.coordinator import orchestrate_task

app = FastAPI()

@app.get("/run")
def run_agent(query: str):
    return orchestrate_task(query)