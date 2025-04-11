from app.controllers.knapsack_controller import router
from fastapi import FastAPI

app = FastAPI(root_path="/api")
app.include_router(router)

