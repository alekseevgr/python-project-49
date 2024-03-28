import random
from .start import start_game

rules = 'Answer "yes" if the number is even, otherwise answer "no"'


def is_even(num):
    return num % 2 == 0


def generate_round():
    num = random.randint(0, 100)
    correct_answer = 'yes' if is_even(num) else 'no'
    question = num
    return (question, correct_answer)


def run_even_game():
    return start_game(generate_round, rules)
