from datetime import date
from typing import List

from pydantic import BaseModel, Field


# request body и pydantic модели - урок 3
class WorkHours(BaseModel):
    name: str


# Body - урок 6 + # pydantic Field - урок 8
class Owner(BaseModel):
    first_name: str = Field(..., max_length=15, min_length=3)
    last_name: str = Field(..., max_length=15, min_length=3)
    age: int = Field(..., gt=18, lt=90, description="Возраст владельца должен быть старше 18 и меньше 90 лет.")



class Pharmacy(BaseModel):
    name_pharm: str
    phone: str
    call_center: str
    fax: str
    address: str
    way_mark: str
    working_hours: List[WorkHours]
    location: float
    refresh: date
