from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


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


def file_2_matrix(filename):
    fr = open(filename)
    number_of_lines = len(fr.readlines())
    return_mat = zeros((number_of_lines,3))
    class_label_vector = []
    fr = open(filename, encoding='utf-8-sig')
    index = 0
    for line in fr.readlines():
        line = line.strip()
        list_from_line = line.split("\t")
        return_mat[index, :] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_label_vector


def auto_norm(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set/tile(ranges, (m, 1))
    return norm_data_set, ranges, min_vals


def plot_the_data(data_set, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_set[:, 0], data_set[:, 1], 15.0*array(labels), 15.0*array(labels))
    plt.show()


def dating_class_test():
    ho_ratio = 0.10
    dating_dat_mat, dating_labels = file_2_matrix('datingTestSet3.txt')
    s_norm_data_set, s_ranges, s_min_val = auto_norm(dating_dat_mat)
    m = s_norm_data_set.shape[0]
    num_test_vecs = int(m*ho_ratio)
    error_count = 0.0
    for i in range(num_test_vecs):
        classifier_result = classify_0(s_norm_data_set[i, :], s_norm_data_set[num_test_vecs:m, :],dating_labels[num_test_vecs:m], 3)
        print("The classifier came back with: %d, the real answer is: %d" % (classifier_result, dating_labels[i]))
        if classifier_result != dating_labels[i]:
            error_count += 1
    print("Total error rate is: %f" % (error_count/float(num_test_vecs)))


def classify_person():
    result_list = ['not at all', 'in_small_doses', 'in_large_doses']
    l_percent_tat = float(input('percent of time spent playing video game?'))
    l_ff_miles = float(input('frequent flier miles earned per year?'))
    l_ice_cream = float(input('liters of ice cream consumed per year?'))
    l_dating_mat, l_dating_labels = file_2_matrix('datingTestSet3.txt')
    l_norm_mat, l_ranges, l_min_vals = auto_norm(l_dating_mat)
    in_array = array([l_ff_miles, l_percent_tat, l_ice_cream])
    classifier_result = classify_0((in_array-l_min_vals)/l_ranges, l_norm_mat, l_dating_labels, 3)
    print("you will probably like this person: ", result_list[classifier_result-1])
