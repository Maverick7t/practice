from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User {user_id} found",
    }


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id,
        "status": "available",
    }