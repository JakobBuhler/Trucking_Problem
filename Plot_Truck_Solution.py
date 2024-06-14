from Truck_QUBO_1D import Trucking_1D_Problem
from Functions_TruckProblem import get_chosen_containers, get_cumulated_container_length
import numpy as np
import neal
import pandas as pd
import plotly.figure_factory as ff

#Create Problem Instance 
box_lengths = np.random.randint(1,10,5).tolist()
container_length = 10

Trucking_Problem = Trucking_1D_Problem()
Trucking_Problem.gen_problem(box_lengths, container_length)
Final_Q = Trucking_Problem.gen_qubo_matrix()

#Solve QUBO using Simulated Annealing from dwave
sampler = neal.SimulatedAnnealingSampler()
sampleset = sampler.sample_qubo(Final_Q, num_reads = 5000, num_sweeps = 1000)
best_sample = sampleset.first.sample

#Convert activated variables into Chosen Containers
packed_containers = get_chosen_containers(box_lengths,best_sample,container_length)
cumulated_container_lengths = get_cumulated_container_length(packed_containers)

#Create Dataframe
df = pd.DataFrame([
     dict(Task = 'Container', Start = s, Finish = f)for s,f in cumulated_container_lengths
    ])

#Plot Solutions
fig = ff.create_gantt(df,  bar_width = 0.4, show_colorbar=True)
fig.update_layout(xaxis_type='linear', autosize=False, width=800, height=300)
fig.show()