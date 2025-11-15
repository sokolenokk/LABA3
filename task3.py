from typing import Optional, List


class Student:
    def __init__(
        self,
        name: str,
        age: int,
        group: str,
        grades: Optional[List[int]] = None,
    ):
        self.name = name
        self.age = age
        self.group = group

        if grades is None:
            self._grades: List[int] = []
        else:
            self._grades = list(grades)

    def add_grade(self, grade: int) -> None:
        if not isinstance(grade, int):
            raise TypeError("Оценка должна быть целым числом")

        if grade < 0 or grade > 100:
            raise ValueError("Оценка должна быть в диапазоне от 0 до 100")

        self._grades.append(grade)

    def get_average_grade(self) -> Optional[float]:
        if not self._grades:
            return None

        summ = sum(self._grades)
        count = len(self._grades)

        return summ / count

    def get_info(self) -> str:
        average = self.get_average_grade()

        if average is None:
            answer = "нет оценок"
        else:
            answer = f"{average:.2f}"

        information = (
            f"Студент: {self.name}\n"
            f"Возраст: {self.age}\n"
            f"Группа: {self.group}\n"
            f"Оценки: {self._grades if self._grades else 'нет'}\n"
            f"Средний балл: {answer}"
        )

        return information


if __name__ == "__main__":
    student = Student(name="Степан Соколовский", age=20, group="221131")

    student.add_grade(81)
    student.add_grade(40)
    student.add_grade(100)

    info = student.get_info()
    print(info)
