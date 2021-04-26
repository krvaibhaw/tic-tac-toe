# Tic Tac Toe ✨

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)
![forthebadge](https://forthebadge.com/images/badges/for-you.svg)
![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)

![](https://img.shields.io/badge/Excitement-High-red)
![](https://img.shields.io/badge/Maintained-Yes-blue)
![](https://img.shields.io/badge/Pull_Requests-Accepting-yellow)
![](https://img.shields.io/github/issues/krvaibhaw/tic-tac-toe)

![](https://img.shields.io/badge/Python-blue)
![](https://img.shields.io/badge/HTML-blueviolet)

## Running Tic-Tac-Toe:

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed.
2. Install [Flask Web Framework](https://flask.palletsprojects.com/en/2.0.x/).
3. Install requirements  
```
    $ pip install requirements.txt
``` 
4. Running the program:
```
	$ git clone https://github.com/krvaibhaw/tic-tac-toe.git
	$ cd tic-tac-toe
	$ python runner.py
```

<p align="center">
<img src="/preview/preview.gif">
</p>


## Introduction

To solve games using AI, we will introduce the concept of a game tree followed by minimax algorithm. The different states of the game are represented by nodes in the game tree, very similar to the above planning problems. The idea is just slightly different. In the game tree, the nodes are arranged in levels that correspond to each player's turns in the game so that the “root” node of the tree (usually depicted at the top of the diagram) is the beginning position in the game. In tic-tac-toe, this would be the empty grid with no Xs or Os played yet. Under root, on the second level, there are the possible states that can result from the first player’s moves, be it X or O. We call these nodes the “children” of the root node.

Each node on the second level, would further have as its children nodes the states that can be reached from it by the opposing player's moves. This is continued, level by level, until reaching states where the game is over. In tic-tac-toe, this means that either one of the players gets a line of three and wins, or the board is full and the game ends in a tie.


## What is Minimax?

Minimax is a artificial intelligence applied in two player games, such as tic-tac-toe, checkers, chess and go. This games are known as zero-sum games, because in a mathematical representation: one player wins (+1) and other player loses (-1) or both of anyone not to win (0).

## How does it works?

The algorithm search, recursively, the best move that leads the *Max* player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating *min* and *max*) until it finds a terminal state (win, draw or lose).

## Understanding the Algorithm

The algorithm was studied by the book Algorithms in a Nutshell (George Heineman; Gary Pollice; Stanley Selkow, 2009). Pseudocode (adapted):

```
minimax(state, depth, player)

	if (player = max) then
		best = [null, -infinity]
	else
		best = [null, +infinity]

	if (depth = 0 or gameover) then
		score = evaluate this state for player
		return [null, score]

	for each valid move m for player in state s do
		execute move m on s
		[move, score] = minimax(s, depth - 1, -player)
		undo move m on s

		if (player = max) then
			if score > best.score then best = [move, score]
		else
			if score < best.score then best = [move, score]

	return best
end
```
Where,

* **state**: the current board in tic-tac-toe (node)
* **depth**: index of the node in the game tree
* **player**: may be a *MAX* player or *MIN* player



<br><br>
Feel free to follow along the code provided along with mentioned comments for 
<br>better understanding of the project, if any issues feel free to reach me out.
<br><br>

## Contributing

Contributions are welcome!
<br>Please feel free to submit a Pull Request.