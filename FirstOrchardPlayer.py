# This program runs the file FirstOrchardTextless.py
#
# It simulates plays of the board game "First Orchard"
# (HABA Games, 2009), and produces game data as a list
# of tuples in the format (game_outcome, game_length).
# game_outcome will either be 0 for a loss or 1 for a 
# win, and game_length shows the number of turns the
# the game took to complete.
#
# To modify the number of games simulated, simply change
# the variable num_games on line 19.


from FirstOrchardTextless import firstorchard
import csv
import matplotlib.pyplot as plt
from collections import Counter

num_games = 100000

data = [("Outcome", "Game Length")]
for i in range(num_games):
    data.append(firstorchard())

with open("FirstOrchardData.csv", "w") as f:
    csv_writer = csv.writer(f)
    for t in data:
        csv_writer.writerow(t)

outcomes = []
wins = 0
losses = 0
for i in data[1:]:
    outcomes.append(i)
for i in outcomes:
    if i[0] == 0:
        losses += 1
    elif i[0] == 1:
        wins += 1
game_lengths = []
for i in data[1:]:
    game_lengths.append(i[1])
length_data = Counter(game_lengths).items()
length = Counter(game_lengths).keys()
frequency = Counter(game_lengths).values()


fig, (axs1, axs2) = plt.subplots(1, 2, figsize = (16,8), gridspec_kw = {"width_ratios": [5, 1]})
axs1.hist2d(length, frequency, bins = 100, cmap=plt.cm.Greys)
axs2.bar(["Loss", "Win"], [losses, wins], color = ["firebrick", "forestgreen"])
axs1.set_xlabel("Game Length in Turns")
axs1.set_ylabel("Frequency")
fig.suptitle("Outcomes of " + str(num_games) + " \"First Orchard\" Games")
axs1.set_title("Game Lengths")
axs2.set_title("Results")
plt.show()
