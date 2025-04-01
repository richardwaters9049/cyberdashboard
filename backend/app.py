from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend is working!!!"}


@app.post("/analyze")
async def analyze_file():
    return {"status": "Analysis complete", "result": "Sample result"}
