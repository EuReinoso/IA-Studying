import numpy

def step_function(soma):
    if soma >= 1:
        return 1
    else:
        return 0

def sigmoid_function(soma):
    return 1/(1 + numpy.exp(-soma))

def tahn_function(soma):
    return (numpy.exp(soma) - numpy.exp(-soma))/(numpy.exp(soma) + numpy.exp(-soma))