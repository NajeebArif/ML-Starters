import matplotlib.pyplot as  plt

g_decision_node = dict(boxstyle="sawtooth", fc="0.8")
g_leaf_node = dict(boxstyle="round4", fc="0.8")
g_arrow_args = dict(arrowstyle="<-")


def create_plot():
    l_fig = plt.figure(1, facecolor='white')
    l_fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node('a decision node', (0.5, 0.1), (0.1, 0.5), g_decision_node)
    plot_node('a leaf node', (0.8, 0.1), (0.3, 0.8), g_leaf_node)
    plt.show()


def plot_node(p_node_text, p_center_pt, p_parent_pt, p_node_type):
    create_plot.ax1.annotate(p_node_text, xy=p_parent_pt, xycoords='axes fraction',
                             xytext=p_center_pt, textcoords='axes fraction', va='center',
                             ha='center', bbox=p_node_type, arrowprops=g_arrow_args)


def get_num_leafs(p_my_tree):
    l_num_leafs = 0
    l_first_str = list(p_my_tree.keys())[0]
    l_second_dict = p_my_tree[l_first_str]
    for key in l_second_dict.keys():
        if type(l_second_dict[key]).__name__ == 'dict':
            l_num_leafs += get_num_leafs(l_second_dict[key])
        else:
            l_num_leafs += 1
    return l_num_leafs


def get_tree_depth(p_my_tree):
    l_max_depth = 0
    l_first_str = list(p_my_tree.keys())[0]
    l_second_dict = p_my_tree[l_first_str]
    for key in l_second_dict.keys():
        if type(l_second_dict[key]).__name__ == 'dict':
            l_this_depth = 1 + get_tree_depth(l_second_dict[key])
        else:
            l_this_depth = 1
        if l_this_depth > l_max_depth:
            l_max_depth = l_this_depth
    return l_max_depth


def retrieve_tree(i):
    list_of_trees = [{'no surfacing': {0: 'no',
                                       1: {'flippers': {0: 'no', 1: 'yes'}}}
                      },
                     {'no surfacing': {0: 'no',
                                       1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}
                      }]
    return list_of_trees[i]

