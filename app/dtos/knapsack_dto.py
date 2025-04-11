from pydantic import BaseModel
from app.dtos.combination_dto import CombinationDTO

class KnapsackDTO(BaseModel):
    capacity: int
    number_of_combinations: int
    combination: CombinationDTO
