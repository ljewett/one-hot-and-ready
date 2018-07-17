# Setup

To install pipenv, from the newly cloned project directory run:

```shell
pip install -rU requirements.txt
```

Then to install the rest of the dependencies, from the project directory run:
```shell
pipenv install
```
*note*: this does install xgboost, which is a compiled library and may take a few minutes to complete.

# Running Tests
To run tests and verify everything appeared correctly, enter from the project directory:
```shell
pipenv run pytest
```

# Running the Executable
## Help
To successfully run the executable and produce a help prompt, run:
```shell
pipenv run ./main.py help
```

## Train
To train a new model, make sure the training data is located in the project folder, and then run:
```shell
pipenv run ./main.py train
```

## Validate
To validate the trained model's accuracy against NASA's provided training data, make sure that a model exists in the *model* folder,
or update the config file to point to a saved xgboost file. Then from the project directory, run:
```shell
pipenv run ./main.py validate
```

## Utilize
To make use of the model in real time, make sure that a model exists in the model subdirectory or update the config file to
point to a saved xgboost model. Then from the project directory, run:
```shell
pipenv run ./main.py predict NUM1 NUM2 ... NUM9
```

Where **NUM1** through **NUM9** are the are the associated readouts from input sensors.


# Essay Questions
**How did you create the model that you trained (e.g. if using deep learning, how did you choose your layers)?**
I chose to run with xgboost for a variety of reasons. Xgboost has been making the rounds at a competition level and performs
very well with tabular data. It's a gradient boosted decision tree, which has been optimized to train and run very quickly.
The downside of course is that it was able to achieve relatively high level accuracy (~99.972%) without too much
tuning, and instead I focused on ways to approach training and working with the model that would be easy to test and
understand from a researchers perspective.

**How did you select the hyperparameters your model utilizes?**
So there are only a few hyperparameters that xgboost really cares about, namely the objective, how long to train for,

**How did you address the problem with asymmetric data?**
The first step I took was to diagnose where the problem areas with the input data existed, to make sure that it was able to
handle the rarest cases associated with the data. Those were at 100% accuracy


**If we were moving your solution to production today (into the space shuttle!), what would you be concerned about?**
The current iteration does load the model from memory each time it runs before producing an output, and relies on a variety
of python libraries. Obviously that's slow and probably not ready, and this setup aims to make training a model perhaps from
a research station easy to accomplish. If we were looking to move this into a production environment contained within a closed
system, part of the justification in choosing XGBOOST is that it's easy enough to compile the command line utility and 
run the executable to load the trained model as a complete utility with relative ease. There may also be other conditions
we'd want consider, especially if this model was expected to be extremely responsive at producing predictions.