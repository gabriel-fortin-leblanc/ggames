# How to Contribute
<!-- TODO: What to read first README, ... -->
You should first read the [code of conduct](https://github.com/gfl-math-stat-info/ggames/edit/main/README.md) and the [read me](https://github.com/gfl-math-stat-info/ggames/edit/main/README.md)

## The project
<!-- TODO: A brief description of the project. Refer to README for mor info. -->
<!-- TODO: Explain that the decision a contributor takes impact on others.
If the decision is too big, speak with a maintainer. -->
GGames, short for Graph Games, is a Python package that provides functions to 
study games on static or time-varying graphs. The project was first created to 
help students answer questions about the [cop-number](#cops-and-robbers-game)
of [edge-periodic graph](#time-varying-graphs).
Because this project is a collection of packages, any decisions made by a contributor might have significant impact on other users/contributors, so make sure to talk with a maintainer if you have an idea that might have big repercussions on the project.

### The structure
<!-- TODO: Speak about the different files and directories our
repository is composed -->
The base repository contains the project's documentation,licensing and configuration files. 
The tests repository contains the tests for each modules and a sub repository called tests_graph_json that contains test graphs encoded in json. We suggest you to read through the test graphs to see examples of graphs and refer to the tests files if you want usage examples.
The ggames repository contains the project's modules. Right now there's the cop & robber game module and the reachability utility module.

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
