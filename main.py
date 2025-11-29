import random
import time
running = True

if open('names.txt', 'r').read() == '':
    name = input('Enter your name: ')
    with open('names.txt', 'a') as f:
        f.write(name + '\n')
if open('names.txt', 'r').read() != '':
    with open('names.txt', 'r') as f:
        names = f.readlines()
        name = names[-1].strip()
    print(f'Welcome, {name} to Times Tables Tutoring!')
print('1. Start Practice')
print('2. View instructions')
print('3. View Previous Scores')
print('4. Exit')
while running:
    try:
        start_choice = int(input('Please enter your choice (1-4): '))
        if start_choice == 1:
            difficulty = (input('Select difficulty Easy, Medium, or Hard: '))
            difficulty_selection = True
            while difficulty_selection:
                if difficulty.lower() == 'easy':
                    max_num = 5
                    difficulty_selection = False
                elif difficulty.lower() == 'medium':
                    max_num = 10
                    difficulty_selection = False
                elif difficulty.lower() == 'hard':
                    max_num = 12
                    difficulty_selection = False
                else:
                    print('Invalid difficulty level. Please choose Easy, Medium, or Hard.')
                    difficulty = (input('Select difficulty Easy, Medium, or Hard: '))
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
            save_option_running = True
            while save_option_running:
                save_option = input('Would you like to save your score? (yes/no): ')
                if save_option.lower() == 'yes':
                    with open('scores.txt', 'a') as f:
                        f.write(f'Difficulty: {difficulty}, Score: {score} out of {qcount}\n')
                    print('Score saved successfully.')
                    time.sleep(2)
                    save_option_running = False
                    retype = True
                elif save_option.lower() == 'no':
                    print('Score not saved.')
                    time.sleep(2)
                    save_option_running = False
                    retype = True
                else:
                    print('Invalid input. Please enter yes or no.')
        elif start_choice == 2:
            print('Instructions:')
            print('1. Choose a difficulty level: Easy, Medium, or Hard.')
            print('2. You will be asked a series of multiplication questions based on the chosen difficulty.')
            print('3. You have 60 seconds to answer as many questions as possible.')
            print('4. Your score will be displayed at the end of the practice session.')
            time.sleep(5)
            retype = True
        elif start_choice == 3:
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
            retype = True
        elif start_choice == 4:
            print(f'Exiting the program. Goodbye {name}!')
            retype = False
            running = False
        if retype:
            print('Welcome to Times Tables Tutoring!')
            print('1. Start Practice')
            print('2. View instructions')
            print('3. View Previous Scores')
            print('4. Exit')
            retype = False
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 4.')
        