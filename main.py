from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers.bus_routes import bus_router

current_version = "v2"

app = FastAPI(
    title="SAGE BUS NAVIGATOR",
    description="A bus navigation app for SAGEians",
    version=current_version
)

app.include_router(
    bus_router,
    prefix=f"/api/{current_version}/bus",
    tags=["bus"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




