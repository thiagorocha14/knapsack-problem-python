from app.dtos.product_dto import ProductDTO
from app.dtos.knapsack_dto import KnapsackDTO
from app.dtos.combination_dto import CombinationDTO
from app.services.combination_service import CombinationService

class KnapsackService:

    def __init__(self):
        self.knapsack = KnapsackDTO(capacity=0, number_of_combinations=0, combination=CombinationDTO(price=0, weight=0, products=[]))

    def solve(self, products: list[ProductDTO], knapsack_capacity: int):
        self.knapsack.capacity = knapsack_capacity
        self.knapsack.number_of_combinations = self.__calculate_number_of_combinations(products)

        begin = 0
        end = self.knapsack.number_of_combinations

        for i in range(begin, end):

            combination = CombinationService.create_combination(i, products)

            if (not self.__can_store_product(combination, knapsack_capacity)):
                continue

            if (self.__is_better_combination(combination)):
                self.knapsack.combination = combination

        return self.knapsack


    def __calculate_number_of_combinations(self, products: list[ProductDTO]):
        quantities = [product.quantity + 1 for product in products]

        size = 1
        for quantity in quantities:
            size *= quantity

        return size

    def __can_store_product(self, combination: CombinationDTO, knapsack_capacity: int):
        return combination.weight <= knapsack_capacity

    def __is_better_combination(self, combination: CombinationDTO):
        if (combination.price > self.knapsack.combination.price):
            return True

        if (combination.price == self.knapsack.combination.price):
            if (combination.weight < self.knapsack.combination.weight):
                return True

        return False
