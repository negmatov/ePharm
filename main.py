from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    print ("Test Git")
    return {"data": "Pharmacy list "}