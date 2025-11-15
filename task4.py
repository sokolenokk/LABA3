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
