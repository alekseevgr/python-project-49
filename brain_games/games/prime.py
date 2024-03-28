import random
from .start import start_game

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def generate_round():
    num = random.randint(0, 10)
    question = num
    correct_answer = 'yes' if prime(num) else 'no'
    return question, correct_answer


def run_prime_game():
    return start_game(generate_round, rules)
