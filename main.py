import random
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
            score = 0
            for i in range(5):
                num1 = random.randint(1, 12)
                num2 = random.randint(1, 12)
                answer = int(input(f'What is {num1} x {num2}? '))
                if answer == num1 * num2:
                    print('Correct!')
                    score += 1
                else:
                    print(f'Incorrect. The correct answer is {num1 * num2}.')
            print(f'You scored {score} out of 5.')
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 4.')
        