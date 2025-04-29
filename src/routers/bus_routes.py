from fastapi import APIRouter, HTTPException
from src.db.dbsetup import route_table, stop_bus, serialize_out
from src.models.bus_data import Bus
from typing import List

bus_router = APIRouter()

@bus_router.get("/stops/")
def get_all_stops():
    routes = stop_bus.find()

    out = []
    for route in routes:
        temp = serialize_out(route)
        out.append(temp.get("stopname"))
    
    return out 


@bus_router.get("/search/stop/", response_model=List[Bus])
def get_bus_by_stop(stop_name: str):
    print(stop_name)
    stop = stop_bus.find_one({"stopname": stop_name})
    
    if not stop:
        raise HTTPException(status_code=404, detail="Stop does not exist")
    
    out = []
    for busNum in stop.get("buses"):
        bus = route_table.find_one({"busNumber":busNum})
        out.append(serialize_out(bus))
    return out

@bus_router.get("/search/number/", response_model=Bus)
def get_bus_by_number(bus_number: int):
    bus = route_table.find_one({"busNumber": bus_number})
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return serialize_out(bus)