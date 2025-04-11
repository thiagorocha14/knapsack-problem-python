from app.dtos.product_dto import ProductDTO
from app.dtos.combination_dto import CombinationDTO

class CombinationService:

    @staticmethod
    def create_combination(index, products: list[ProductDTO]):

        bases = [product.quantity for product in products]

        selected_products = CombinationService.select_products(index,bases)
        price, weight = CombinationService.calculate_price_and_weight(selected_products, products)

        return CombinationDTO(price=price, weight=weight, products=selected_products)

    @staticmethod
    def select_products(index, bases):
        selected_products = []
        quotient = index
        bases.reverse()

        for base in bases:
            rest = quotient % (base + 1)
            quotient = quotient // (base + 1)
            selected_products.insert(0, rest)

        bases.reverse()

        return selected_products

    @staticmethod
    def calculate_price_and_weight(selected_products, products):
        price = 0
        weight = 0

        for (index, quantity) in enumerate(selected_products):
            price += products[index].price * quantity
            weight += products[index].weight * quantity

        return price, weight
