
import csv

class Utilbox:

    def __init__(self) -> None:
        pass

    def create_matrix(self,name):
        
        data = []
        with open(name) as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    
    def get_unique_vector_vals(self, vector):

        return list(set(vector))        
    
    
    def get_unique_matrix_vals(self, matrix):
        pass
    def get_attr_count(self, vector, matrix):

        attrs = { x : 0 for x in vector}

        for row in matrix:
            attrs[row[0]] += 1
        
        return attrs
