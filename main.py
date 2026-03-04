from fastapi import FastAPI
from agent import root_agent

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Zoo Guide Agent is running"}

@app.get("/agent")
def run_agent():
    result = root_agent.run(
        input="Tell me about lions"
    )
    return {"response": result}