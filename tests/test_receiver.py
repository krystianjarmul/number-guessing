import unittest
from unittest import mock

from controller.receiver import NumberGenerator


class TestNumberGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = NumberGenerator()

    @mock.patch("controller.receiver.random.randint", return_value=74)
    def test_generate_number_should_draw_number(self, random_mock):
        self.generator.generate_number()

        self.assertEqual(self.generator.number, 74)

    @mock.patch.object(NumberGenerator, "bigger_hint")
    def test_compare_number_should_call_bigger_hint_when_passed_number_is_bigger(
            self, hint_mock):
        self.generator.number = 74

        self.generator.compare_number(88)

        hint_mock.assert_called_once()

    @mock.patch.object(NumberGenerator, "smaller_hint")
    def test_compare_number_should_call_smaller_hint_when_passed_number_is_smaller(
            self, hint_mock):
        self.generator.number = 74

        self.generator.compare_number(44)

        hint_mock.assert_called_once()

    @mock.patch.object(NumberGenerator, "win_hint")
    def test_compare_number_should_call_win_hint_when_numbers_are_equal(self,
                                                                        hint_mock):
        self.generator.number = 74

        self.generator.compare_number(74)

        hint_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
