from pydantic import BaseModel

class ProductDTO(BaseModel):
    price: float
    quantity: int
    weight: float