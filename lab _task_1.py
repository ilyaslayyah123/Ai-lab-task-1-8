import random
# 1 todo list
Todo_list=[]
while True:
    print("1. Add task:")
    print("2. view task: ")
    print("3. Delete task: ")
    print("4. Exit: ")
    choice=int(input("Choose an option: "))
    if choice==1:
        task=input("Enter a task: ")
        Todo_list.append(task)
    elif choice==2:
        print("Taskes: ")
        for i ,task in enumerate(Todo_list,1):
            print(i,task)
    elif choice==3:
        task_number=int(input("Enter task number to delete task: "))
        del Todo_list[task_number-1]
    elif choice==4:
        break
    else:
        print("invalid choice: ")

# 2 hangman game

def hangman():
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    def chose_word():
        word_easy=["apple","banana","cherry","date","elderberry"]
        word_medium=["elephant","giraffe","hippo","iguana","jaguar"]
        word_hard=["kangaroo","lemur","monkey","narwhal","octopus"]
        choice=input("Choose the level of difficulty: easy, medium, hard: ").lower()
        if choice=="easy":
            return random.choice(word_easy).lower(),len(hangman) - 3
        elif choice=="medium":
            return random.choice(word_medium).lower(),len(hangman) - 2
        elif choice=="hard":
            return random.choice(word_hard).lower(),len(hangman) - 1
        else:
            print("Invalid choice")
            return random.choice(word_medium).lower(),len(hangman) - 2
    play_again=True
    while play_again:
        word,attempts=chose_word()
        gussed_word=["_"]* len(word)
        gussed_letters=[] 
        game_over=False
        
        print("Welcome to Hangman!")
        print(f"The word has {len(word)} letters: {' '.join(gussed_word)}")
        print(hangman_stages[0])  
    while not game_over:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue    
        if guess in gussed_letters:
            print("You already guessed that letter.")
            continue 
        gussed_letters.append(guess)
        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i]==guess:
                    gussed_word[i]=guess
        else:
            print("Wrong guess!")
            attempts-=1
            print(f"You have {attempts} attempts left.")
            print(hangman_stages[attempts])
        if "_" not in gussed_word:
            game_over=True
            print(f"Congratulations! You won!{''.join(gussed_word)}")
        elif attempts==0:
            game_over = True
            print(f"Game over! The word was: {word}")
            print(f"{' '.join(gussed_word)}")
            print(f"Guessed letters: {', '.join(gussed_letters)}")
    play_again = input("do you want to play again?(Y/N): ").lower()=="yes"
hangman()