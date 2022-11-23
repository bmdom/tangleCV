import random
import node
import math

def generate_node(node_list, id_counter):
    #To prevent the graph from being overpopulated,
    #Generate nodes with a carrying capacity of 100
    carrying_capacity = 100
    #The range of the graph we will be using is 0 to 100 in both x and y coordinates
    min_range = 100.0
    max_range = 0.0

    if(random.randrange(carrying_capacity) >= len(node_list)):
        #Generate random starting positions around edge of graph
        temp1 = max_range * random.randrange(2)
        temp2 = random.uniform(min_range, max_range)

        #Assign these values randomly to x and y coordinates
        if(random.randrange(2) == 0):
            x_pos = temp1
            y_pos = temp2
        else:
            x_pos = temp2
            y_pos = temp1

        #Generate random velocity vector, and normalize it to its unit vector
        x_vel = random.uniform(0.0, 10.0)
        y_vel = random.uniform(0.0, 10.0)
        norm = math.sqrt(x_vel**2 + y_vel**2)
        x_vel = x_vel / norm
        y_vel = y_vel / norm

        #Generate random c value, with 0 being malicious nodes
        c_val = random.randrange(4)

        #Generate id
        id = id_counter
        id_counter += 1

        #Create node with previous information, and add to list
        temp = node.NodeObj(x_pos, y_pos, x_vel, y_vel, c_val, id)
        node_list.append(temp)

def maintain_list(node_list):
    #Create copy of list to be able to delete items from it
    copy_list = node_list.copy()

    for nodes in copy_list:
        #Increment position values based on velocity
        nodes.x_pos += nodes.x_vel
        nodes.y_pos += nodes.y_vel

        #If the position is outside of the range of the map, delete the node
        if nodes.x_pos < 0.0 or nodes.x_pos > 100.0 or nodes.y_pos < 0.0 or nodes.y_pos > 100.0:
            node_list.remove(nodes)

def distance(node1, node2):
    #Calculates the distance between 2 nodes
    val1 = node1.x_pos - node2.x_pos
    val2 = node1.y_pos - node2.y_pos
    val1 = val1**2
    val2 = val2**2
    return math.sqrt(val1 + val2)

def validate_node(node1, node_list):
    #Validate every active node for our current node
    for node2 in node_list:
        distances = distance(node1, node2)
        
        #If node is outside if range of graph, delete from node1 seen and validated lists
        if node2.x_pos < 0.0 or node2.x_pos > 100.0 or node2.y_pos < 0.0 or node2.y_pos > 100.0:
            node1.seen.remove(node2)
            node1.validated.remove(node2)
        #If they are the same node, continue on
        elif node1 == node2:
            continue
        #If node2 is within the radius of node1, add to seen
        #If node2 is not a malicious node, then add it to validated and update accumulated c value
        elif distances <= node1.sensor_radius:
            if node2 not in node1.seen:
                node1.seen.append(node2)
                if node2.singular_c_value != 0:
                    node1.validated.append(node2)
                    node2.accumulated_c_value += node1.accumulated_c_value
        #If node2 is not within radius of node1 sensor, and just moved outside of its range
        #Remove it from both node1 seen and validated if possible, and update accumulated c value
        else:
            if node2 in node1.seen:
                node1.seen.remove(node2)
                if node2 in node1.validated:
                    node1.validated.remove(node2)
                    node2.accumulated_c_value -= node1.accumulated_c_value


def print_data(node1):
    print("Node")
    print("Position: {", node1.x_pos, ", ", node1.y_pos + "}")
    print("Velocity: {", node1.x_vel, ", ", node1.y_vel + "}")
    print("Singular C Value: ", node1.singular_c_value)
    print("Accumulated C Value: ", node1.accumulated_c_value)
    print("Nodes seen by sensors")
    for node in node1.seen:
        if node in node1.validated:
            print("Position: {", node.x_pos, ", ", node.y_pos + "} Validated")
        else:
            print("Position: {", node.x_pos, ", ", node.y_pos + "}")



def main():
    node_list = []
    id_counter = 0

    generate_node(node_list, id_counter)
    maintain_list(node_list)
    for nodes in node_list:
        validate_node(node, node_list)
    
   



if __name__ == '__main__': 
    main()
