import random
import time
import datetime
running = True


def load_or_create_name():
    try:
        with open('names.txt', 'r') as f:
            names = f.readlines()
            if names:
                return names[-1].strip()
            else:
                return None
    except FileNotFoundError:
        return None

def showmenu():
    name = load_or_create_name()
    if not name:
        name = input('Enter your name: ')
        with open('names.txt', 'a') as f:
            f.write(f'{name}\n')
    print()
    print(f'Welcome {name} to Times Tables Tutoring!')
    print('1. Start Practice')
    print('2. View instructions')
    print('3. View Previous Scores')
    print('4. Change Name')
    print('5. Exit')

def select_difficulty():
    difficulty = input('Select difficulty Easy, Medium, or Hard: ')
    while True:
        if difficulty.lower() == 'easy':
            return difficulty, 5
        elif difficulty.lower() == 'medium':
            return difficulty, 10
        elif difficulty.lower() == 'hard':
            return difficulty, 12
        else:
            print('Invalid difficulty level. Please choose Easy, Medium, or Hard.')
            difficulty = input('Select difficulty Easy, Medium, or Hard: ')

def start_practice(max_num):
    qcount = 0   
    score = 0
    start_time = time.time()
    time_limit = 60
    elapsed_time = time.time() - start_time
    
    while elapsed_time < time_limit:
        try:
            elapsed_time = time.time() - start_time
            if elapsed_time < time_limit:
                    print(f'Time remaining: {int(time_limit - elapsed_time)} seconds')
            if elapsed_time >= time_limit:
                print('Time is up!')
                break 
            num1 = random.randint(1, max_num)
            num2 = random.randint(1, max_num)
            answer = int(input(f'What is {num1} x {num2}? '))
                
            if answer == num1 * num2:
                print('Correct!')
                score += 1
                qcount += 1
            else:
                print(f'Incorrect. The correct answer is {num1 * num2}.')
                qcount += 1
                
        except ValueError:
            print('Invalid input. Please enter a number.')
            qcount += 1
    print(f'You scored {score} out of {qcount}.')
    return score, qcount

def save_score(difficulty, score, qcount):
    save_option_running = True
    while save_option_running:
        save_option = input('Would you like to save your score? (yes/no): ')
        if save_option.lower() == 'yes':
            date = datetime.date.today()
            date_string = date.strftime('%d-%m-%Y')
            with open('scores.txt', 'a') as f:
                f.write(f'Difficulty: {difficulty}, Score: {score} out of {qcount} Date: {date_string}\n')
            print('Score saved successfully.')
            time.sleep(2)
            save_option_running = False
        elif save_option.lower() == 'no':
            print('Score not saved.')
            time.sleep(2)
            save_option_running = False
        else:
            print('Invalid input. Please enter yes or no.')

def show_instructions():
    print('Instructions:')
    print('1. Choose a difficulty level: Easy, Medium, or Hard.')
    print('2. You will be asked a series of multiplication questions based on the chosen difficulty.')
    print('3. You have 60 seconds to answer as many questions as possible.')
    print('4. Your score will be displayed at the end of the practice session.')
    time.sleep(5)

def show_previous_scores():
    print('Previous Scores:')
    try:
        with open('scores.txt', 'r') as f:
            scores = f.readlines()
            if scores:
                for line in scores:
                    print(line.strip())
            else:
                print('No previous scores found.')
    except FileNotFoundError:
        print('No previous scores found.')
    time.sleep(5)

def change_name():
    new_name = input('Enter your new name: ')
    with open('names.txt', 'a') as f:
        f.write(f'{new_name}\n')
    print(f'Name changed successfully to {new_name}.')
    time.sleep(2)

def main():
    running = True
    showmenu()
    while running:
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            difficulty, max_num = select_difficulty()
            score, qcount = start_practice(max_num)
            save_score(difficulty, score, qcount)
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            show_previous_scores()
        elif choice == '4':
            change_name()
        elif choice == '5':
            name = load_or_create_name()
            print(f'Exiting the program. Goodbye {name}!')
            running = False
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')
        if running:
            showmenu()

main()
        