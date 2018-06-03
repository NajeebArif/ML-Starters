from numpy import *
import operator
from os import listdir


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


def image_2_vector(filename):
    l_return_vector = zeros((1, 1024))
    l_fr = open(filename)
    for i in range(32):
        l_line_str = l_fr.readline()
        for j in range(32):
            l_return_vector[0, 32*i+j] = int(l_line_str[j])
    return l_return_vector


def handwriting_class_test():
    l_hw_labels = []
    l_training_file_list = listdir('trainingDigits')
    l_m = len(l_training_file_list)
    l_training_mat = zeros((l_m, 1024))
    for i in range(l_m):
        l_file_name_str = l_training_file_list[i]
        l_file_str = l_file_name_str.split('.')[0]
        l_class_num_str = l_file_str.split('_')[0]
        l_hw_labels.append(l_class_num_str)
        l_training_mat[i, :] = image_2_vector('trainingDigits/%s' % l_file_name_str)
    l_test_file_list = listdir('testDigits')
    l_error_count = 0.0
    l_m_test = len(l_test_file_list)
    for i in range(l_m_test):
        l_file_name_str = l_test_file_list[i]
        l_file_str = l_file_name_str.split('.')[0]
        l_class_num_str = l_file_str.split('_')[0]
        l_vector_under_test = image_2_vector('testDigits/%s' % l_file_name_str)
        l_classification_result = classify_0(l_vector_under_test, l_training_mat, l_hw_labels, 3)
        # print('The classifier came back with %s and the real answer is %s.' % (l_classification_result, l_class_num_str))
        if l_classification_result != l_class_num_str:
            l_error_count += 1
    print('Total number of error counts is %d.' % l_error_count)
    print('The total error rate is %f' % (l_error_count/l_m_test))


handwriting_class_test()
