from random import randint
from time import sleep

class hangman:
    def __init__(self):
        self._word = ""
        self.display = []
        self.wrong = 0
        self.guessed = []
        self.result = ""
        self.graphics =[
        '''
        +--------+
        |        |
        |
        |
        |
        |
        +============
        ''','''
        +--------+
        |        |
        |        o
        |       
        |          
        |
        +============
        ''','''
        +--------+
        |        |
        |        o
        |       /
        |         
        |
        =============
        ''','''
        +--------+
        |        |
        |        o
        |       /|
        |         
        |
        +============
        ''','''
        +--------+
        |        |
        |        o
        |       /|\\
        |          
        |
        +============
        ''','''
        +--------+
        |        |
        |        o
        |       /|\\
        |       /    
        |
        +============
        ''','''
        +--------+
        |        |
        |        o
        |       /|\\
        |       / \   
        |
        +============
        '''
        ]

    def __repr__(self):
        return "A fun word-guessing game called Hangman!"

    def pick_word(self):
        with open("words.txt") as file:
        # https://github.com/sapbmw/The-Oxford-3000 is source of words.txt
            characters = len(file.read())
            file.seek(randint(1,characters))
            file.readline()
            word = file.readline()
        self._word = (word.split()[0]).lower()

    def hide_word(self):  
        for x in self._word:
            if x.isalpha():
                self.display += "_"
            else:
                self.display += x

    def display_word(self):
        print("Hangman Game")
        print(self.graphics[self.wrong])
        print(f"Your word is: \n{''.join(self.display)}\n")
        print(f"Guessed Letters: {','.join(self.guessed)}")

    def guess(self):
        while True:
            guess = (input("What letter would you like to pick? ")).strip()
            if len(guess)> 1:
                print(f"Please only enter one letter!")
            elif guess.isalpha() == False:
                print(f"Please enter a valid alphabetical letter!")
            elif guess in self.guessed or guess in ''.join(self.display):
                print(f"You guessed this letter already!")
            else:
                break    
        if guess not in self._word:
            self.wrong += 1
            self.guessed += guess
            print(f"Sorry, the word does not contain {guess}.")
        else:
            for x in range(len(self._word)):
                if self._word[x] == guess:
                    self.display[x] = guess
            print(f"Nice, the word contains the letter {guess}!")
        
    def play(self):
        self.pick_word()
        self.hide_word()
        while self.wrong != 6 and self._word != ''.join(self.display):
            self.display_word()
            self.guess()
            sleep(1)
        print(self.graphics[self.wrong])
        print(f"The word is: {self._word}")
        if self.wrong == 6:
            print("YOU LOSE! HANGMAN!")
            self.result = "lose"
        else:
            print("CONGRATULATIONS, YOU WIN!")
            self.result = "won"
        self.display = []

#For Two Player Game - No Word Input From AI
    def player1_word(self):
        while True:
            self._word = input("User1, what word would you like to input (one word only)? No looking User2! ")
            if self._word.isalpha() == False:
                print("Please only use alphabetical letters in the word!")
            else:
                print("Your turn to guess User2!")
                break
        self._word = (self._word.split()[0]).lower()
        print(self._word)

    def player2_word(self):
        while True:
            self._word = input("User2, what word would you like to input (one word only)? No looking User1! ")
            if self._word.isalpha() == False:
                print("Please only use alphabetical letters in the word!")
            else:
                print("Your turn to guess User1!")
                break
        self._word = (self._word.split()[0]).lower()
        print(self._word)

    def two_play(self):
        self.hide_word()
        while self.wrong != 6 and self._word != ''.join(self.display):
            self.display_word()
            self.guess()
            sleep(1)
        print(self.graphics[self.wrong])
        print(f"The word is: {self._word}")
        if self.wrong == 6:
            print("YOU LOSE! HANGMAN!")
            self.result = "lose"
        else:
            print("CONGRATULATIONS, YOU WIN!")
            self.result = "won"
        self.display = []


class User:
    active_users = 0
    active_user_stats = []

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users!"

    def __init__(self, first_name, last_name, user):
        self.first = first_name.lower()
        self.last = last_name.lower()
        self.user = user.lower()
        self.games = 0
        self.won = 0
        self.lost = 0
        User.active_users += 1
        User.active_user_stats.append(self)

    def __repr__(self):
        return f"<User: {self.user},  Games Played: {self.games},  Games Won {self.won},  Games Lost:{self.lost}>"

#For One Player Game - AI Word input
    def play_hangman(self):
        while True:
            game = hangman()
            game.play()
            if game.result == "won":
                self.won += 1
            else:
                self.lost+= 1
            self.games += 1
            repeat = (input("Would you like to play again? Yes or No ")).lower()
            if "n" in repeat:
                print("Thanks for playing, bye!")
                break

#For Two Player Game - No Word Input From AI
    def two_player_hangman(self):
        giver = input("Who would like to give the first word for the other to guess? User1 or User2 ")
        while True:
            game = hangman()
            if "1" in giver:
                game.player1_word()
                giver = "2"
                game.two_play()
                if game.result == "won":
                    self.lost += 1
                else:
                    self.won+= 1
            else:
                game.player2_word()
                giver = "1"
                game.two_play()
                if game.result == "won":
                    self.won += 1
                else:
                    self.lost+= 1
            self.games += 1
            repeat = (input("Would you like to play again? Yes or No ")).lower()
            if "n" in repeat:
                print("Thanks for playing, bye!")
                break

#For One Player Game - AI Word input
def main1():
    first = input("First Name: ")
    last = input("Last Name: ")
    user = input("Username: ")
    user1 = User(first,last,user)
    user1.play_hangman()
    user2 = User("karen","jin","kjin")
    user2.games = 1000
    user2.won = 1000
    print(user1)
    print(User.display_active_users())
    print(User.active_user_stats)

#For Two Player Game - No Word Input From AI
def main2():
    print("User1")
    first1 = input("First Name: ")
    last1 = input("Last Name: ")
    username1 = input("Username: ")
    print("User2")
    first2 = input("First Name: ")
    last2 = input("Last Name: ")
    username2 = input("Username: ")
    user1 = User(first1,last1,username1)
    user2 = User(first2,last2,username2)
    print(f"User1: {user1.user}")
    print(f"User2: {user2.user}")    
    user1.two_player_hangman()
    user2.won = user1.lost
    user2.lost = user1.won
    user2.games = user1.games
    print(User.active_user_stats)

def start():
    while True:
        num_of_players = input("One or Two Players? ")
        if num_of_players[0] == "1" or num_of_players.lower()[0] == "o":
            main1()
            break
        elif num_of_players[0] == "2" or num_of_players.lower()[0] == "t":
            main2()
            break
        print("Please enter a valid choice (one/two)")

start()