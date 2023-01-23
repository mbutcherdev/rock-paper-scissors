# Rock paper scissors game in python
# Console only version for now

class GamePlay:
    def __init__(self):
        self.p1 = None
        self.p1_score = 0
        self.c_score = 0
        self.games = 0
        self.player_choice = None
        self.computer_choice = None

    def score(self):
        print(f"\nGames: {self.games}")
        print("Player score: " + str(self.p1_score))
        print("Computer score: " + str(self.c_score) + "\n")

    def computer_pick(self):
        import random
        self.computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    def compare(self, p1):
        loss_condition = {
            "Rock": {"Scissors"},
            "Paper": {"Rock"},
            "Scissors": {"Paper"}
        }
        self.games += 1
        if p1 == self.computer_choice:
            print('Tie!')
        elif p1 in loss_condition[self.computer_choice]:
            print('You lose!')
            self.c_score += 1
        elif self.computer_choice in loss_condition[p1]:
            print('You win!')
            self.p1_score += 1

    def play(self):
        full_word = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scissors"
        }
        try:
            self.p1 = str(input('Pick rock, paper or scissors (r/p/s): ')).lower()
            if self.p1 in full_word:
                self.player_choice = full_word[self.p1]
                self.computer_pick()
                print('You picked ' + self.player_choice)
                print('Computer picked ' + self.computer_choice)
                self.compare(self.player_choice)
                self.score()
            else:
                print('Whoops! Try entering "r" for rock, "p" for paper or "s" for scissors')
        except ValueError:
            pass


def main():
    game = GamePlay()
    print("Welcome to Rock Paper Scissors!")
    print("First to 3 games!\n")
    while True:
        game.play()
        if game.p1_score == 3:
            print("What a winner! Thanks for playing!")
            break
        elif game.c_score == 3:
            print("Better luck next time!")
            break


if __name__ == '__main__':
    main()
