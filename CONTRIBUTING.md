# How to Contribute
Before to contribute, you should first read the [code of conduct](https://github.com/gfl-math-stat-info/ggames/edit/main/README.md) and the [README file](https://github.com/gfl-math-stat-info/ggames/edit/main/README.md).

## The project
GGames, short for Graphs Games, is a Python package that provides functions to 
study games on static or time-varying graphs.

### The structure
The structure of the project is quite simple. At its root, you have the code of conduct,
the license, the README and multiple configuration files used to test, publish and more
the package.
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
There is also two directories: "src" and "tests". For more information about this
file structure, you can read the [tutorial on Pypi](#https://packaging.python.org/tutorials/packaging-projects/).

### The workflow
<!-- TODO: Speak about GitFlow, briefly how it works, (Refer to a good tutorial
about GitFlow in English and French) and Tox (refer to tox installation page).
GitHub Actions will be also added very soon. I keep you in touch about that. -->
<!-- TODO: How to commit, not to often, not to rarely. Nice messages in commits.
Don't be scared to use --amend. Push with Pull requests. -->

We suggest these two tutorials to get started : GitFlow [EN](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)/[FR](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow) and [Tox](https://tox.readthedocs.io/en/latest/).
Try to [commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) when you have completed a "task" in the project : a complete, not necessary big, part of the project that can be identified as an improvement. Try to specify what that improvement is and describe what you did to accomplish it in the git commit message. Push using [pull requests](https://github.com/gfl-math-stat-info/ggames/pulls).

### Add a new feature
<!-- TODO: Explain: Coverage 100% by the new tests. If new module,
make sure it cannot be put inside another one. If one becomes too
big, speak with others to split the module into smaller ones.
NEVER delete function, but rather add deprecated warning -->
To add a new feature, first make sure if it could fit inside an already existing module or not (you can also ask a maintainer if you're unsure). If you think it should include an existing module, but it would make it too "bloaty", don't hesitate to ask to split the module into smaller ones (that we could all put under a same directory).
Do not delete functions : instead add a deprecated warning on it.
Because this project is a community one, any decisions made by a contributor might have significant impact on other users/contributors, so make sure to talk with a maintainer before to take a decision that might have big repercussions on the project.

### The code quality
<!-- TODO: PEP8, list the conventions already used here and the
importance to respect them. Use English everywhere since people speak different
languages. -->
Try to respect the code quality's guideline to ensure cohesion throughout the project.
The code standard this project is following is [PEP8](https://www.python.org/dev/peps/pep-0008/). Also use the single quotes (') instead of double quotes (") whenever applicable. Always write in english, please.

## How to report an issue
<!-- TODO: Describe how report issue. Explain that it's quick to do
and how it's important. Always check if it's a known issue. -->
List the issue under the appropriate tab and describe the impact on the project and how to reproduce it (if able). Try to evaluate if it's a quick fix or not and verify that's not a known issue.
