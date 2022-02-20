from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"data": "Pharmacy list"}
