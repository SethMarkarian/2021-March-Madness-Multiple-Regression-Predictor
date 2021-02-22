import pandas as pd
from sklearn import linear_model
import numpy as np
from scipy import stats
import statsmodels.api as sm

data =  pd.read_csv('\\Users\sethh\OneDrive - lafayette.edu\Desktop\Ross Stuff\March Madness NW PA - Data NW PA.csv')

print(data)

column_names = {'SMII 32',	'SMII 16',	'SMII 8',	'SMII 4',	'SMII 2',	'Seed Points',	'Should Make it to',	'Conference Wins',	'Conference PCT',	'Overall Wins',	'Overall PCT',	'Non-Conf Wins', 'Non-Conf PCT', 'Points Scored',	'Field Goal %',	'Field Goals Made',	'Field Goals Attempted/Game',	'Defensive Rebounds/Game',	'Rebounds/Game', '2 Points %',	'Free Throws Made/Game',	'Free Throws Attempted/Game', 'Assists',	'Assists per Game',	'Assists/Turnovers',	'Steals',	'Steals/Fouls',	'BPI Offense', 'BPI Defense',	'BPI',	'SOR Points',	'SOS Points',	'538 Ro32',	'538 S16',	'538 Elite 8',	'538 Final 4',	'Finals.1',	'Champion.1',	'Power Rating'}

X = data['Round Made']

#Single Regression
#for i in column_names :
#             y = data[[i]]
#             y = sm.add_constant(y)
#             results = sm.OLS(X, y).fit()
#             if results.rsquared > 0.8 and results.params[1] > 0 and results.pvalues[1] < 0.01:
#                 print(results.summary())


# 2 Variable
completed_combinations = []
for i in column_names :
    for j in column_names :
            if i != j and not (i + j in completed_combinations):
                y = data[[i, j]]
                y = sm.add_constant(y)
                results = sm.OLS(X, y).fit()
                if results.rsquared > 0.75 and results.params[1] > 0 and results.params[2] > 0 and results.pvalues[1] < 0.01 and results.pvalues[2] < 0.01:
                    print(results.summary())
            completed_combinations.append(i + j)
            completed_combinations.append(j + i)

# DONE UP TO HERE

#3 Variable
# completed_combinations = []
# for i in column_names :
#     for j in column_names :
#         for k in column_names :
#             if i != j and i != k and j != k and not (i + j + k in completed_combinations):
#                 y = data[[i, j, k]]
#                 y = sm.add_constant(y)
#                 results = sm.OLS(X, y).fit()
#                 if results.rsquared > 0.85 and results.params[1] > 0 and results.params[2] > 0 and results.params[3] > 0 and results.pvalues[1] < 0.01 and results.pvalues[2] < 0.01 and results.pvalues[3] < 0.01:
#                     print(results.summary())
#             completed_combinations.append(i + j + k)
#             completed_combinations.append(i + k + j)
#             completed_combinations.append(j + i + k)
#             completed_combinations.append(j + k + i)
#             completed_combinations.append(k + i + j)
#             completed_combinations.append(k + j + i)

#4 Variable
#for i in column_names :
#     for j in column_names :
#        for k in column_names :
#            for l in column_names :
#                  if i != j and i != k and i != l and j != k and j != l and k != l:
#                      y = data[[i, j, k, l]]
#                      y = sm.add_constant(y)
#                      results = sm.OLS(X, y).fit()
#                      if results.rsquared > 0.8 and results.params[1] > 0 and results.params[2] > 0 and results.params[3] > 0 and results.params[4] > 0 and results.pvalues[1] < 0.01 and results.pvalues[2] < 0.01 and results.pvalues[3] < 0.01 and results.pvalues[4] < 0.01:
#                          print(results.summary())