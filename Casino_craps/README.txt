This is a simple text-based game of craps.
You will need to instal pytest to do the testing as it was one of the methods i used to test this game

Installation of pytest
If python3 doesnt work you can try py .
Step One :
Go into the terminal or Powershell 
Step Two :
python3 -m pip install pip --upgrade
Step Three :
python3 -m pip install pytest
Step Four :
python3 -m pip install pytest-pythonpath
Step Five :|
python3 -m pip install pytest-cov
Step Six :
python3 -m pytest

How to Play:
You begin with a bankroll of $1,000,000 .
The minimum bet amount is $5.

Come Out Roll Bet:
You roll two dice to determine the initial outcome.
Natural Win (7 or 11): You win double your bet!
Craps (2, 3, or 12): You lose your bet.
Point Established (anything else): The sum of the rolled dice becomes the "point" for subsequent rolls.

Pass Line Bet :
You can choose to place a bet on the "pass line."
You win if you roll the established point before rolling a 7.
You lose if you roll a 7 before rolling the point.

Subsequent Rolls:
After the come-out roll, you'll keep rolling the dice until you win, lose, or run out of money.
Winning/losing conditions depend on whether you placed a pass line bet and the outcome of each roll.

It also includes bets like the Dont Come, Feild, Hardway, and Big 6 or 8 .
Each bet has its own winning/losing conditions, and you can choose to place them at different points in the game.

After each round, you'll be asked if you want to play again.
The game continues until you decide to stop or lose all your money.
