from pydantic import BaseModel

class CombinationDTO(BaseModel):
    price: float
    weight: float
    products: list

