import random

def roll_dice():
  dice = (random.randint(1,6), random.randint(1,6))
  return dice

def place_bet(money, min_bet, bet_type):
  while True:
    try:
      bet_amount = int(input(f"Enter bet amount for {bet_type} (min {min_bet}): "))
      if bet_amount >= min_bet and bet_amount <= money:
        money -= bet_amount
        return bet_amount, money
      else:
        print("Invalid bet amount. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def craps():
  money = 1000000
  min_bet = 5

  while money > 0:
    print(f"\nCurrent bankroll: ${money}")

    # Come Out Bet
    come_out_roll = roll_dice()
    come_out_sum = sum(come_out_roll)
    print(f"Come out roll: {come_out_roll} ({come_out_sum})")

    # Come Out Bet
    if come_out_sum in (7, 11):
      print("Natural - You win!")
      money += min_bet * 2
    elif come_out_sum in (2, 3, 12):
      print("Craps - You lose!")
    else:
      point = come_out_sum
      print(f"Point established: {point}")

      # Pass Line Bet
      pass_line_bet, money = place_bet(money, min_bet, "Pass Line")

      # Passline Bet 
      while True:
        roll = roll_dice()
        roll_sum = sum(roll)
        print(f"Roll: {roll} ({roll_sum})")

        if roll_sum == point:
          print("Pass Line - You win!")
          money += pass_line_bet * 2
          break
        elif roll_sum == 7:
          print("Seven Out - You lose!")
          break

    # Do you want to play again
    if money > 0:
      play_again = input("Play again? (y/n): ").lower()
      if play_again != 'y':
        break
    
    while money > 0:
      print(f"\nCurrent bankroll: ${money}")
      
    
    # Dont Come Bet Roll
    dont_comebet = roll_dice()
    dont_comebet_sum = sum(dont_comebet)
    print(f"Come out roll: {dont_comebet} ({dont_comebet_sum})")

    # Dont Comeback Bet
    if dont_comebet_sum in (7, 11):
      print("Dont Come Bet - You Lose!")
      money += min_bet * 2
    elif dont_comebet_sum in (2, 3, 12):
      print("Dont Come Bet  - You Win!")
    else:
      point = dont_comebet_sum
      print(f"Point established: {point}")

      # Dont Passline  Bet
      dont_passline, money = place_bet(money, min_bet, "Pass Line")

      # Dont Passline 
      while True:
        roll = roll_dice()
        roll_sum = sum(roll)
        print(f"Roll: {roll} ({roll_sum})")

        if roll_sum == point:
          print("Pass Line - You Lose!")
          money += dont_passline * 2
          break
        elif roll_sum == 12 :
          print("Dont Pass Bet")
          break
        elif roll_sum == 7:
          print("Seven Out - You Win!")
          break

    # Do you want to play again
    if money > 0:
      play_again = input("Play again? (y/n): ").lower()
      if play_again != 'y':
        break
      
 

  print(f"\nFinal amount: ${money}")

  while money > 0:
    print(f"\nCurrent amount: ${money}")

    # Feild Bet  Roll
    feild_bet = roll_dice()
    feild_bet_sum = sum(feild_bet)
    print(f"Come out roll: {feild_bet} ({feild_bet_sum})")

    # Feild Bet 
    if feild_bet_sum in (2, 3, 4, 9, 10, 11, 12):
      print("Feild Bet - You win!")
      money += min_bet * 2
    elif feild_bet_sum in (1, 5, 6 , 7 , 8):
      print("Feild Bet - You lose!")
    else:
      point = feild_bet_sum
      print(f"Point established: {point}")

      # Feild  Bet
      feild_bet, money = place_bet(money, min_bet, "Feild Bet")

      # Subsequent Rolls
      while True:
        roll = roll_dice()
        roll_sum = sum(roll)
        print(f"Roll: {roll} ({roll_sum})")

        if roll_sum == point:
          print("Pass Line - You win!")
          money += pass_line_bet * 2
          break
        elif roll_sum == 7:
          print("Seven Out - You lose!")
          break

    # Check bankroll and ask to continue
    if money > 0:
      play_again = input("Play again? (y/n): ").lower()
      if play_again != 'y':
        break

  while money > 0:
    print(f"\nCurrent amount: ${money}")

    # Hardway Bet 
    hardway_bet = roll_dice()
    hardway_bet_sum = sum(hardway_bet)
    print(f"Come out roll: {hardway_bet} ({hardway_bet_sum})")

    # Hardway Bet 
    if hardway_bet_sum == 4 or hardway_bet_sum == 10 :
      print("Hardway Bet - You win!")
      money += min_bet * 7
    else:
      money += min_bet * 9
      print(f"Point established: {point}")

      # Big 
      big, money = place_bet(money, min_bet, "Pass Line")

      # Big 6 or 8 
      while True:
        roll = roll_dice()
        roll_sum = sum(roll)
        print(f"Roll: {roll},({roll_sum})")

        if roll_sum == 6 or roll_sum == 8:
          print("Big 6 or 8  - You win!")
          money += big * 1
          break
        else :
          print("Big 6 or 8  - You lose!")
          break

    # Do you want to continue
    if money > 0:
      play_again = input("Play again? (y/n): ").lower()
      if play_again != 'y':
        break


if __name__ == "__main__":
  craps()
