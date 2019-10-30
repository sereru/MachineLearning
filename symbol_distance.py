#Recomend value function
import numpy as np

K=3

y_true = [[1,2], [1,2],[4],[1,2,3,4],[3,4]]

y_pred=[[1,2,4],[4,1,2],[1,4,3],[1,2,3],[1,2,4]]

def symbol(true, pred):
    sum_precision = 0.0

    for i,p in enumerate(pred):
        if p in true:
            tmp = 1/(2**i)
            sum_precision += tmp
    m = 2*(1-(1/2)**len(true))
    return sum_precision/m

def distance(y_true,y_pred):
    return np.mean([symbol(y_i_true,y_i_pred) for y_i_true, y_i_pred in zip(y_true, y_pred)])

print(distance(y_true,y_pred))
