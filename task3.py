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

    def get_info(self) -> str:
        info = (
            f"Студент: {self.name}\n"
            f"Возраст: {self.age}\n"
            f"Группа: {self.group}\n"
            f"Оценки: {self._grades if self._grades else 'нет'}\n"
        )

        return info


if __name__ == "__main__":
    student = Student(name="Степан Соколовский", age=20, group="221131")

    info = student.get_info()
    print(info)
