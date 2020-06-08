from controller.commands import GuessCommand, IsGameOverCommand


class Invoker:
    _guess_number = None
    _game_status = None

    def set_guess_number(self, command: GuessCommand) -> None:
        self._guess_number = command

    def set_game_status(self, command: IsGameOverCommand) -> None:
        self._game_status = command

    def guess_number(self, number: int) -> None:
        self._guess_number.execute(number)

    def is_game_over(self) -> bool:
        return self._game_status.execute()
