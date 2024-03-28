import random
from .start import start_game

rules = 'What number is missing in the progression?'


def generate_progression(num, step, number_count):
    array = []
    j = 1
    progression_element = num
    while j <= number_count:
        array.append(progression_element)
        progression_element += step
        j += 1
    return array


def generate_round():
    num = random.randint(0, 100)
    step = random.randint(1, 5)
    number_count = random.randint(5, 10)
    progression = generate_progression(num, step, number_count)
    hidden_number_index = random.randint(0, number_count)
    progression[hidden_number_index] = '..'
    correct_answer = str(num + hidden_number_index * step)
    question = ' '.join(map(str, progression))
    return question, correct_answer


def run_prog_game():
    return start_game(generate_round, rules)
