import random


class NumberGenerator:
    number: int = None
    is_game_over: bool = False

    def generate_number(self) -> None:
        self.number = random.randint(0, 100)

    def compare_number(self, other_number: int) -> None:
        if other_number < self.number:
            self.smaller_hint()
        elif other_number > self.number:
            self.bigger_hint()
        else:
            self.win_hint()
            self.is_game_over = True

    def bigger_hint(self) -> None:
        print("Your number is too big. Try again!")

    def smaller_hint(self) -> None:
        print("Your number is too small. Try again!")

    def win_hint(self) -> None:
        print("Congratulations! You've guessed the number!")
