# How to Contribute
Before to contribute, you should first read the
[code of conduct](https://github.com/gfl-math-stat-info/ggames/blob/main/CODE_OF_CONDUCT.md)
and the [README file](https://github.com/gfl-math-stat-info/ggames/blob/main/README.md).

## The project
GGames, short for Graphs Games, is a Python package that provides functions to 
study games on static or time-varying graphs.

### The structure
The structure of the project is quite simple. At its root, you have the code of conduct,
the license, the README and multiple configuration files used to test, publish and more
the package.
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
There is also two directories: "src" and "tests". For more information about this
file structure, you can read the [tutorial on Pypi](https://packaging.python.org/tutorials/packaging-projects/).

### The workflow
On your machine, you can manage your workflow like you want, but our project
hold a "tox" configuration file that allows you to use [Tox](https://tox.readthedocs.io/en/latest/).
Tox is an small an easy-to-use tool to execute multiple commands on a project.
With the "tox.ini", you can quickly test your code and print a report about
the coverage of your tests. Keep in mind that your tests will be run
with the version of your Python interpreter, but will be run with other
versions on the remote.

The workflow GitFlow is used to keep an understanding method of creation of
branches. For more information about GitFlow, you can read the
[tutorial on Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

After being reading familiar with this project, a good way to start contributing is
to take a look to the known [issues](https://github.com/gfl-math-stat-info/ggames/issues)
and resolve one. If there is no interesting one, you can create a new feature.

When you've completed a new feature or resolved a issue, do a
[pull request](https://github.com/gfl-math-stat-info/ggames/pulls).

### Add a new feature
When you add a new feature, make sure to add to the good module. If the feature is a new module,
then be sure it can't fit into an existing one. If you think it should include into an existing
module, but it would make it too "bloaty", ask to split the module into smaller ones
(that we could all put under a same directory).

Never functions : instead add a deprecated warning on it. A deleted function may imply bugs into
the users' programs.

This project is a community one, any decisions made by a contributor might have
significant impact on other users/contributors, so make sure to
[talk with a maintainer](https://github.com/gfl-math-stat-info/ggames/discussions)
before to take a decision that might have big repercussions on the project.

### The code quality
Try to respect the code quality's guideline to ensure cohesion throughout the project.
The code standard this project is following is
[PEP8](https://www.python.org/dev/peps/pep-0008/). It exists other unofficial guidelines
used in this project, like using the single quotes (') instead of double quotes (") for strings.
Please respect them.

We come from different nations and don't speak the same language. Since English is the most spoken
one, we use it everywhere in the project.

## How to report an issue
Reporting new [issues](https://github.com/gfl-math-stat-info/ggames/issues)
when one's discovered is important to improve this project. Before reporting
one, verify that's not known. List the issue under the appropriate tab and describe the impact
on the project and how to reproduce it. Try to evaluate if it's a quick fix.
