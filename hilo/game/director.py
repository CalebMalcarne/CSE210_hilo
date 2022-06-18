# Code by Rebecca Roeth, CSE 210
from game.card import Card
# import random

class Director:
    '''
    Attributes:
        card (List[Card]): a list of card instances
        is_playing (boolean): Wheather or not the game is being played still
            If player reaches 0, game automatially over
            If player chooses to end game, game ends
        score(int): The score for one round of play.
            Starts at 300
        total_score (int): The score for the entire game.
            +100 if they guess correctly
            -75 if they guess incorrectly
    '''
    def __init__(self):
        '''Constructs a new Director
        
        Args:
            self (Director): an instance of Director
        '''
        self.current_card = -1
        self.total_score = 300
        self.card = Card()
    
    def start_game(self):
        """
        Starts the game by running the main game loop which repeats until 
        player does not want to continue or loses.

        Args:
            self (Director): an instance of director
        """
        # The game starts without asking if you want to play, unlike the dice
        is_playing = True
        while is_playing:
            self.do_current_card()
            h_l = self.get_inputs() # High/Low choice
            self.do_outputs(h_l)
            is_playing = self.still_playing()

    def do_current_card(self):
        """Updates the player's score.
        
        Args:
            self(Director): An instance of Director
        """
        if self.current_card < 0:
            self.current_card = self.get_next_card()
    
        print(f"\nThe card is: {self.current_card}")

    def get_next_card(self):
        """ Calls Card class to get the next card

        Args:
            self(Director): An instance of Director
        """
        return self.card.draw()
    
    def get_inputs(self):
        '''Ask the user Higher or lower? and gets answer, checks input is good

        Args:
            self (director): An instance of Director
        '''
        inp = input("Higher or lower? [h/l] ")

        while inp != 'h' or inp != 'l':
            print(f"\nUnexpected input: {inp}\n")
            inp = input("Higher or lower? [h/l] ")
        
        return inp

    def do_outputs(self, h_l):
        """Displays the card and the score. Also asks the player if they want to play again
        
        Args:
            self(Director): An instance of Director.
            h_l: High or low in h or l characters.
        """
        next_card = self.get_next_card()
        print(f"Next card was: {next_card}")

        # Scoring
        if (h_l == 'h' and next_card > self.current_card) or (h_l == 'l' and next_card < self.current_card):
            self.total_score += 100
        else:
            self.total_score -= 75

        self.current_card = next_card

        print(f"Your score is: {self.total_score}")

    def still_playing(self):
        '''Ask the user if they want to keep playing
            
            Args:
            self (director): An instance of Director
        '''
        if self.total_score > 0:
            playing = input("Play again? [y/n] ")
            return (playing == "y")
        else:
            print("You lose, goodbye.")
            return False