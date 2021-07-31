# GGames

## About The Project
GGames, short for Graph Games, is a Python package that provides functions to 
study games on static or time-varying graphs. The project was first created to 
help students answer questions about the [cop-number](#cops-and-robbers-game)
of [edge-periodic graph](#time-varying-graphs).

## Preliminary
The user must have minimum knowledge of [graph theory](#bondy-murty) and 
[time-varying graph](#casteigts) to enjoy this package. Depending on the field
of study of the user, he/she should be familiar with the
[Cops and Robbers game](#bonato-nowakowski) and the
[reachability game](#berwanger). More references are available at the end of 
this document.

### Cops and Robbers game
The Cops and Robbers game was first introduced independently by
[Quilliot](#quilliot), and by [Nowakowski and Winkler](#nowakowski-winkler).
This game is played by *k* cops and a robber who place themselves on vertices of
a graph and take turns moving along an edge. Cops play first. They win if at any 
moment a cop occupies the same vertex as the robber. If the
robber can avoid capture forever, he wins. A good survey on the subject
has been written by [Bonato and Nowakowski](#bonato-nowakowski).

There exist a lot of different variants of this game. One involves playing
on time-varying graphs: more specifically, on discrete ones. This
variant was first introduced by [Erlebach and Spooner](#erlebach-spooner).
Because of its recency, a lot of questions about it have yet to be answered.

### Reachability game
The reachability game is played by two players, Player 0 and Player 1, on a
graph. The set of vertices is partitioned into two sets, *S0* and *S1*. A
token is placed on a vertex of the graph. When the token is on a vertex of
*S0*, Player 0 moves the token to an adjacent vertex. Player 1 does the same if
the token is on a vertex of *S1*.  There is also a subset of *S1*, *F*. 
Player 0 wins if the token occupies a vertex of *F*, and Player 1 wins 
if he can avoid that forever. Because many important problems can be reduced to 
a reachability game, this topic is constantly being studied. To learn more 
about reduction and [the theory of computation](#sipser), a nice and short introduction on the
reachability game has been written by [Berwanger](#berwanger).

## Getting started
### Installation
You can easily install the package via
[pip](https://pip.pypa.io/en/stable/installation/) with the following command:
```sh
pip install -i https://test.pypi.org/simple/ ggames
```
or you can download the
[sources](https://github.com/gfl-math-stat-info/ggames).
The program requires Python 3.9+. The program probably works on older versions
of Python 3.0+, but hasn't been tested.

### Usage
GGames can be used by importing it into a Python session.
```python
from ggames import cop_robber_game as crg

# Create a cycle of length 4.
V = list(range(4))
E = [(i, (i+1)%4) for i in range(4)]
print(crg.is_kcop_win(V, E, k=1)) # prints False
print(crg.is_kcop_win(V, E, k=2)) # prints True

# You can add a presence mapping for the edges.
tau = {(0, 1): '1', (1, 2): '001', (2, 3): '1', (3, 0): '1'}
print(crg.is_kcop_win(V, E, tau, 1)) # prints True
```
You can reduce a Cops and Robbers game to a reachability game.
```python
Vgg, Agg = crg.get_game_graph(V, E, tau, 1)
S0, S1, A, F = crg.game_graph_to_reachability_game(Vgg, Agg)
```
By computing the attractor set of the reachability game, you can extract a
winning strategy for the winner.
```python
from ggames import reachability_game as rg

attractor = rg.get_attractor(S0, S1, A, F)
current_config_vertex = (0, 2, False, 0)
# ^^ (cop position, robber position, False := cop's turn, time step)
next_moves = rg.get_next_winning_moves(current_config_vertex, A, attractor)
print(next_moves) # prints [(0, 2, True, 0), (1, 2, True, 0), (3, 2, True, 0)]
# ^^ Doesn't give only the best winning strategy.
next_moves = rg.get_next_winning_moves((3, 2, True, 0), A, attractor,
      player0_move=False)
print(next_moves) # prints []. The robber will lose in any case.
```
To get more information, see the [documentation](#documentation).

Also, by having a static of an edge-periodic graph into
[JSON](https://www.json.org/json-en.html) format, a console script can 
easily be called to answer basic questions.
```sh
kcop-win 1 outerplanar_graph.json # prints False
kcop-win 2 outerplanar_graph.json --output output.txt
cat output.txt # prints True
```
where outerplanar_graph.json contains
```json
{
   "V": [ 1, 2, 3, 4, 5, 6, 7, 8 ],
   "E": [ [1, 2], [1, 8], [2, 3], [2, 4], [2, 8], [3, 4], [4, 5], [4, 6],
         [5, 6], [6, 7], [6, 8], [7, 8] ]
}
```
To get help on a console script, you can use the *--help* arguments.
```sh
kcop-win --help # prints the help section
```

## Documentation
### `cops_robbers_game`
#### `get_game_graph(V: list, E: list, tau: dict, k: int): list`
Computes the game graph where the "k"-cops and robber game takes place on 
the edge periodic graph (V, E, tau). If "tau" is not specified, then the
graph is considered to be static. Returns the list of vertices and arcs of
the game graph.

Parameters | Description
--------- | ---------
V | The list of vertices
E | The list of edges
tau | The presence function of the edges in E in dict. If the graph is static, defaults to 'None'.
k | The number of cops in the game

#### `game_graph_to_reachability_game(V_gg: list, A_gg: list): list`
Computes and returns a reachable game corresponding to the game graph
G = (V_gg, A_gg).
Parameters | Description
--------- | ---------
V_gg | A list of vertices of a game graph
A_gg | A list of edges of a game graph


#### `is_kcop_win(V: list, E: list, tau: dict, k: int): boolean`
Computes if the time-varying graph ("V", "E", "tau") is "k"-cop win
by turning the game into a reachability game. 
Parameters | Description
--------- | ---------
V | A set of vertices 
E | A set of edges
tau | A map from E to a set of bit sequences
k | The number of cops that play on the time-varying graph


### `reachability_game`
#### `get_attractor(S0: list, S1: list, A: list, F: list): list`
Computes the attractor set.
Parameters | Description
--------- | ---------
S0 | A list of vertices
S1 | A list of vertices (must be disjointed of S0)
A | A sub-list (subset) of S0&times;S1 &cup; S1&times;S0
F | A sub-list (subset) of S1 as list.

#### `get_next_winning_moves(current_vertex: int, A: list, attractor: list, player0_move: boolean): list`
Compute a list of next moves that lead to a winning game for the player 0
if "player0_move" with respect to the game on the graph with the set of
arcs "A", its attractor set "attractor" and the vertex "current_vertex"
the token is on.
Parameters | Description
--------- | ---------
current_vertex | A vertex
A | A list of arcs
attractor | A list representing the attractor set.
player0_move | A flag meaning that it's Player 0's turn to play.`

## References
<p id="bondy-murty">[1] Bondy, J. A. & Murty, U. S. R. (1976). Graph Theory
With Applications. North-Holland.</p>
<p id="casteigts">[2] Casteigts, A. (2018). A Journey Through Dynamic
Networks (with Excursions). Université de Bordeaux.</p>
<p id="berwanger">[3] Berwanger, D. (2013). Graph games with perfect
information [Lecture notes]. ENS Cachan, Cachan.</p>
<p id="bonato-nowakowski">[4] Bonato, A. & Nowakowski, R. J. (2011).
The Game of Cops and Robbers on Graphs. American Mathematical Society.
http://dx.doi.org/10.1090/stml/061.<p>
<p id="erlebach-spooner">[5] Erlebach, T & Spooner, J. T. (2019). A
Game of Cops and Robbers on Graphs with Periodic Edge-Connectivity.
arXiv:1908.06828<p>
<p id="quilliot">[6] Quilliot, A. (1978). Jeux et pointes fixes sur les
graphes. PhD thesis, University of Paris VI.<p>
<p id="nowakowski-winkler">[7] Nowakowski, R. & Winkler, P. (1983).
Vertex-to-vertex pursuit in a graph. Discrete Mathematics, 32(2-3), 235-239.
https://doi.org/10.1016/0012-365X(83)90160-7.<p>
<p id="sipser">[8] Sipser, M. (2013). Introduction to the Theory of
Computation (3rd ed.). Cengage Learning.</p>

## Contribute
Feel free to contribute by adding new modules for other graph games, creating more
efficient algorithms for some classes of graphs, or even improving the
existing algorithms! For more information on how to contribute to this project,
read [How to Contribute](#TODO).

## Contact
If you have any further questions or want to contribute, feel free to send an
email to [Gabriel](https://github.com/gfl-math-stat-info).
