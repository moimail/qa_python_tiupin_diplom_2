import allure
import pytest

from helpers.helpers_on_create_user import HelpersOnCreateUser as u
from tests.test_create_order import TestCreateOrder
from helpers.helpers_on_check_response import HelpersOnCheck as c
from helpers.helpers_on_get_ingredients import HelpersOnGetIngredients as g

@pytest.fixture
@allure.title('Создаем пользователя и инициализируем данные для удаления после завершения работы')
def setup_user():
    # генерируем данные нового пользователя: email, password, user_name
    user_data = u.generate_random_user_data()
    # отправляем запрос на создание пользователя
    auth_token, refresh_token = u.create_user(user_data)
    # сохраняем полученные данные пользователя
    yield user_data, auth_token

    # Удаляем созданного пользователя
    u.try_to_delete_user(auth_token)

@pytest.fixture(scope='class')
@allure.title('Инициализируем списки ингредиентов')
def setup_ingredients():
    ingredients = g.get_ingredients()
    TestCreateOrder.buns_list = g.get_buns_list(ingredients)
    TestCreateOrder.fillings_list = g.get_fillings_list(ingredients)
    TestCreateOrder.sauces_list = g.get_sauces_list(ingredients)
    c.check_ingredients(TestCreateOrder.buns_list, TestCreateOrder.fillings_list, TestCreateOrder.sauces_list)


