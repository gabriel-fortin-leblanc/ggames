# Python modules to compute the cop-number of static and time-varying graphs (dynamic graphs)


## About The Project
This Python package provides functions to study games on graphs that can be either static or time-varying. The project was first created to help students with answering questions about the [cop-number](#cops-and-robber-game) of [edge-periodic graph](#time-varying-graphs).

## Primilinary
### Graph
A graph $G$ is a ordered pair of two sets, the set of vertices $V$ and the set of edges $E$. A vertex can be any kind of object and an edge is a pair of vertices. Thus, for a given graph $G = (V, E)$, $E \subseteq V \times V$. A graph can be directed, which in this case the graph is defined with a set of arcs $A$ instead of $E$. The set of arcs is rather an ordered pair of vertices. For a good introduction to graph, refer to [[1]](#bondy-murty).

### Time-varying graph
A time-varying graph (also called dynamic graph or temporal graph) is a graph that changes over time. The time domain $\mathcal{T}$ can be either discrete ($\mathbb{N}$) or continuous ($\mathbb{R}^+$). A time-varying graph $\mathcal{G} = (V, E, \mathcal{T}, \rho, \zeta)$ is composed of a set of vertices $V$, a set of edges $E$, a time domain $\mathcal{T}$ (also called lifetime of time horizon), a presence function $\rho: E \times \mathcal{T} \to \{0, 1\}$ and a latency function $\zeta: E \times \mathcal{T} \to \mathcal{T}. A prensence function informs you if the edge $e \in E$ is in the graph at the time $t \in \mathcal{T}$. The latency function tells you how much time it takes for a token (any kind of object) to cross the edge $e \in E$ at the time $\mathcal{T}$. Some models of time-varying graph are improved by adding more restrictions like a presence function and a latency function for the vertices. For more information about time-varying graph, refer to [[2]](#casteigts).

### Reachability game


### Cops and robber game
### Cops and robber game on time-varying graph

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
<p id="casteigts">[2] Casteigts, Arnaud. (June 2018). A Journey Through Dynamic Networks (with Excursions). habilitation à diriger des recherches, Université de Bordeaux.

## Contribute


## Contact
If you have any further questions, feel free to send an email to *[email]*
