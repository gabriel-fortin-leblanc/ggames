# GGames

## About The Project
<<<<<<< HEAD
This Python package provides functions to study games on graphs that can be
either static or time-varying. The project was first created to help students
with answering questions about the [cop-number](#cops-and-robbers-game) of
[edge-periodic graph](#time-varying-graphs).
=======
This program takes a cop-number problem and decides if it is a k-cop-
winning graph. The graph can be either static or edge periodic. It proceeds
by reducing the problem to a reachability game.

## Installation
The following commands are the current valid ways of installing the program.

#### Windows
   ```sh
   
   ```

#### Linux
   ```sh
   
   ```

The program requires Python 3.9

## Usage
The program takes in two arguments: a cop number and a JSON file describing the graph. The file must include a list of vertices ("V"), a list of edges ("E") and, optionally, a list of *[how do you describe the binary sequences?]*, as follows:
   ```sh
   {
    "V" : [ 1, 2, 3 ],
    "E" : [ [1, 2], [2, 3], [3, 1] ],
    "tau" : [ "0110", "1", "001" ]
    }
   ```
Several sample graphs can be found under the folder titled "graph_test_dir".
>>>>>>> coverage

## Primilinary
The user must have a minimal knowledge of [graph theory](#bondy-murty) and 
[time-varying graph](#casteigts) to enjoy this package. Depending on the field
of study of the user, he should be initiated to the
[cops and robbers game](#bonato-nowakowski) and to the
[reachability game](#berwanger). There are more references at the end of this
document.

### Cops and robbers game
The cops and robbers game was first introduced independently by
[Quilliot](#quilliot), and by [Nowakowski and Winkler](#nowakowski-winkler).
This game played by *k* cops and a robber who take place on vertices of a
graph. Each player takes turn by moving along an edge and the cops play first.
They win if at any moment a cop occupies the same vertex as the robber. If the
robber can avoid the capture forevery, he wins. A good survey on the subject
has been written by [Bonato and Nowakowski](#bonato-nowakowski).

It exists a lot of different variants of this game. One is the cops and robbers
game on time-varying graphs, and more specificaly on distrete ones. This
variant was first introduced by [Erlebach and Spooner](#erlebach-spooner). It's
pretty recent and a lot of questions wait to be answered.

### Reachability game
The reachability game is player by two players, Player 0 and Player 1, on a
graph. The set of vertices is partitionned into two sets, *S0* and *S1*. A
token is placed on a vertex of the graph and when the token is on a vertex of
*S0*, Player 0 moves the token to an adjancent vertex, and similarly if the
token is on a vertex of *S1*. There is also a subset of *S1*, *F*. The Player 0
wins if the token occupy a vertex of *F*, and the Player 1 wins if he can avoid
that forever. This game is very studied since we can reduce important problems
to it. To learn more about the reduction and about
[the theory of computation](#sipser). A nice and short introduction on
rechability game has been written by [Berwanger](#berwanger).

## Getting started
### Installation
You can easily install the package via
[pip](https://pip.pypa.io/en/stable/installation/) with the following command:
```sh
pip install -i https://test.pypi.org/simple/ ggames
```
or you can download the
[sources](#https://github.com/gfl-math-stat-info/ggames).
The program requires Python 3.9+. The program probably works on older version
of Python 3+, but hasn't been tested.

### Usage
GGames can be used by importing it into a Python session.
```python
from ggames import cop_robber_game as crg

# Create a cycle of length 4.
V = list(range(4))
E = [(i, (i+1)%4) for i in range(4)]
print(crg.is_kcop_win(V, E, k=1)) # print False
print(crg.is_kcop_win(V, E, k=2)) # print True

# You can add a presence mapping for the edges.
tau = {(0, 1): '1', (1, 2): '001', (2, 3): '1', (3, 0): '1'}
print(crg.is_kcop_win(V, E, tau, 1)) # print True
```
You can reduce a cops and robbers game to a reachability game.
```python
Vgg, Agg = crg.get_game_graph(V, E, tau, 1)
S0, S1, A, F = crg.game_graph_to_reachability_game(Vgg, Agg)
```
By computing the attractor set of the reachability game, you can extract a
winning stratedy for the winner.
```python
from ggames import reachability_game as rg

attractor = rg.get_attractor(S0, S1, A, F)
current_config_vertex = (0, 2, False, 0)
# ^^ (cop position, robber position, False := cop's turn, time step)
next_moves = rg.get_next_winning_moves(current_config_vertex, A, attractor)
print(next_moves) # print [(0, 2, True, 0), (1, 2, True, 0), (3, 2, True, 0)]
# ^^ Doesn't give only the best winning strategy.
next_moves = rg.get_next_winning_moves((3, 2, True, 0), A, attractor,
      player0_move=False)
print(next_moves) # print []. The robber will lost in any case.
```
To get more information, see the [docuentation](#TODO).

Also, by having a static of edge-periodic graph into
[JSON](#https://www.json.org/json-en.html) format, a console script can be
easily called to answer basic questions.
```sh
kcop-win 1 outerplanar_graph.json # print False
kcop-win 2 outerplanar_graph.json --output output.txt
cat output.txt # print True
```
where outerplanar_graph.json contains
```json
{
   "V": [ 1, 2, 3, 4, 5, 6, 7, 8 ],
   "E": [ [1, 2], [1, 8], [2, 3], [2, 4], [2, 8], [3, 4], [4, 5], [4, 6],
         [5, 6], [6, 7], [6, 8], [7, 8] ]
}
```
To get help about a console script, you can use the *--help* arguments.
```sh
kcop-win --help # print the help
```

## References
<p id="bondy-murty">[1] Bondy, J. A. & Murty, U. S. R. (1976). Graph Theory
With Applications. North-Holland</p>
<p id="casteigts">[2] Casteigts, Arnaud. (2018). A Journey Through Dynamic
Networks (with Excursions). habilitation à diriger des recherches, Université
de Bordeaux.</p>
<p id="berwanger">[3] Berwanger, Dietmar. (2013). Graph games with perfect
information. arXiv:1407.1647.</p>
<p id="bonato-nowakowski">[4] Bonato, Antony & Nowakowski, Richard J. (2011).
The Game of Cops and Robbers on Graphs. American Mathematical Society.<p>
<p id="erlebach-spooner">[5] Erlebach, Thomas & Spooner, Jakob T. (2019). A
Game of Cops and Robbers on Graphs with Periodic Edge-Connectivity.
arXiv:1908.06828<p>
<p id="quilliot">[6] Quilliot, Alain. (1978). Jeux et pointes fixes sur les
graphes. PhD thesis, University of Paris VI.<p>
<p id="nowakowski-winkler">[7] Nowakowski, Richard & Winkler, Peter. (1983).
Vertex-to-vertex pursuit in a graph. Discrete Mathematics.<p>
<p id="sipser">[8] Sipser, Michael. (2013). Introduction to the Theory of
Computation, Third Edition. Cengage Learning.</p>

## Contribute
Feel free to contribute by adding new modules for other graph games, new
algorithms more efficient for some classes of graphs or even by improving the
existing algorithms! For more information on how contributing to this project,
read [How to Contribute](#TODO).

## Contact
If you have any further questions or want to contribute, feel free to send an
email to [Gabriel](#mailto:gabriel.fortin-leblanc@umontreal.ca).
