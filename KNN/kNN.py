from numpy import *
import operator


def create_data_set():
    group = array([[1.1, 1.0], [1.0, 1.0], [0.1, 1.0], [0.0, 1.0]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify_0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_dist_indices[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


inp_x = [1, 1.01]
print("Input value which needs to be predicted:(inp_x) ", inp_x)
g, lab = create_data_set()
print("Data set:(features) ", g)
print("Classes: ", lab)
inp_k = 3
v = classify_0(inp_x, g, lab, inp_k)
print("Class for inp_x is: "+v)
