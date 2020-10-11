# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#Read the dataset
dataset = pd.read_csv('hiring.csv')
#Rename the obtained columns
dataset.columns = ['experience','test_score','interview_score','salary']
#Fill the empty test scores by mean
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)
#Get the training data
X = dataset.iloc[:, :3]

#Converting words to integer values
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, np.nan: 0}
    return word_dict[word]
#Get the experience column converted to numbers
X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

#Test dataset
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2, 9, 6]]))