from controller.commands import GuessCommand, IsGameOverCommand
from controller.invoker import Invoker
from controller.receiver import NumberGenerator

if __name__ == '__main__':
    invoker = Invoker()
    receiver = NumberGenerator()

    invoker.set_guess_number(GuessCommand(receiver))
    invoker.set_game_status(IsGameOverCommand(receiver))

    while True:
        number = int(input("Guess a number: "))
        invoker.guess_number(number)

        if invoker.is_game_over():
            break

