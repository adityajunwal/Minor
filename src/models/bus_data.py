from pydantic import BaseModel
from typing import List

class Route(BaseModel):
    serialNumber: int
    busStop: str
    timing1: str
    timing2: str


class Bus(BaseModel):
    _id: str
    busNumber: int
    driverName: str
    registrationNumber: str
    routeTable: List[Route]
    routeMap: str

class BusAdd(BaseModel):
    busNumber: int
    driverName: str
    registrationNumber: str
    routeTable: List[Route]
    routeMap: str

