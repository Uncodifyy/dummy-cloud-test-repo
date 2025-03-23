from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI on Vercel!"}

@app.get("/test")
def test_endpoint():
    return {"message": "Test endpoint works 1!!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

