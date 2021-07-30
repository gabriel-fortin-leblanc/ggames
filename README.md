# GGames

## About The Project
This Python package provides functions to study games on graphs that can be
either static or time-varying. The project was first created to help students
with answering questions about the [cop-number](#cops-and-robbers-game) of
[edge-periodic graph](#time-varying-graphs).

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
The program requires Python 3.9+.

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

The program takes in two arguments: a cop number and a JSON file describing the graph. The file must include a list of vertices ("V"), a list of edges ("E") and, optionally, a list ("tau") with as many elements as the list of edges that contains binary sequences which determine the dynamic aspect of the graph. More precisely, the nth sequence of that list represent the appearance sequence of the nth edge in "E". At the time T, the nth edge appears if the nth sequence, say x, has a '1' at x[T%x.size]. Example of a valid JSON:
   ```sh
   {
    "V" : [ 1, 2, 3 ],
    "E" : [ [1, 2], [2, 3], [3, 1] ],
    "tau" : [ "0110", "1", "001" ]
    }
   ```
Several sample graphs can be found under the folder titled "graph_test_dir".

### Optional arguments:

## References
<p id="bondy-murty">[1] Bondy, J. A. & Murty, U. S. R. (1976). Graph Theory With Applications. North-Holland</p>
<p id="casteigts">[2] Casteigts, Arnaud. (2018). A Journey Through Dynamic Networks (with Excursions). habilitation à diriger des recherches, Université de Bordeaux.</p>
<p id="berwanger">[3] Berwanger, Dietmar. (2013). Graph games with perfect information. arXiv:1407.1647.</p>
<p id="bonato-nowakowski">[4] Bonato, Antony & Nowakowski, Richard J. (2011). The Game of Cops and Robbers on Graphs. American Mathematical Society.<p>
<p id="erlebach-spooner">[5] Erlebach, Thomas & Spooner, Jakob T. (2019). A Game of Cops and Robbers on Graphs with Periodic Edge-Connectivity. arXiv:1908.06828<p>
<p id="quilliot">[6] Quilliot, Alain. (1978). Jeux et pointes fixes sur les graphes. PhD thesis, University of Paris VI.<p>
<p id="nowakowski-winkler">[7] Nowakowski, Richard & Winkler, Peter. (1983). Vertex-to-vertex pursuit in a graph. Discrete Mathematics.<p>
<p id="sipser">[8] Sipser, Michael. (2013). Introduction to the Theory of Computation, Third Edition. Cengage Learning.</p>

To see the project's version : ```sh --version```

## References
The algorith is based on *[TODO:AutorName]*'s [paper] *[TODO:PaperURL]*.

## Contribute
Feel free to ask the permission to contribute by improving the existing algorithms or implement another reachability problem to this project!

## Contact
If you have any further questions or want to contribute, feel free to send an email to *[TODO:email]*
