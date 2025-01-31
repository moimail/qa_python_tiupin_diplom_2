## qa-python-diplom-2
### Тест-сьют для проверки API приложения "Stellar Burgers" с помощью Pytest и библиотеки Requests

### Структура проекта

- `tests/` - папка с файлами тестов:
  - `tests/test_create_user.py`     - тесты эндпойнта создания пользователя
  - `tests/test_login_user.py`      - тесты эндпойнта авторизации пользователя
  - `tests/test_update_user.py`     - тесты эндпойнта обновления данных пользователя
  - `tests/test_create_order.py`    - тесты эндпойнта создания заказа
  - `tests/test_get_user_orders.py` - тесты эндпойнта получения заказов пользователя


- `helpers/` - папка вспомогательных функций:
  - `helpers/helpers_on_create_user.py`     - функции для работы с пользователями и заказами
  - `helpers/helpers_on_get_ingredients.py` - функции для получения ингредиентов
  - `helpers/helpers_on_requests.py`        - функции для создания заказа и получения списка заказов
  - `helpers/helpers_on_check_response.py`  - функции для проверки полученного ответа на запрос к API


- `conftest.py` - функции-фикстуры 
- `data.py` - константы, URL-адреса и данные для тестов


- `.gitignore` - файл для проекта в Git/GinHub
- `requirements.txt` - файл с внешними зависимостями
- `README.md` - файл с описанием проекта (этот файл)

- `allure_results/` - папка с отчетами Allure


### Для запуска тестов должны быть установлены пакеты:
- `Pytest`
- `Requests`
- `Allure-pytest`
- `Allure-python-commons`

### Для генерации отчетов необходимо дополнительно установить:
- `пакет Allure`
- `фреймворк JDK`

**Запуск всех тестов выполняется командой:**

>  `$ pytest -v ./tests`

**Запуск тестов с генерацией отчета Allure выполняется командой:**

>  `$ pytest -v ./tests  --alluredir=allure_results`

**Генерация отчета выполняется командой:**

>  `$ allure serve allure_results`

**Генерация файла внешних зависимостей requirements.txt выполняется командой:**

>  `$  pip freeze > requirements.txt`

**Установка зависимостей из файла requirements.txt выполняется командой:**

>  `$ pip install -r requirements.txt`
