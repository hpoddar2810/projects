from random import randint

def isboardfull(bo):
  return (bo.count(' ') == 1)

def pos_empty(bo,res):
  return (bo[res] == ' ')

def print_board(bo):
  i = 1
  while i < 8:
    #print("  | | ")
    print(" " ,bo[i], "|", bo[i+1], "|", bo[i+2])
    i += 3

  print("---------------")
  #print("  | | ")

def check(bo,sign):
  return  ( (bo[1] == sign and bo[2] == sign and bo[3] == sign) or
            (bo[4] == sign and bo[5] == sign and bo[6] == sign) or
            (bo[7] == sign and bo[8] == sign and bo[9] == sign) or
            (bo[1] == sign and bo[4] == sign and bo[7] == sign) or
            (bo[2] == sign and bo[5] == sign and bo[8] == sign) or
            (bo[3] == sign and bo[6] == sign and bo[9] == sign) or
            (bo[1] == sign and bo[5] == sign and bo[9] == sign) or
            (bo[3] == sign and bo[5] == sign and bo[7] == sign) )



def main():
  print(__name__)
  print('Welcome to Tic Toe')
  name = input('Enter your name: ')
  cscore = 0
  pscore = 0

  while True:
    board = [' ' for x in range(10)]
    print_board(board)

    while not isboardfull(board):
      #ask to fill
      res = input('Enter the position to fill [1-9]: ')
      #validate the input
      while ((not int(res)) or (int(res) < 1 or int(res) > 10)):
        res = input('!!!!!!Enter an integer position between 1-9: ')

      res = int(res)
      #check for pos if its empty or not
      # if empty fill and if not ask again
      if not pos_empty(board,res):
        print('position' , res, "is not empty." )
        print_board(board)
        continue

      board[res] = 'X'
      print_board(board)

      #chexk wether the person win
      if check(board,'X'):
        print("Congratulation!!!! You Win.")
        pscore += 1
        break

      #computer response
      while not pos_empty(board,res):
        res = randint(1,9)

      print("Computer Filled: ", res)
      board[res] = '0'
      print_board(board)

      #check if computer win
      if check(board,'0'):
        print("Congratulation!!!! You Lose.")
        cscore += 1
        break

    if isboardfull(board):
      print("Congratulation!!!! It's a Tie.")

    print(name, ' score: ', pscore)
    print("Computer score: ", cscore)

    player_wants = input("Want to play again?(Y/N): ")
    if player_wants == 'N':
      if pscore > cscore:
        print("Congratulation!!! you win this session.")

      elif pscore < cscore:
        print("Congratulations!!1 you lose this session.")

      else:
        print("This session is tie.")

      print("Thank You for playing with me.")
      break


if __name__ == "__main__":
    main()
