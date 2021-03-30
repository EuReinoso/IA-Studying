import pandas
from sklearn.model_selection import train_test_split

predictors = pandas.read_csv('deep learning/breast_cancer/entradas_breast.csv')
answer = pandas.read_csv('deep learning/breast_cancer/saidas_breast.csv')

predicted_training, predictors_test, answer_training, answer_test = train_test_split(predictors, answer, test_size=0.25)

