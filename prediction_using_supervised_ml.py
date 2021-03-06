# -*- coding: utf-8 -*-
"""Prediction using Supervised ML.ipynb

Automatically generated by Colaboratory.


#The Sparks Foundation's Graduate Rotational Internship Program (GRIP)
##Data Science & Business Analytics' Task
###Prediction using Supervised ML
####(Level - Beginner)
* To Predict the percentage of an student based on the no. of study hours.
* This is a simple linear regression task as it involves just 2 variables.
* Dataset is available at http://bit.ly/w-data 
* We will try to predict a student's score when a student studies for 9.25 hrs/ day?

##By - Nihir Yadav

##Importing all libraries required
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas
import numpy
import matplotlib

# %matplotlib inline

"""##Reading data from the URL"""

url = "http://bit.ly/w-data"
dataset = pandas.read_csv(url)
print("Data has been imported successfully.")
print()
print(dataset)

"""##Checking for any missing values"""

print("Missing Value : ",dataset.isnull().sum().values.sum())

"""##Summary and some basic statistical details about the data"""

print(dataset.shape)

print(dataset.head())

print(dataset.info())

print(dataset.describe())

"""##Visualizing the data
###Plotting the data on two dimensinal graph to visualize the dataset and see if we can detect any relationship between the data. We will create the graph with the following code:
"""

matplotlib.pyplot.rcParams["figure.figsize"] = [10,10]
dataset.plot(x='Hours', y='Scores', style='*', color='green', markersize=7)
matplotlib.pyplot.title('Hours vs Percentage')  
matplotlib.pyplot.xlabel('Hours Studied') 
matplotlib.pyplot.ylabel('Percentage Score')  
matplotlib.pyplot.show()

"""####We observed linear relation between the  and percentage and number of hours studiedbased from the graph.

##Preparing the data
####We will mark the data into "features" (inputs) and "labels". Features are the inputs and labels are the output.
"""

X = dataset.iloc[:, :-1].values  
Y = dataset.iloc[:, 1].values

print(X)
print(Y)

"""####We marked our attributes and labels. Now to split the data into training and test sets. Splitting the data helps us effectively test our algorithm against unknown data."""

from sklearn.model_selection import train_test_split  
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

"""##Training the model
####Choosing the model
"""

from sklearn.linear_model import LinearRegression  

regressor = LinearRegression()

"""####Fitting the model"""

regressor.fit(X_train, Y_train) 

print("Training complete")

"""##Visualizing the model"""

line = regressor.coef_*X+regressor.intercept_

matplotlib.pyplot.scatter(X_train, Y_train, color='green')
matplotlib.pyplot.plot(X, line, color='blue');
matplotlib.pyplot.rcParams["figure.figsize"] = [10,10]
matplotlib.pyplot.title('Percentage vs Hours')
matplotlib.pyplot.xlabel('Hours Studied')  
matplotlib.pyplot.ylabel('Percentage Score')
matplotlib.pyplot.show()

"""##Making Predictions"""

print(X_test)
Y_pred = regressor.predict(X_test)

"""####Evaluating Predictions"""

df = pd.DataFrame({'Actual': Y_test, 'Predicted': Y_pred})
print(df)

"""####Coefficient of determination"""

print(regressor.score(X_test, Y_test))

"""##Making the predictions"""

hours = numpy.array([[9.25]])
own_pred = regressor.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

"""##Error Value"""

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred))
