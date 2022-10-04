# Rock, Paper, Scissors

def rock_paper_scissors():

    run = True

    while run == True:

        p1_move = int(input("Player One: Enter '1' for 'rock', '2' for 'paper', or '3' for scissors."))
        if p1_move not in {1: 'rock', 2: 'paper', 3: 'scissors'}:
            print("Player Two: Please enter a valid option: '1' for 'rock', '2' for 'paper', or '3' for scissors.")
        
        p2_move = int(input("Player Two: Enter '1' for 'rock', '2' for 'paper', or '3' for scissors."))
        if p2_move not in {1: 'rock', 2: 'paper', 3: 'scissors'}:
            print("Player Two: Please enter a valid option: '1' for 'rock', '2' for 'paper', or '3' for scissors.")
        
        if p1_move != p2_move:
            moves = {}
            moves[p1_move] = 'player one'
            moves[p2_move] = 'player two'
            if p1_move == 1:
                if p2_move == 3:
                    winner = 'p1'
                else:
                    winner = 'p2'

            elif p1_move == 2:
                if p2_move == 1:
                    winner = 'p1'
                else:
                    winner = 'p2'

            else:
                if p2_move == 1:
                    winner = 'p2'
                else:
                    winner = 'p1'

            print(f'The winner is {winner}!')

        else:
            print('Tie game!')

        keep_playing = input('Enter \'q\' to quit, or enter anything else to play another around.')
        if keep_playing == 'q':
            run = False
            print('Thanks for playing!')
            break

rock_paper_scissors()