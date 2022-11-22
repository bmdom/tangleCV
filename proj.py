import random
import node
import numpy

def generate_node(node_list):
    if(len(node_list) < 20):
        x_pos = random.randrange(21)
        y_pos = random.randrange(21)
        x_vel = random.randrange(2)
        if x_vel == 0:
            x_vel = -1
        y_vel = random.randrange(2)
        if y_vel == 0:
            y_vel = -1
        temp = node.NodeObj(x_pos, y_pos, x_vel, y_vel)
        node_list.append(temp)

def maintain_list(node_list):
    copy_list = node_list.copy()
    for nodes in copy_list:
        nodes.x_pos += nodes.x_vel
        nodes.y_pos += nodes.y_vel
        if nodes.x_pos < 0 or nodes.x_pos >= 20 or nodes.y_pos < 0 or nodes.y_pos >= 20:
            node_list.remove(nodes)

def main():
    node_list = []

    a = numpy.zeros((20, 20))
    print(numpy.matrix(a))

    for i in range(20):
        generate_node(node_list)
        maintain_list(node_list)

        for nodes in node_list:
            a[nodes.x_pos][nodes.y_pos] = 1

        print(numpy.matrix(a))
        s = input()



if __name__ == '__main__': 
    main()