class Data:
    login = 'ninja'
    password = '1234'
    name = 'Ниндзя'
    courier = {'login': 'ninja', 'password': '1234', 'name': 'Ниндзя'}
    wrong_name_courier = {'login': 'ninja', 'password': '1234'}
    wrong_password = {'login': 'ninja', 'password': '123456'}

    Url_main_page = 'https://qa-scooter.praktikum-services.ru/'
    Url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    Url_create_login = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    Url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class OrderDate:
    order_scooter_black = {
        'name': 'Кот',
        'lastName': 'Всапогах',
        'address': 'Красная площадь, 1',
        'metroStation': 'Охотный ряд',
        'phone': '+78005553535',
        'rentTime': '1',
        'deliveryDate': '19-07-2024',
        'comment': 'Мяу-мяу-мяу-мяу?',
        'color': ['BLACK']
    }

    order_scooter_grey = {
        'name': 'Губка',
        'lastName': 'Боб',
        'address': 'Бикини-боттом, 5',
        'metroStation': 'Чертаново',
        'phone': '+79153334855',
        'rentTime': '6',
        'deliveryDate': '20-07-2024',
        'comment': 'Спешу к Патрику на Патрики!',
        'color': ['GREY']
    }

    order_scooter_grey_and_black = {
        'name': 'Ходор',
        'lastName': 'Ходор',
        'address': 'Ходор, 70',
        'metroStation': 'Баррикадная',
        'phone': '+79997774457',
        'rentTime': '',
        'deliveryDate': '21-07-2024',
        'comment': 'Ходор ходор ходор ходор ходор ходор ходор',
        'color': ['BLACK', 'GREY']
    }

    order_scooter_no_color = {
        'name': 'Маршалл',
        'lastName': 'Эриксен',
        'address': 'Краснобогатырская ул., 90',
        'metroStation': 'Баррикадная',
        'phone': '+74952053323',
        'rentTime': '7',
        'deliveryDate': '20-07-2024',
        'comment': 'Жду Лилилапушку',
        'color': []
    }


class TextAnswer:
    create_courier = '{"ok":true}'
    duplicate_courier = 'Этот логин уже используется. Попробуйте другой.'
    not_once_required_field = 'Недостаточно данных для создания учетной записи'
    not_login_courier = 'Недостаточно данных для входа'
    not_password_courier = 'Недостаточно данных для входа'
    no_such_username_and_password = 'Учетная запись не найдена'
