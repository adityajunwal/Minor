from fastapi import APIRouter, HTTPException
from db.dbsetup import route_table, stop_bus, serialize_out
from typing import List
from models.bus_data import Bus

admin_router = APIRouter()

admin_router.get("/")
def admin_root():
    return {"message": "Welcome to the Admin Dashboard"}

admin_router.get("/buses", response_model=List[Bus])
def get_all_buses():
    buses = stop_bus.find()
    out = {serialize_out(bus) for bus in buses}

    return out

admin_router.post("/bus/", response_model=Bus)
def add_bus(bus: Bus):
    stop_bus.insert_one(bus)
    

    