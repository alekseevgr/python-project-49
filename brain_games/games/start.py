import prompt

rounds_count = 3


def start_game(generate_round, rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')
    print(rules)

    for i in range(rounds_count):
        question, correct_answer = generate_round()
        print(f'Question: {question}')

        answer = input('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
