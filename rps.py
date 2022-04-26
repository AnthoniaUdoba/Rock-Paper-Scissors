#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    moves = ['rock', 'paper', 'scissors']

    # instance initialization
    def __init__(self):
        self.score = 0
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        # learn opponent move
        self.my_move = my_move
        self.their_move = their_move
        pass


# validates the winner
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    def move(self):
        # Select a move at random and return it
        self.moves = random.choice(self.moves)
        return self.moves


class HumanPlayer(Player):

    # Function to choose a move
    def move(self):
        while True:
            pick_move = input("Rock, paper, scissors? > ").lower()
            if pick_move in self.moves:
                return pick_move
            elif pick_move == 'exit':
                exit()


class ReflectPlayer(Player):

    def move(self):
        if self.their_move in self.moves:
            return self.their_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):

    def move(self):
        # choses a different move of the last round
        self.their_move = random.choice(self.moves)
        if self.their_move == "rock".lower():
            return "paper"
        elif self.their_move == "paper".lower():
            return "scissors"
        elif self.their_move == "scissors".lower():
            return "rock"


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Initialization
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}.")
        print(f"Opponent played: {move2}.")

        if (move1 == move2):
            print("*** IT'S A TIE! ***")
        elif beats(move1, move2):
            self.score_p1 += 1
            print("*** PLAYER 1 WINS! ***")
        elif beats(move2, move1):
            self.score_p2 += 1
            print("*** PLAYER 2 WINS! ***")

        print(f"\nPlayer 1 Current Score:{self.score_p1}")
        print(f"Player 2 Current Score:{self.score_p2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # start game
    def rounds(self):
        # input no of rounds
        while True:
            self.numrounds = input("How many rounds do you want want play? > ")
            if self.numrounds.isdigit():
                return self.numrounds
            elif self.numrounds.lower() == 'exit':
                exit()

    # start game
    def play_game(self):
        print(">>>> Game start! <<<<")
        self.rounds()
        print("Rock paper scissors, Go! \n")
        for round in range(int(self.numrounds)):
            print(f"Round {round + 1} --:")
            self.play_round()

        print("Game over!")
        print(f"\nPlayer 1 Final Score:{self.score_p1}")
        print(f"Player 2 Final Score:{self.score_p2}")


if __name__ == '__main__':
    # choose player
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
