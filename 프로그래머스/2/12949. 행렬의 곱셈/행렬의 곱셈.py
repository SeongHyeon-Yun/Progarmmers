import numpy as np
import json

def solution(arr1, arr2):
    answer = [[]]
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    result = np.dot(arr1, arr2)
    result = result.tolist()
    
    
    
    return result