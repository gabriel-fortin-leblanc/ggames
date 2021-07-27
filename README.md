# Python modules to compute the cop-number of static and time-varying graphs (dynamic graphs)


## About The Project
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

## Contribute


## Contact
If you have any further questions, feel free to send an email to *[email]*
