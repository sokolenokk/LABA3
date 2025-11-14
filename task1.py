class PalindromeAnalyzer:
    @staticmethod
    def is_palindrome(text: str) -> bool:
        normalized = text.lower()

        cleaned = "".join(character for character in normalized if character.isalnum())

        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_palindrome = [
        "Madam, I’m Adam",
        "I'm Stepan",
        "Искать такси",
        "Я - Степан",
        "12321",
        "76543",
    ]

    for i in test_palindrome:
        answer = PalindromeAnalyzer.is_palindrome(i)
        print(f"'{i}' -> {'палиндром' if answer else 'не является полиндромом'}")
