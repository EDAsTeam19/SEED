import numpy as np

class element(object):
    def __init__(self,dim):  #dim: Represents the dimension of the vector element.  
       self.dim = dim
       self.Element = np.zeros(self.dim) # element vector 
    def setVal(self,index,val): # Method that allows to introduce values to the vector element
        self.Element[index]=val
    def getElement(self,index): # Method that allows to get values of the vector element 
        return self.Element[index]
    def getDim(): # return the dimension of the vector lement
        return self.dim
