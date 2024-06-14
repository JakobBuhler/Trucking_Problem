

def get_chosen_containers(box_lengths, best_sample,container_length):
    chosen_containers = []
    for k in best_sample:
        for i in range(len(box_lengths)):
            if k in range(i * container_length, i*container_length + container_length):
                  if best_sample[k] == 1:
                        chosen_containers.append(box_lengths[i])
    return chosen_containers

def get_cumulated_container_length(packed_containers):
    cumulated_container_lengths = []
    start = 0
    for i in packed_containers:
          start_finish_of_container = [start, start + i]
          cumulated_container_lengths.append(start_finish_of_container)
          start = start_finish_of_container[1]
    return cumulated_container_lengths


def get_objective_value_truck(packed_containers,container_length):
    obj_value= sum(packed_containers)
    if obj_value > container_length:
        obj_value = 0
    return obj_value