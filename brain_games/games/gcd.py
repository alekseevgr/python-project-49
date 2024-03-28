import random
from .start import start_game

rules = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def generate_round():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def run_gcd_game():
    return start_game(generate_round, rules)
