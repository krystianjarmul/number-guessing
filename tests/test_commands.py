import unittest
from unittest import mock

from controller.commands import GuessCommand, IsGameOverCommand
from controller.receiver import NumberGenerator


class TestGuessCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.receiver = NumberGenerator()

    @mock.patch.object(NumberGenerator, 'generate_number')
    @mock.patch.object(NumberGenerator, 'compare_number')
    def test_execute_should_generate_number_when_it_doesnt_exist(self,
                                                                 compare_mock,
                                                                 generate_mock):
        GuessCommand(self.receiver).execute(74)

        generate_mock.assert_called_once()

    @mock.patch.object(NumberGenerator, 'generate_number')
    @mock.patch.object(NumberGenerator, 'compare_number')
    def test_execute_should_compare_number_when_it_exists(self,
                                                          compare_mock,
                                                          generate_mock):
        GuessCommand(self.receiver).execute(74)

        compare_mock.assert_called_once()


class TestIsGameOverCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.receiver = NumberGenerator()

    def test_execute_should_return_False_when_is_not_game_over(self):
        result = IsGameOverCommand(self.receiver).execute()

        self.assertFalse(result)

    def test_execute_should_return_True_when_is_game_over(self):
        self.receiver.is_game_over = True

        result = IsGameOverCommand(self.receiver).execute()

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
