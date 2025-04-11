from fastapi import APIRouter, HTTPException
from app.requests.solve_knapsack_request import FillKnapsackRequest
from app.dtos.product_dto import ProductDTO
from app.services.knapsack_service import KnapsackService
import time

router = APIRouter()
service = KnapsackService()

@router.post("/solve")
def solve(data: FillKnapsackRequest):
    try:
        start_time = time.time()

        if not data.products or not data.knapsack_capacity:
            raise HTTPException(status_code=400, detail="Products and knapsack capacity are required")

        if data.knapsack_capacity <= 0:
            raise HTTPException(status_code=400, detail="Knapsack capacity must be greater than 0")

        solution = service.solve(data.products, data.knapsack_capacity)

        end_time = time.time()
        execution_time = end_time - start_time

        return {
            "solution": solution,
            "message": "Knapsack problem solved successfully",
            "execution_time": execution_time
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))