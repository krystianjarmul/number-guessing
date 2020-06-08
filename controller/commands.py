import abc

from controller.receiver import NumberGenerator


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass


class GuessCommand(Command):
    def __init__(self, receiver: NumberGenerator):
        self._receiver = receiver

    def execute(self, number: int) -> None:
        if not self._receiver.number:
            self._receiver.generate_number()
        self._receiver.compare_number(number)


class IsGameOverCommand(Command):
    def __init__(self, receiver: NumberGenerator):
        self._receiver = receiver

    def execute(self) -> bool:
        if not self._receiver.is_game_over:
            return False
        return True
