from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "practice-fastapi",
    }


@app.get("/")
async def root():
    return {
        "message": "FastAPI practice repository"
    } 