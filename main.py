import random
import time
running = True
    

print('Welcome to Times Tables Tutoring!')
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
            
            try:
                while elapsed_time < time_limit:
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
            retype = True
        elif start_choice == 2:
            print('Instructions:')
            print('1. Choose a difficulty level: Easy, Medium, or Hard.')
            print('2. You will be asked a series of multiplication questions based on the chosen difficulty.')
            print('3. You have 60 seconds to answer as many questions as possible.')
            print('4. Your score will be displayed at the end of the practice session.')
            retype = True
        elif start_choice == 4:
            print('Exiting the program. Goodbye!')
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
        