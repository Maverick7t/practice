from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
async def search(
    q: str,
    page: int = 1,
    limit: int = 10,
):
    return {
        "query": q,
        "page": page,
        "limit": limit,
    }


@app.get("/products")
async def list_products(
    category: str | None = None,
):
    return {
        "category": category,
    }