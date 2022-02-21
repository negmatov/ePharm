from typing import List
from pydantic import BaseModel
from datetime import date

#request body и pydantic модели - урок 3
class work_hours(BaseModel):
    name: str

class Pharmacy(BaseModel):
    name_pharm: str
    phone: str
    call_center: str
    fax: str
    address: str
    way_mark: str
    working_hours: List[work_hours]
    location: float
    refresh: date