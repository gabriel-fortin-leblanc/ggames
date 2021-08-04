# How to Contribute
Before contributing, you should first read the
[code of conduct](https://github.com/gfl-math-stat-info/ggames/blob/main/CODE_OF_CONDUCT.md)
and the [README file](https://github.com/gfl-math-stat-info/ggames/blob/main/README.md).

## The Project
GGames, short for Graphs Games, is a Python package that provides functions to 
study games on static or time-varying graphs.

### The Structure
The structure of the project is quite simple. At its root, you have the code of conduct,
the license, the README, and multiple configuration files used to test the package,
publish changes, and more.
```
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│   ├── ggames
│   │   ├── cop_robber_game.py
│   │   ├── __init__.py
│   │   └── reachability_game.py
│   └── ggames.egg-info
│       │
│       .
├── tests
│   ├── test_cop_robber_game.py
│   ├── test_kcop_win_console_script.py
│   ├── test_reachability_game.py
│   └── tests_graph_json
│       │
│       .
└── tox.ini
```
There are also two directories: "src" and "tests". For more information about this
file structure, you can read the [tutorial on Pypi](https://packaging.python.org/tutorials/packaging-projects/).

### The Workflow
On your machine, you can manage your workflow however you want, but our project
holds a "tox" configuration file that allows you to use [Tox](https://tox.readthedocs.io/en/latest/).
Tox is a small and easy-to-use tool to execute multiple commands on a project.
With the "tox.ini" file, you can quickly test your code and print a report about
the coverage of your tests. Keep in mind that your tests will be run
with the version of your Python interpreter, but will be run with other
versions on the remote.

The workflow GitFlow is used to keep an understandable method of creation of
branches. For more information about GitFlow, you can read the
[tutorial on Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

After familiarizing yourself with this project, a good way to start contributing is
by taking a look at known [issues](https://github.com/gfl-math-stat-info/ggames/issues)
and resolving one. Alternatively, you can create a new feature.

When you've completed a new feature or resolved an issue, do a
[pull request](https://github.com/gfl-math-stat-info/ggames/pulls).

### Add a New Feature
When you add a new feature, make sure to add it to the correct module. If the feature 
is a new module, ensure it can't fit into an existing one. If you think it should be
included in an existing module but would make it too "bloated", ask to split the module 
into smaller ones (that we could place under a same directory).

Never delete functions : instead, add a deprecated warning on it. A deleted function may
cause bugs in the users' programs.

This project is a community one, any decisions made by a contributor might have
significant impact on other users/contributors, so make sure to
[talk with a maintainer](https://github.com/gfl-math-stat-info/ggames/discussions)
before taking a decision that might have big repercussions on the project.

### The Code Quality
Try to respect the code quality's guidelines to ensure cohesion throughout the project.
The code standard this project follows is [PEP8](https://www.python.org/dev/peps/pep-0008/). 
There exist other unofficial guidelines used in this project, such as using single quotes (') 
instead of double quotes (") for strings. Please respect them.

We come from different nations and don't speak the same language. Since English is the most 
commonly spoken one, we use it everywhere in the project.

## How to report an issue
Reporting new [issues](https://github.com/gfl-math-stat-info/ggames/issues)
when one's discovered is important to improve this project. Before reporting
one, verify that it's not known. List the issue under the appropriate tab and describe the impact
on the project and how to reproduce it. Try to evaluate if it's a quick fix.
