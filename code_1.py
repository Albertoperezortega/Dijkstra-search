# Alberto Perez Ortega 40489659
# Option A


import math
import sys

numbers=[7,2,8,3,2,14,5,7,6,11,2,11,6,14,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0]
numbers_2=[8,2,8,3,2,14,5,7,6,11,2,11,6,14,1,99,99,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1]



def main():
    file_input = sys.argv[1]
    numbers = []
    for i in read_file(file_input):
        num = int(i)
        numbers.append(num)
    caves = {}
    cave_num = numbers[0]
    organize_caves(numbers,cave_num,caves)
    output = Dijkstra_serach(caves, cave_num)
    create_empty_file(file_input, output)

def organize_caves(numbers,cave_num,caves):
    count = 1
    for i in range(cave_num):
        caves[count] = [numbers[(i*2)+1],numbers[(i*2)+2]],find_connections(numbers[cave_num*2+1:],cave_num,count)
        count = count +1
    return caves

def find_connections(links,cave_num,count):
    connected_caves = []
    for i in range(cave_num):
        if links[count+(i*cave_num)-1] == 1:
            connected_caves.append(i+1)
    return connected_caves

def calculate_distance(first, second):
    return ((math.sqrt(((first[0]-second[0])**2)+(first[1]-second[1])**2)))

def Dijkstra_serach(caves, num_caves):
    posibilities = {}
    for i in range(num_caves):
        if (i) == 0:
            posibilities[i+1] = [0,False,1]
        else:
            posibilities[i+1] = [math.inf,False]


    candidates = shortest(posibilities)
    output = []
    while candidates:
        if num_caves in candidates:
            
            distance = (calculate_distance(caves[node][0], caves[num_caves][0]))
            posibilities[num_caves][0] = distance + posibilities[node][0]
            posibilities[num_caves].append(node)
            current_node = num_caves
            while current_node != 1:
                output.append(current_node)
                current_node = posibilities[current_node][2]
            output.append(1)
            output.reverse()
            return output
            
        node = candidates[0]
        posibilities[node][1] = True
        for i in caves[node][1]:
            distance = (calculate_distance(caves[node][0], caves[i][0]))
            if distance < posibilities[i][0]:
                posibilities[i][0] = distance + posibilities[node][0]
                posibilities[i].append(node)
        candidates = shortest(posibilities)
    return 0

def shortest(posibilities):
    min_dist = math.inf
    min_nodes = []
    for key, value in posibilities.items():
        if value[0] < min_dist and value[1] == False:
            min_dist = value[0]
            min_nodes = [key]
        elif value[0] == min_dist and value[0] < math.inf and value[1] == False:
            min_nodes.append(key)
    return min_nodes
        
def read_file(file_input):
    file_path = file_input + ".cav"
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.split(",")
        return(content)



def create_empty_file(file_path, output):
    new_file_name = file_path + ".csn"
    with open(new_file_name, 'w') as f:
        for i in output:
            value = str(i) + " "
            f.write(value)
        pass


main()


