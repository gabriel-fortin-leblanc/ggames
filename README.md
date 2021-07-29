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
