class TicTacToe:

    def __init__(self) -> None:
        self.board = [" "] * 9
        self.turn = 0
        self.available_moves = [x for x in range(9)]
        self.player_interface()


    def player_interface(self):

        print()
        print("TIC-TAC-TOE")
        print("------------")

        while True:
            print()
            input_value = input("Press 1 to play against Computer\nPress 2 to play two players\n\nSelect your option (1/2): ")
            if input_value in ('1','2'):
                game_type = int(input_value)
                break  

        print()
        if game_type == 1:
            self.player1 = input("Enter player name: ")
            self.player2 = "Computer"
            self.print_board()
            self.single_player()
        else:
            self.player1 = input("Enter first player name: ")
            self.player2 = input("Enter second player name: ")
            self.print_board()
            self.multi_player()


    def print_board(self):

        print()
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("----------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("----------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()


    def isValid(self, move):

        if move in self.available_moves:
            return True
        return False

    
    def isWinning(self, player):

        if self.board[0] == self.board[1] == self.board[2] == player\
            or self.board[3] == self.board[4] == self.board[5] == player\
               or self.board[6] == self.board[7] == self.board[8] == player\
                   or self.board[0] == self.board[4] == self.board[8] == player\
                       or self.board[0] == self.board[3] == self.board[6] == player\
                           or self.board[1] == self.board[4] == self.board[7] == player\
                               or self.board[2] == self.board[5] == self.board[8] == player\
                                   or self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False


    def isGameOver(self, player):

        result = self.isWinning(player)

        if result:
            if player == 'X':
                print(f"{self.player1} wins!!\n")   
            else:
                print(f"{self.player2} wins!!\n")
            return True

        elif not self.available_moves:
            print("Game Drawn!\n")
            return True

        return False

    
    def turnTracker(self):
        if self.turn % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        return player


    def getMove(self):

        while True:
            input_value = input("Enter a valid move(1-9): ")
            if input_value in (str(x) for x in range(1,10)):
                move = int(input_value) - 1
                if self.isValid(move):
                    return move


    def play(self, move, player):
        
        self.board[move] = player
        self.available_moves.remove(move)
        self.print_board()
       

    def CPUMove(self):
        
        moves = list(self.available_moves)
        best_move, _ = self.findBestMove(moves, 'O', 0)
        self.play(best_move, 'O')


    def findBestMove(self, moves, player, depth):    
        '''
        minimax algorithm to find best move for CPU
        '''

        #CPU move
        if player == 'O':
            best_score = float('-inf')
            best_move = None
                
            for move in moves:
                score = 0
                self.board[move] = player
                if self.isWinning(player):
                    score = 10
                elif len(moves) == 1:
                    score = 0
                else:
                    remaining_moves = list(moves)
                    remaining_moves.remove(move)
                    _, score = self.findBestMove(remaining_moves, 'X', depth + 1)

                if score > best_score:
                    best_score = score
                    best_move = move

                self.board[move] = " "

            return (best_move, best_score - depth)

        #human move
        else:

            best_score = float('inf')
            best_move = None

            for move in moves:
                score = 0
                self.board[move] = player
                if self.isWinning(player):
                    score = -10
                elif len(moves) == 1:
                    score = 0
                else:
                    remaining_moves = list(moves)
                    remaining_moves.remove(move)
                    _, score = self.findBestMove(remaining_moves, 'O', depth + 1)

                if score < best_score:
                    best_score = score
                    best_move = move

                self.board[move] = " "

            return (best_move, best_score + depth)
    

    def single_player(self):

        while True:

            player = self.turnTracker()
   
            if player == 'X':
                
                move = self.getMove()
                self.play(move, player)

            else:
                self.CPUMove()

            self.turn += 1

            if self.isGameOver(player):
                break

        self.start_new_game()
            

    def multi_player(self):

        while True:

            player = self.turnTracker()
            move = self.getMove()
            self.play(move, player)

            self.turn += 1

            if self.isGameOver(player):
                break

        self.start_new_game()


    def start_new_game(self):

        print()
        while True:
            input_value = input("Do you want to play a new game? (Y/N)")
            if input_value.lower() in ('y','n'):
                break

        if input_value.lower() == 'y':
            self.board = [" "] * 9
            self.turn = 0
            self.available_moves = [x for x in range(9)]
            self.player_interface()
        else:
            print("Thanks for playing!\n")

        

game = TicTacToe()
