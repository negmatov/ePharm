from typing import List
from pydantic import BaseModel, validator
from datetime import date


# request body и pydantic модели - урок 3
class WorkHours(BaseModel):
    name: str


# Body - урок 6
class Owner(BaseModel):
    first_name: str
    last_name: str
    age: int

    # пишем свой валидатор поля в pydantic - урок 7
    @validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('Возраст владельца должен быть больше 18 лет')
        return v

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
