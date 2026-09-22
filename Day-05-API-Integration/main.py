from fastapi import FastAPI, Header, HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Day 5 API Integration is running"}


@app.get("/protected")
def protected(api_key: str = Header()):
    if api_key != "my-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "message": "You accessed a protected endpoint"
    }
