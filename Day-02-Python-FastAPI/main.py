from fastapi import FastAPI
from routes.users import router as users_router
from routes.products import router as products_router

app = FastAPI()
app.include_router(users_router)
app.include_router(products_router)

@app.get("/")
def home():
    return {"message": "Hello,FastAPI!"}

