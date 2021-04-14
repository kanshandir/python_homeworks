import allure
from task_calc import calc


def test_calc():
    with allure.step("Проверяем функцию calc"):
        assert calc("239/30") == [7, 1, 29]