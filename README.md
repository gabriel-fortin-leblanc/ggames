# Python modules to compute the cop-number of static and time-varying graphs (dynamic graphs)


## About The Project
This Python package provides functions to study games on graphs that can be either static or time-varying. The project was first created to help students with answering questions about the [cop-number](#cops-and-robbers-game) of [edge-periodic graph](#time-varying-graphs).

## Primilinary
### Graph
A graph $G$ is an ordered pair of two sets, the set of vertices $V$ and the set of edges $E$. A vertex can be any kind of object and an edge is a pair of vertices. Thus, for a given graph $G = (V, E)$, $E \subseteq V \times V$. A graph can be directed, which in this case the graph is defined with a set of arcs $A$ instead of $E$. The set of arcs is rather an ordered pair of vertices. For a good introduction to graph, refer to [[1]](#bondy-murty).

### Time-varying graph
A time-varying graph (also called dynamic graph or temporal graph) is a graph that changes over time. The time domain $\mathcal{T}$ can be either discrete ($\mathbb{N}$) or continuous ($\mathbb{R}^+$). A time-varying graph $\mathcal{G} = (V, E, \mathcal{T}, \rho, \zeta)$ is composed of a set of vertices $V$, a set of edges $E$, a time domain $\mathcal{T}$ (also called lifetime of time horizon), a presence function $\rho: E \times \mathcal{T} \to \{0, 1\}$ and a latency function $\zeta: E \times \mathcal{T} \to \mathcal{T}$. A prensence function informs you if the edge $e \in E$ is in the graph at the time $t \in \mathcal{T}$. The latency function tells you how much time it takes for a token (any kind of object) to cross the edge $e \in E$ at the time $\mathcal{T}$. Some models of time-varying graph are improved by adding more restrictions like a presence function and a latency function for the vertices. For more information about time-varying graph, refer to [[2]](#casteigts).

### Reachability game
A reachability games can be defined by a pair $(G, F)$ where $G = (V, A)$ is a directed graph with a partition of $V = S_0 \sqcup S_1$ and $F \subseteq S_1$. A token is initialy placed on a vertex of $G$. Two players Player 0 and player 1 take turn by moving the token along the arcs. When the token lay on a vertex of $S_0$, it's at the Player 0 to move the token, and similarly when the token is on a vertex of $S_1$. The Player 0 wins if the token lay on a vertex of $F$, and the Player 1 wins if he can avoid this forever. For an introduction two the subject, refer to [[3]](#berwanger).

### Cops and robbers game
A cops and robbers game is played on a graph with rounds. At the round 0 $k > 0$ tokens reprensenting the cops are placed on vertices of the graph, and another toke, the robber, is placed on a vertex. For next rounds, each cop can move to adjancent vertex to theirs. After the cops' move, the robber does the same. The cops win if at any time in the game, a cop occupy the same vertex of the robber, and the robber wins if he can avoid that forever. This game was first introduced seperately by Quilliot [[6]](#quilliot) and by Nowakowski and Winkler [[7]](#nowakowski-winkler). It exists a lot of variants of the game. The interesting mesures on this game is the cop-number which is the minimal number of cops to catch a robber on a given graph, and the capture time which is the maximum number of rounds for cop-number cops to catch the robber. For a survey of the subject, read [[4]](#bonato-nowakowski).

### Cops and robbers game on time-varying graph
The variant of the cops and robbers game on time-varying graph was first introduced by Erlebach and Spooner in A Game of Cops and Robbers on Graphs with Periodic Edge-Connectibity [[5]](#erlebach-spooner). The model of [time-varying graph](#time-varying-graph) mostly studied is composed of $\mathcal{G} = (V, E, \tau)$ where $\tau: E \to \{0, 1\}^*$ is the presence function for the edges. Graphs from this model are also called edge periodic graphs.

## Installation
The following commands are the current valid ways of installing the program.

#### Using pip
```sh
   pip install -i https://test.pypi.org/simple/ ggames
```
 
#### Windows
   ```sh
   
   ```

#### Linux
   ```sh
   
   ```

The program requires Python 3.?+

## Usage
The program takes in two arguments: a cop number and a JSON file describing the graph. The file must include a list of vertices ("V"), a list of edges ("E") and, optionally, a list ("tau") with as many elements as the list of edges that contains binary sequences which determine the dynamic aspect of the graph. More precisely, the nth sequence of that list represent the appearance sequence of the nth edge in "E". At the time T, the nth edge appears if the nth sequence, say x, has a '1' at x[T%x.size]. Example of a valid JSON:
   ```sh
   {
    "V" : [ 1, 2, 3 ],
    "E" : [ [1, 2], [2, 3], [3, 1] ],
    "tau" : [ "0110", "1", "001" ]
    }
   ```
Several sample graphs can be found under the folder titled "graph_test_dir".

There's also a list of optional arguments:

## References
<p id="bondy-murty">[1] Bondy, J. A. & Murty, U. S. R. (1976). Graph Theory With Applications. North-Holland</p>
<p id="casteigts">[2] Casteigts, Arnaud. (2018). A Journey Through Dynamic Networks (with Excursions). habilitation à diriger des recherches, Université de Bordeaux.</p>
<p id="berwanger">[3] Berwanger, Dietmar. (2013). Graph games with perfect information. arXiv:1407.1647.</p>
<p id="bonato-nowakowski">[4] Bonato, Antony & Nowakowski, Richard J. (2011). The Game of Cops and Robbers on Graphs. American Mathematical Society.<p>
<p id="erlebach-spooner">[5] Erlebach, Thomas & Spooner, Jakob T. (2019). A Game of Cops and Robbers on Graphs with Periodic Edge-Connectivity. arXiv:1908.06828<p>
<p id="quilliot">[6] Quilliot, Alain. (1978). Jeux et pointes fixes sur les graphes. PhD thesis, University of Paris VI.<p>
<p id="nowakowski-winkler">[7] Nowakowski, Richard & Winkler, Peter. (1983). Vertex-to-vertex pursuit in a graph. Discrete Mathematics.<p>

## Contribute


## Contact
If you have any further questions, feel free to send an email to *[email]*
