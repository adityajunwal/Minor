from fastapi import APIRouter, HTTPException
from db.dbsetup import route_table, stop_bus, serialize_out
from models.bus_data import Bus

bus_router = APIRouter()

@bus_router.get("/stops/")
def get_all_stops():
    routes = stop_bus.find()
    out = []
    for route in routes:
        out.append(route["stopname"])
    return out


@bus_router.get("/search/{stop_name}", response_model=Bus)
def get_bus_by_stop(stop_name: str):
    buses = stop_bus.find_one({"stopname": stop_name})
    if not buses:
        raise HTTPException(status_code=404, detail="Stop does not exist")
    
    return buses["buses"]

@bus_router.get("/search/{bus_number}", response_class=Bus)
def get_bus_by_number(bus_number: int):
    bus = route_table.find_one({"busNumber": bus_number})
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return serialize_out(bus)