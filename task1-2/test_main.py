from models import Stack
from main import check_bracket_balance


def test_function (function,expected,*args):
    result = function(*args)
    try:
        assert result == expected 
        print(f"Тест функции {function.__name__} с аргументами {args} пройден успешно")
    except AssertionError as e:
        print(f"Тест функции {function.__name__} с аргументами {args} провален")

bracket_balance = ['(((([{}]))))', '[([])((([[[]]])))]{()}','{{[()]}}']
bracket_unbalance = ['}{}','{{[(])]}}', '[[{())}]'] 
for arg in bracket_balance:
    test_function(check_bracket_balance,'Сбалансировано', arg)
for arg_1 in bracket_unbalance:
    test_function(check_bracket_balance,'Несбалансировано', arg_1)
test_function(check_bracket_balance,'Неправильный символ: 7', '((([[[]]])7))')
