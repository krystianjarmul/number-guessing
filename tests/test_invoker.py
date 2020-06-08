import unittest
from unittest import mock
from controller.invoker import Invoker
from controller.commands import GuessCommand, IsGameOverCommand


class TestInvoker(unittest.TestCase):
    def setUp(self) -> None:
        self.invoker = Invoker()

    @mock.patch('controller.receiver.NumberGenerator')
    def test_set_guess_number_should_implement_GuessCommand(self, receiver_mock):
        self.invoker.set_guess_number(GuessCommand(receiver_mock))

        self.assertTrue(self.invoker._guess_number)

    @mock.patch('controller.receiver.NumberGenerator')
    def test_set_game_status_should_implement_IsGameOverCommand(self,
                                                             receiver_mock):
        self.invoker.set_game_status(IsGameOverCommand(receiver_mock))

        self.assertTrue(self.invoker._game_status)

    @mock.patch('controller.receiver.NumberGenerator')
    @mock.patch.object(GuessCommand, 'execute')
    def test_set_guess_number_should_execute_guess_command(self,
                                                           execute_mock,
                                                           receiver_mock):
        self.invoker.set_guess_number(GuessCommand(receiver_mock))
        number = 74

        self.invoker.guess_number(number)

        execute_mock.assert_called_with(number)

    @mock.patch('controller.receiver.NumberGenerator')
    @mock.patch.object(IsGameOverCommand, 'execute')
    def test_set_game_status_should_execute_game_over_command(self,
                                                           execute_mock,
                                                           receiver_mock):
        self.invoker.set_game_status(IsGameOverCommand(receiver_mock))

        self.invoker.is_game_over()

        execute_mock.assert_called_once()

if __name__ == '__main__':
    unittest.main()
