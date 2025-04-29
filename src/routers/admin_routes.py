from fastapi import APIRouter, HTTPException
from src.db.dbsetup import route_table, serialize_out
from typing import List
from src.models.bus_data import Bus, BusAdd
from bson import ObjectId

admin_router = APIRouter()

@admin_router.get("/")
def admin_root():
    return {"message": "Welcome to the Admin Dashboard"}

@admin_router.get("/buses", response_model=List[Bus])
def get_all_buses():
    buses = route_table.find()
    out = [serialize_out(bus) for bus in buses]

    return out

@admin_router.post("/bus/", response_model=Bus)
def add_bus(bus: BusAdd):
    new_bus = bus.model_dump(by_alias=True, exclude_unset=True)
    res = route_table.insert_one(new_bus)
    new_bus["_id"] = res.inserted_id
    
    return serialize_out(new_bus)

@admin_router.put("/bus/", response_model=Bus)
def update_bus(bus: Bus):
    bus_update_id = bus._id
    bus_to_update = route_table.find_one_and_update(
        {"_id": ObjectId(bus_update_id)},
        {"$set": bus.model_dump(by_alias=True, exclude_unset=True)},
        return_document=True
    )

    return serialize_out(bus_to_update)


    