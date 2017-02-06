#!/usr/bin/env python2
# encoding: UTF-8

"""A number guessing game"""

import math
import random

__author__ = "Léon Spaans"
__date__ = "2017-02-04"
__version__ = "0.1.0"


class NumberGuessing(object):
    """
    A number guessing game.
    """
    def __init__(self, max_number=100, max_turns=7):
        """
        The constructor method.

        Arguments:
            max_number - int(): maximum random number
            max_turns  - int(): maximum of turns
        """
        self._guessed = None
        self._max_number = max_number
        self._max_turns = max_turns
        self._name = ""
        self._turn = None
        self._number = None
        self._won = None

        self._init_game()

    def _init_game(self):
        """
        Initializes new game.
        """
        self._guessed = set([])
        self._turn = 0
        self._won = False

        self._init_name()
        self._init_max_number()
        self._init_max_turns()

        self._number = int(self._max_number * random.random())

    def _init_max_number(self):
        """
        Initializes the maximum number.
        """
        input_max_number = ""

        while not input_max_number.isdigit():
            input_max_number = raw_input(
                (
                    "What is the upper boundary [default={max_number}]? "
                ).format(
                    max_number=self._max_number
                )
            )

            if input_max_number == "":
                input_max_number = str(self._max_number)

        self._max_number = int(input_max_number)
        self._max_turns = int(math.log(self._max_number, 10) * 3.5)

    def _init_max_turns(self):
        """
        Initializes the maximum number of turns.
        """
        input_max_turns = ""

        while not input_max_turns.isdigit():
            input_max_turns = raw_input(
                (
                    "How many guesses would you like [default={max_turns}]? "
                ).format(
                    max_turns=self._max_turns
                )
            )

            if input_max_turns == "":
                input_max_turns = str(self._max_turns)

        self._max_turns = int(input_max_turns)

    def _init_name(self):
        """
        Initializes the player name.
        """
        while self._name == "":
            self._name = raw_input("What's your name? ")

    def _main_loop(self):
        """
        The main game loop.
        """
        while self._turn < self._max_turns:
            guess = raw_input("Choose a number: ")

            try:
                guess = int(guess)
            except ValueError:
                continue

            if guess in self._guessed:
                print "You have already guessed that number!"
                continue

            self._turn += 1
            self._guessed.add(guess)

            if guess == self._number:
                self._won = True
                break
            elif guess < self._number:
                print "You need to guess higher!"
            else:
                print "You need to guess lower!"

        if self._won is True:
            print (
                "Congratulations {name}!! The number was in fact " +
                "{number}. You have guessed it in {turn} turns. " +
                "Well done!"
            ).format(
                name=self._name,
                number=self._number,
                turn=self._turn
            )
        else:
            print (
                "Too bad {name}, you were not able to guess it in " +
                "{max_turns} turns. The number was {number}."
            ).format(
                name=self._name,
                max_turns=self._max_turns,
                number=self._number
            )

        print "The end!"

    def start(self):
        """
        Starts the game.
        """
        print "Hi {name}, we are going to play Guess the Number!".format(
            name=self._name
        )

        self._main_loop()

    @property
    def won(self):
        """
        Returns the "self._won" bool().
        """
        return self._won


def main():
    """
    The main function that is automatically called when the script itself
    is executed.
    """
    try:
        NumberGuessing().start()
    except KeyboardInterrupt:
        print "\nSee you next time!"

if __name__ == "__main__":
    main()
