class Counter:
    def __init__(self, num: int = 0):
        self._value = num

    def increment(self, step: int = 1) -> None:
        self._value += step

    def decrement(self, step: int = 1) -> None:
        self._value -= step

    def get_value(self) -> int:
        return self._value


if __name__ == "__main__":
    counter = Counter()

    print("Начальное значение:", counter.get_value())

    counter.increment()
    print("После увеличения без параметра:", counter.get_value())

    counter.increment(7)
    print("После увеличения на 7:", counter.get_value())

    counter.decrement()
    print("После уменьшения без параметра:", counter.get_value())

    counter.decrement(3)
    print("После уменьшения на 3:", counter.get_value())
