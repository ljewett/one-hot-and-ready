# Machine Learning Kata

This kata will test your knowledge of core concepts in machine learning systems and your ability to provide craftsmanship in a cognitively challenging problem space. 100% accuracy is not as important as your process and being able to speak to the solution you've provided.

Please provide both the the items listed in the deliverables section, as well as responses to the questions at the end of the Readme.

# Instructions

NASA has asked you to model a set of sensor data they have provided to accurately predict the state of their radiator subsystem on the space shuttle. 

The file labeled **shuttle.trn** contained within this repo is a portion of their data they have set aside to train your model. **shuttle.tst** is the set they are saving to validate the accuracy of the solution you provide.

Within **shuttle.trn** there are 9 attributes available to generate your model. Unfortunately, due to the classified nature of the project, NASA is only able to give details about the meaning of two attributes:

The first column is time data, which NASA is not sure how relevant it is to the model and has randomized the ordering of data elements. The last column is the determined state of the radiator subsystem, which has been hand tabulated by trained observers and deemed accurate, however since it was collected by hand there may be some irregularities.

There are 7 different states that the radiator subsystem can be in:
```
1 Rad Flow 
2 Fpv Close 
3 Fpv Open 
4 High 
5 Bypass 
6 Bpv Close 
7 Bpv Open 
```

**NOTE**: The data is highly skewed, with approximately 80% of the time the state of the radiator subsystem is at **Rad Flow**, with **Bpv Close** and **Bpv Open** being the most rare.

# Key Deliverables
```
- A model that can predict the state of the radiator subsystem at 99.9%+ accuracy with the provided test data
- Ability to retrain the model easily as new data is introduced
- Ability to utilize the model generated easily so that when given sensor inputs, return an appropriate output
- Solution to address any data irregularity
- Ability to easily validate the accuracy of the model generated 
```


# Essay Questions
How did you create the model that you trained (e.g. if using deep learning, how did you choose your layers)?

How did you select the hyperparameters your model utilizes?

How did you address the problem with asymmetric data?

If we were moving your solution to production today (into the space shuttle!), what would you be concerned about?

# Attribution

Original shuttle data set provided by https://archive.ics.uci.edu/ml/datasets/Statlog+%28Shuttle%29