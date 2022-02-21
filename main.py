from fastapi import FastAPI, Query, Path, Body
from schemas import Pharmacy, Owner
from typing import List

app = FastAPI()


# Response и response_model - урок 9


# Path параметры и валидация - урок 5
@app.get("/pharmacy/{pk}")
async def get_singel_pharmacy(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}


# Query параметры и валидация - урок 4
@app.get("/pharmacy")
async def get_pharmacy(q: List[str] = Query(["Test1", "Teat2"], description="Search Pharmacy")):
    return q


# request body и pydantic модели - урок 3 +  # Body - урок 6
@app.post("/add-pharm")
async def create_pharmacy(item: Pharmacy, owner: Owner, quantity: int = Body(...)):
    return {"item": item, "owner": owner, "quantity": quantity}


@app.post("/owner")
async def create_owner(owner: Owner = Body(..., embed=True)):
    return {"owner": owner}


# request body и pydantic модели - урок 3
@app.get("/user/{pk}/items/{item}")
async def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


# работа с url - урок 2
@app.get("/{pk}")
async def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}


@app.get("/home/{name}")
async def say_hello(name: str):
    return {"message": f"Салом Алейкум {name}"}


# создание и обзор проекта - урок 1
@app.get("/")
async def home():
    return {"message": "Салом Алейкум, ман дар саҳифаи аввал"}