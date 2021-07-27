# Python modules to compute the cop-number of static and time-varying graphs (dynamic graphs)


## About The Project
This program takes a cop-number problem and decides if it is a k-cop-
winning graph. The graph can be either static or edge periodic. It proceeds
by reducing the problem to a reachability game.

## Installation
The following commands are the current valid ways of installing the program.

#### Using [pip](https://pip.pypa.io/en/stable/installation/)
```sh
pip install -i https://test.pypi.org/simple/ ggames
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

### Optional arguments:

To change the output path: ```sh -o [FilePath]``` or ```sh --output_path```

To activate verbose (more output informations) : ```sh  -v``` or ```sh --verbose```

To see the project's version : ```sh --version```

## References
The algorith is based on *[TODO:AutorName]*'s [paper] *[TODO:PaperURL]*.

## Contribute
Feel free to ask the permission to contribute by improving the existing algorithms or implement another reachability problem to this project!

## Contact
If you have any further questions or want to contribute, feel free to send an email to *[TODO:email]*
