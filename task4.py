from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price: float) -> float:
        pass


class NoDiscountStrategy(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price


class PercentageDiscountStrategy(PricingStrategy):
    def __init__(self, discount_rate: float):
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Процент скидки должен быть от 0 до 1")
        self._discount_rate = discount_rate

    def calculate(self, base_price: float) -> float:
        discount_amount = base_price * self._discount_rate
        return base_price - discount_amount


class FixedDiscountStrategy(PricingStrategy):
    def __init__(self, discount_amount: float):
        if discount_amount < 0:
            raise ValueError("Сумма скидки не может быть отрицательной")
        self._discount_amount = discount_amount

    def calculate(self, base_price: float) -> float:
        answer = base_price - self._discount_amount
        return max(answer, 0.0)


class PriceCalculator:
    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PricingStrategy) -> None:
        self._strategy = strategy

    def calculate_price(self, base_price: float) -> float:
        if base_price < 0:
            raise ValueError("Изначальная цена не может быть отрицательной")
        return self._strategy.calculate(base_price)


if __name__ == "__main__":
    start_price = 100.0

    calculator = PriceCalculator(NoDiscountStrategy())
    price_no_discount = calculator.calculate_price(start_price)
    print(f"Изначальная цена: {start_price}, без скидки: {price_no_discount}")

    calculator.set_strategy(PercentageDiscountStrategy(0.70))
    price_70_percent = calculator.calculate_price(start_price)
    print(f"Изначальная цена: {start_price}, со скидкой 70%: {price_70_percent}")

    calculator.set_strategy(FixedDiscountStrategy(22.3))
    price_fix_discount = calculator.calculate_price(start_price)
    print(f"Изначальная цена: {start_price}, со скидкой 22.3 рубля: {price_fix_discount}")



