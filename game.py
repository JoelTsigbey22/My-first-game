# Created by Joel Tsigbey - Ghana - Oct 2026
import random

print("=== JOEL'S ROCK PAPER SCISSORS ===")
print("First to 3 wins!")

your_score = 0
computer_score = 0

while True:
    print(f"\nScore - You: {your_score} | Computer: {computer_score}")
    you = input("Choose rock, paper, or scissors (or quit): ").lower()
    if you == "quit":
        print("Thanks for playing!")
        break
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if you == computer:
        print("Draw!")
    elif (you == "rock" and computer == "scissors") or (you == "paper" and computer == "rock") or (you == "scissors" and computer == "paper"):
        print("YOU WIN this round!")
        your_score = your_score + 1
    elif you in choices:
        print("Computer wins this round!")
        computer_score = computer_score + 1
    else:
        print("Wrong word! Type rock, paper, or scissors")
        continue
    if your_score == 3:
        print("\nYOU ARE THE CHAMPION!!!")
        break
    if computer_score == 3:
        print("\nComputer won, try again!")
        break
