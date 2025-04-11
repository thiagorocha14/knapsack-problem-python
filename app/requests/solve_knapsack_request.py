from pydantic import BaseModel
from app.dtos.product_dto import ProductDTO

class FillKnapsackRequest(BaseModel):
    products: list[ProductDTO]
    knapsack_capacity: int