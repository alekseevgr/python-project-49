import random
from .start import start_game

rules = 'What is the result of the expression?'

expression_symbols = ['+', '-', '*']


def calculate(num1, symbol, num2):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    else:
        return num1 * num2


def generate_round():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    symbol = random.choice(expression_symbols)

    question = f'{num1} {symbol} {num2}'
    correct_answer = str(calculate(num1, symbol, num2))
    return question, correct_answer


def run_calc_game():
    return start_game(generate_round, rules)
