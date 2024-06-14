import numpy as np



class Trucking_1D_Problem():

    def __init__(self):
        self.box_lengths = []
        self.box_amount = 0
        self.container_length = 0
        self.qubo_length = 0
        self.penalty_value = 0

    def gen_problem(self,box_lengths,container_length):
        self.box_lengths = box_lengths
        self.box_amount = len(box_lengths)
        self.container_length = container_length
        self.qubo_length = self.box_amount * self.container_length 
        self.penalty_value = sum(self.box_lengths) 

    def gen_qubo_matrix(self):
        #Objective Function
        Q = np.zeros((self.qubo_length,self.qubo_length))
        #First Hamiltonian
        for i in range(self.box_amount):
            for j in range(self.container_length):
                index = i*self.container_length + j
                Q[index , index] -= self.box_lengths[i]
        #Second Hamiltonian 
        for i in range(self.box_amount):
            for j in range(self.container_length):
                for k in range(self.container_length):
                    if j == k:
                        continue
                    if k < j:
                        continue
                    if k > j:
                        index01 = i*self.container_length + j
                        index02 = i*self.container_length + k
                        Q[index01, index02] += 0.5*self.penalty_value
                        Q[index02, index01] += 0.5*self.penalty_value
        #Third Hamiltonian
        for i1 in range(self.box_amount):
            for i2 in range(self.box_amount):
                if i1 == i2:
                    continue 
                for j in range(self.container_length):
                    for k in range(self.box_lengths[i1]):
                        if j + k < self.container_length:
                            index1 = i1*self.container_length +j
                            index2 = i2*self.container_length +j + k
                            if index2 < self.qubo_length:
                                Q[index1, index2] += 0.5*self.penalty_value 
                                Q[index2, index1] += 0.5*self.penalty_value
        #Fourth Hamiltonian
        for i in range(self.box_amount):
            for j in range(self.container_length):
                if j > self.container_length - self.box_lengths[i]:
                    index3 = i*self.container_length + j
                    Q[index3,index3] += 1*self.penalty_value
        
        return Q
