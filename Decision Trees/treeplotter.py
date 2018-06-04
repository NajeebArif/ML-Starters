import matplotlib.pyplot as  plt

g_decision_node = dict(boxstyle="sawtooth", fc="0.8")
g_leaf_node = dict(boxstyle="round4", fc="0.8")
g_arrow_args = dict(arrowstyle="<-")


def create_plot(p_in_tree):
    l_fig = plt.figure(1, facecolor='white')
    l_fig.clf()
    l_ax_props = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **l_ax_props)
    plot_tree.totalW = float(get_num_leafs(p_in_tree))
    plot_tree.totalD = float(get_tree_depth(p_in_tree))
    plot_tree.xOff = -0.5/plot_tree.totalW
    plot_tree.yOff = 1.0
    plot_tree(p_in_tree, (0.5, 1.0), '')
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


def plot_mid_text(p_center_pt, p_parent_pt, p_txt_string):
    l_x_mid = (p_parent_pt[0] - p_center_pt[0])/2.0 + p_center_pt[0]
    l_y_mid = (p_parent_pt[1] - p_center_pt[0])/2.0 + p_center_pt[1]
    create_plot.ax1.text(l_x_mid, l_y_mid, p_txt_string)


def plot_tree(p_my_tree, p_parent_pt, p_node_txt):
    l_num_leafs = get_num_leafs(p_my_tree)
    get_tree_depth(p_my_tree)
    l_first_str = list(p_my_tree.keys())[0]
    l_center_pt = (plot_tree.xOff + (1.0 + float(l_num_leafs))/2.0/plot_tree.totalW, plot_tree.yOff)
    plot_mid_text(l_center_pt, p_parent_pt, p_node_txt)
    plot_node(l_first_str, l_center_pt, p_parent_pt, g_decision_node)
    l_second_dict = p_my_tree[l_first_str]
    plot_tree.yOff = plot_tree.yOff - 1.0/plot_tree.totalD
    for key in l_second_dict.keys():
        if type(l_second_dict[key]).__name__ == 'dict':
            plot_tree(l_second_dict[key], l_center_pt, str(key))
        else:
            plot_tree.xOff = plot_tree.xOff + 1.0/plot_tree.totalW
            plot_node(l_second_dict[key], (plot_tree.xOff, plot_tree.yOff), l_center_pt, g_leaf_node)
            plot_mid_text((plot_tree.xOff, plot_tree.yOff), l_center_pt, str(key))
    plot_tree.yOff = plot_tree.yOff + 1.0/plot_tree.totalD
