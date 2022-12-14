

map1 = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
"""

map2 = """
0 ? ?
0 ? ?
"""

map3 = """
? ? ? ? 0 0 0
? ? ? ? 0 ? ?
? ? ? 0 0 ? ?
? ? ? 0 0 ? ?
0 ? ? ? 0 0 0
0 ? ? ? 0 0 0
0 ? ? ? 0 ? ?
0 0 0 0 0 ? ?
0 0 0 0 0 ? ?
"""




map4 = """
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ?
? ? 0 ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ?
0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ?
0 0 0 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ?
0 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
"""



map5 = """
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? 0 ? ? ?
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 ? ? ? ? ? ? 0
? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ?
? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ?
? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ?
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
"""



map6 = """
? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? 0
? ? ? 0 0 0 ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
? ? ? ? ? 0 ? ? ? ? ? ? 0 0 ? ? ? ? 0 0
0 0 ? ? ? 0 0 ? ? ? ? ? 0 0 ? ? ? ? 0 0
0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? ?
0 0 ? ? ? 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ?
0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ?
0 0 ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 0 0
0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ?
0 0 ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? ? 0 0 ? ? ? ? ? ? 0 ? ?
0 0 0 ? ? ? ? 0 0 0 0 ? ? ? ? ? 0 ? ? ?
0 0 0 ? ? ? ? 0 0 ? ? ? 0 ? ? ? 0 ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? 0 ? ? ?
0 0 ? ? ? 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 ? ? ? 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
"""

map7 = """
0 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? ? ? ?
0 ? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? 0
? ? ? ? 0 0 0 0 0 0
? ? ? 0 0 0 0 0 0 0
"""


map8 = """
0 0 0 0
0 0 0 0
? ? 0 0
? ? ? ?
? ? ? ?
? ? ? ?
? ? 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""




solution_map1 = [["1", "x", "1", "1", "x", "1"],
                 ["2", "2", "2", "1", "2", "2"],
                 ["2", "x", "2", "0", "1", "x"],
                 ["2", "x", "2", "1", "2", "2"],
                 ["1", "1", "1", "1", "x", "1"],
                 ["0", "0", "0", "1", "1", "1"]]




solution_map2 = [["0", "1", "x"],
                ["0", "1", "1"]]


solution_map3 = [["1", "x", "x", "1", "0", "0", "0"],
                ["2", "3", "3", "1", "0", "1", "1"],
                ["1", "x", "1", "0", "0", "1", "x"],
                ["1", "1", "1", "0", "0", "1", "1"],
                ["0", "1", "1", "1", "0", "0", "0"],
                ["0", "1", "x", "1", "0", "0", "0"],
                ["0", "1", "1", "1", "0", "1", "1"],
                ["0", "0", "0", "0", "0", "1", "x"],
                ["0", "0", "0", "0", "0", "1", "1"]]


solution_map4 = [["1", "1", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"],
                ["x", "1", "0", "1", "x", "1", "0", "0", "2", "x", "2", "0", "0", "0", "0", "1", "x", "2", "1"],
                ["1", "1", "0", "2", "3", "3", "1", "1", "3", "x", "2", "0", "0", "0", "0", "1", "2", "x", "1"],
                ["0", "1", "1", "2", "x", "x", "1", "2", "x", "3", "1", "0", "0", "0", "0", "0", "1", "1", "1"],
                ["0", "1", "x", "2", "2", "2", "1", "3", "x", "3", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "1", "1", "1", "0", "0", "0", "2", "x", "2", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "2", "2", "1", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "x", "x", "1", "0", "0", "0", "0", "0"],
                ["0", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "2", "2", "1", "0", "0", "0", "0", "0"],
                ["0", "0", "1", "x", "2", "1", "3", "x", "2", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0"],
                ["0", "0", "1", "1", "2", "x", "3", "x", "3", "1", "1", "0", "0", "0", "0", "1", "x", "1", "0"],
                ["0", "0", "0", "0", "1", "2", "3", "2", "2", "x", "1", "0", "0", "0", "0", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0", "1", "x", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"],
                ["0", "0", "1", "1", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "x", "1"],
                ["0", "0", "1", "x", "2", "x", "2", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"],
                ["0", "0", "1", "1", "2", "1", "3", "x", "3", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1"],
                ["0", "0", "0", "0", "0", "0", "2", "x", "x", "1", "0", "0", "0", "1", "1", "1", "0", "1", "x"],
                ["0", "0", "0", "1", "1", "1", "1", "2", "2", "1", "0", "0", "0", "1", "x", "1", "1", "2", "2"],
                ["0", "0", "0", "1", "x", "3", "2", "1", "0", "0", "0", "1", "1", "2", "1", "1", "1", "x", "2"],
                ["0", "0", "0", "1", "2", "x", "x", "1", "0", "0", "0", "1", "x", "1", "0", "1", "2", "3", "x"],
                ["0", "0", "0", "0", "1", "2", "2", "1", "1", "1", "1", "1", "1", "1", "0", "1", "x", "3", "2"],
                ["0", "0", "0", "0", "1", "1", "1", "1", "2", "x", "1", "1", "1", "1", "0", "2", "3", "x", "2"],
                ["0", "0", "0", "0", "1", "x", "1", "1", "x", "2", "1", "1", "x", "1", "0", "1", "x", "3", "x"]]


solution_map5 = [["0", "0", "0", "0", "0", "0", "0", "0", "1", "x", "x" ,"2" ,"1", "0", "1", "x", "1", "0", "1" ,"2", "x"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "1", "2", "3" ,"x" ,"1", "0", "2", "2", "2", "1", "2" ,"x", "2"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "2" ,"2" ,"2", "0", "1", "x", "1", "1", "x" ,"2", "1"],
                 ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "1" ,"x" ,"1", "0", "1", "2", "2", "2", "1" ,"1", "0"],
                 ["1", "1", "0", "0", "0", "1", "x", "1", "0", "1", "2" ,"2" ,"1", "0", "0", "1", "x", "1", "1" ,"1", "1"],
                 ["x", "1", "0", "0", "0", "1", "1", "1", "0", "1", "x" ,"1" ,"0", "0", "0", "1", "1", "1", "1" ,"x", "1"],
                 ["2", "2", "1", "0", "0", "0", "0", "0", "0", "1", "1" ,"1" ,"0", "0", "0", "0", "0", "0", "1" ,"1", "1"],
                 ["1", "x", "1", "0", "0", "0", "0", "0", "0", "0", "1" ,"2" ,"2", "1", "0", "0", "1", "1", "1" ,"0", "0"],
                 ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1" ,"x" ,"x", "1", "0", "0", "1", "x", "1" ,"0", "0"]]



solution_map6 = [   ["1", "1", "1", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0" ,"0", "1", "x", "1", "0"],
                    ["1", "x", "1", "0", "0", "0", "1", "x", "1", "1", "1", "1", "0", "0", "0" ,"0", "1", "1", "1", "0"],
                    ["1", "1", "2", "1", "1", "0", "1", "1", "1", "1", "x", "1", "0", "0", "1" ,"2", "2", "1", "0", "0"],
                    ["0", "0", "2", "x", "2", "0", "0", "1", "1", "2", "1", "1", "0", "0", "1" ,"x", "x", "1", "0", "0"],
                    ["0", "0", "2", "x", "2", "0", "0", "1", "x", "1", "0", "0", "0", "0", "1" ,"2", "2", "2", "1", "1"],
                    ["0", "0", "2", "2", "2", "0", "0", "1", "1", "1", "0", "0", "0", "1", "1" ,"1", "1", "2", "x", "1"],
                    ["0", "0", "1", "x", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "x" ,"1", "2", "x", "3", "1"],
                    ["0", "0", "1", "1", "1", "0", "1", "2", "2", "1", "0", "0", "0", "1", "1" ,"1", "2", "x", "2", "0"],
                    ["0", "0", "1", "2", "2", "1", "1", "x", "x", "2", "1", "1", "0", "1", "1" ,"1", "1", "1", "1", "0"],
                    ["0", "0", "1", "x", "x", "1", "1", "2", "2", "2", "x", "1", "0", "1", "x" ,"1", "0", "0", "0", "0"],
                    ["0", "0", "1", "2", "2", "1", "0", "0", "0", "1", "1", "1", "0", "1", "1" ,"1", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ,"0", "1", "2", "2", "1"],
                    ["0", "0", "1", "1", "2", "1", "1", "0", "0", "0", "0", "0", "1", "1", "2" ,"1", "2", "x", "x", "3"],
                    ["0", "0", "1", "x", "2", "x", "2", "1", "1", "0", "0", "0", "1", "x", "3" ,"x", "3", "3", "x", "x"],
                    ["0", "0", "1", "1", "3", "2", "3", "x", "1", "0", "0", "1", "2", "2", "3" ,"x", "2", "1", "3", "3"],
                    ["0", "0", "0", "1", "2", "x", "2", "1", "1", "0", "0", "1", "x", "1", "1" ,"1", "1", "0", "1", "x"],
                    ["0", "0", "0", "1", "x", "3", "2", "0", "0", "0", "0", "1", "1", "2", "1" ,"1", "0", "1", "3", "3"],
                    ["0", "0", "0", "1", "2", "x", "1", "0", "0", "1", "1", "1", "0", "1", "x" ,"1", "0", "1", "x", "x"],
                    ["0", "0", "0", "0", "1", "1", "2", "1", "1", "1", "x", "1", "0", "1", "1" ,"1", "0", "2", "3", "3"],
                    ["0", "0", "1", "1", "1", "0", "1", "x", "1", "1", "1", "1", "0", "0", "0" ,"0", "0", "1", "x", "1"],
                    ["0", "0", "1", "x", "1", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0" ,"0", "0", "1", "1", "1"]]

solution_map7 = [   ["0", "0", "0", "0", "1", "1", "1", "1", "1", "1"],
                    ["0", "0", "0", "1", "2", "x", "2", "2", "x", "1"],
                    ["0", "1", "1", "2", "x", "2", "2", "x", "2", "1"],
                    ["1", "2", "x", "2", "1", "1", "1", "1", "1", "0"],
                    ["1", "x", "2", "1", "0", "0", "0", "0", "0", "0"],
                    ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"]]



solution_map8 = [["0", "0", "0", "0"],
                ["0", "0", "0", "0"],
                ["1", "1", "0", "0"],
                ["x", "2", "1", "1"],
                ["x", "3", "1", "x"],
                ["x", "2", "1", "1"],
                ["1", "1", "0", "0"],
                ["0", "0", "0", "0"],
                ["0", "0", "0", "0"],
                ["0", "0", "0", "0"]]




# 1 = 6
# 2 = 1
# 3 = 6
# 4 = 43
# 5 = 18
# 6 = 42
# 7 = 6
# 8 = 4

num_of_bombs = 18

map = map5.strip()

def open(y,x):
    return solution_map5[y][x]




#from preloaded import open

def solve_mine(map, n):

#########################################################################################################

    # A node class that represents each entry/item of the game.
    class node():
        def __init__(self, kolonne, rad, value):
            self.cordinates = (rad, kolonne)
            self.rad = rad
            self.kolonne = kolonne
            self.value = value
            self.adj_list = []
            self.connected_unknowns = 0
            self.connected_bombs = 0

            # These variables are used for the list gathering of the multi evaluation recursive test.
            # They are returned to default values after the test.        
            self.part_of_cluster = False
            self.previous = None
            self.next = None
            # These variables belong are used during the recursive test.
            # After the test they are returned to their default values.
            self.short_adj_list = []
            self.connected_Tbombs = 0
            self.attached_Tbomb = False
            self.max_Tbombs = False
            self.initial_Tbombs_to_place = 0
            self.Tbombs_to_place = 0


    # A class that contains the game board information.
    class game_board():
        def __init__(self, map, bombs):
            self.string_map = map
            self.total_bombs = bombs
            self.node_map = []
            self.any_zero = False
        
        
        
        def only_bombs_left(self):
            count_unknown = 0
            
            for row in self.node_map:
                    for item in row:
                        if str(item.value) == "?":
                            count_unknown += 1
            if self.total_bombs - count_unknown == 0:
                for row in self.node_map:
                    for item in row:
                        if str(item.value) == "?":
                            item.value = "x"
                
            

        def open_node(self, target):
            answer = open(target.rad, target.kolonne)
            #print(f"Opening row: {target.rad} and column: {target.kolonne}")
            if answer == "x":
                print(f"There is a bomb at row: {target.rad} and column: {target.kolonne}")

            #return open(target.rad, target.kolonne)
            return answer

                
        def are_all_bombs_accounted_for(self):
            if self.total_bombs == 0:
                for row in self.node_map:
                    for item in row:
                        if str(item.value) == "?":
                            item.value = open(item.rad, item.kolonne)
                return True
            return False


        
        # Reads all the values from the map into Nodes part of a nested list. 
        def node_map_creator(self):
            lstA = self.string_map.split("\n")
            lstB = [x.split(" ") for x in lstA]
            help_list = []
            for r, row in enumerate(lstB):
                for c, value in enumerate(row):
                    help_list.append(node(c,r, value))
                self.node_map.append(help_list)
                help_list = []
        

        # Adds all adjacent nodes into the current nodes adj_list.
        # This is done in a clockwise fashion, starting with the one directly above.
        def adj_list_populator(self):
            for i, row in enumerate(self.node_map):
                for j, item in enumerate(self.node_map[i]):
                    adj_list_order = [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1)]
                    for direction in adj_list_order:
                        if direction[0] >= 0 and direction[1] >= 0:
                            try:
                                item.adj_list.append(self.node_map[direction[0]][direction[1]])
                            except:
                                pass


        # This function opens all nodes connected to a value 0 node.
        def open_connected_to_zero(self):
            for row in self.node_map:
                for item in row:
                    if str(item.value) == "0":
                        self.any_zero = True
                        for connection in item.adj_list:
                            connection.value = self.open_node(connection)


        # Sets the number of connected bombs and unknowns to each node.
        def set_num_of_conections_to_bombs_and_unknowns(self):
            for row in self.node_map:
                for item in row:
                    for conection in item.adj_list:
                        if str(conection.value) == "x":
                            item.connected_bombs += 1
                        if str(conection.value) == "?":
                            item.connected_unknowns += 1


        # This function flags all nodes that definitely have a bomb, as a bomb.
        # If it made any changes to the node_map, it will return True
        def flag_only_bomb_connections(self):
            change = False
            for row in self.node_map:
                for item in row:
                    if str(item.connected_unknowns + item.connected_bombs) == str(item.value):
                        #print(f"The item: {item.cordinates}")
                        #print(item.value)
                        for connection in item.adj_list:
                            if str(connection.value) == "?":
                                connection.value = "x"
                                self.total_bombs -= 1
                                change = True
                                for next_to in connection.adj_list:
                                    next_to.connected_unknowns -= 1
                                    next_to.connected_bombs += 1
            return change


        # This function opens new ? nodes that connect to a node with numerical value with confirmed bomb 
        # connections that equal to the node value. If it made any changes to the node_map, it will return True
        def open_safe_connections(self):
            change = False
            for row in self.node_map:
                for item in row:            
                    if str(item.connected_bombs) == str(item.value):
                        for connection in item.adj_list:
                            if str(connection.value) == "?":
                                connection.value = self.open_node(connection)
                                #print(f"Opened node at: {connection.cordinates[0]}, {connection.cordinates[1]}")
                                change = True
                                for next_to in connection.adj_list:
                                    next_to.connected_unknowns -= 1
            return change


        # This method calls the two previous methods for opening nodes and placing bomb flags. 
        # It will call these methods until they can no longer yield any results.
        def assert_bombs_open_safe_and_repeat(self):
            while True:
                new_round = self.open_safe_connections()
                if new_round == False:
                    new_round = self.flag_only_bomb_connections()
                    if new_round == False:
                        break


        def print_map(self): # Used for development purpuses
            printable_node_list = []
            row_list = []
            for row in self.node_map:
                for item in row:
                    row_list.append(item.value)
                printable_node_list.append(row_list)
                row_list = []
            for row in printable_node_list:
                print(row)
        

        def solved_map(self):
            map_string = "\n"

            for row in self.node_map:
                for i, item in enumerate(row):
                    if i+1 == len(row):
                        map_string = map_string + str(item.value) + "\n"
                    else:
                        map_string = map_string + str(item.value) + " "
            map_string = map_string + "\n"

            return map_string
        


####################################################################################################

    class Seed_point_groups:
        def __init__(self, node_map):
            self.node_map = node_map
            self.seed_point_groups = []


        def find_all_unconected_seed_points(self):
            for row in self.node_map:
                for item in row:
                    if str(item.value) == "?":
                        if len(self.seed_point_groups) > 0:
                            item_cordinates_part_of_a_existing_group = False
                            for dictionary in self.seed_point_groups:
                                if item.cordinates in dictionary:
                                    item_cordinates_part_of_a_existing_group = True
                            if item_cordinates_part_of_a_existing_group == False:                                    
                                seed_point_group = {}
                                seed_point_group = self.expand_seed_point_group(item, seed_point_group)
                                self.seed_point_groups.append(seed_point_group)
                        else:
                            #print("First seed point group")
                            seed_point_group = {}
                            seed_point_group = self.expand_seed_point_group(item, seed_point_group)
                            self.seed_point_groups.append(seed_point_group)


        def expand_seed_point_group(self, start, seed_point_group):
            for connected in start.adj_list:
                if str(connected.value) == "?":
                    if connected.cordinates not in seed_point_group:
                        seed_point_group[connected.cordinates] = connected
                        self.expand_seed_point_group(connected, seed_point_group)
            return seed_point_group



    class GroupTest():
        def __init__(self, node_list, target_group, remaining_bombs):
            self.node_map = node_list
            self.remaining_bombs = remaining_bombs          
            self.target_group = target_group
            self.border_group = {}
            self.border_list = []
            self.solutions = []

        
        def establish_border_group(self):
            for item in self.target_group:
                for connected in self.target_group[item].adj_list:
                    if str(connected.value) in ["1", "2", "3", "4", "5", "6"]: #, "7", "8"]: ##### Ved å redusere antal som blir testet på så vil kodens kjøretid bli bedre
                        self.border_group[connected.cordinates] = connected
        
        def make_dicts_to_lists(self):
            # for item in self.target_group:
            #     self.target_list.append(self.target_group[item])            
            for item in self.border_group:
                self.border_list.append(self.border_group[item])

        def create_short_adj_list(self):
            # The short_adj_list for the cluster list
            for item in self.border_list:
                for connected in item.adj_list:
                    if connected.cordinates in self.target_group:
                        item.short_adj_list.append(connected)
            # The short_adj_list for the cluster list
            for item in self.target_group:
                for connected in self.target_group[item].adj_list:
                    if connected.cordinates in self.border_group:
                        self.target_group[item].short_adj_list.append(connected)


        def next_pointer_for_border_list(self):
            for i, item in enumerate(self.border_list):
                if i < len(self.border_list) - 1:
                    item.next = self.border_list[i + 1]


        

        def print_groups(self):
            print("Target Group")
            for item in self.target_group:
                print(item)

            print("Border Group")
            for item in self.border_group:
                print(item)
            print(" ")


        def create_border_and_target_lists(self):
            self.establish_border_group()
            self.make_dicts_to_lists()
            self.create_short_adj_list()
            self.next_pointer_for_border_list()

            #self.print_groups() # Gir rette verdier.
        


        def solve_puzzle(self):
            self.bomb_plaser(self.border_list[0])
        
                
        def bomb_plaser(self, bomber_node): # recurcive function...
            bomb_placed = False            
            for target in bomber_node.short_adj_list:   
                #print(f" The next of the bomber: {bomber_node.next}")
                if int(bomber_node.value) - int(bomber_node.connected_bombs) - int(bomber_node.connected_Tbombs) > 0:
                    if self.can_bomb_be_placed_here(target) == True:
                        #print(f"Bomb placed at: {target.rad}, {target.kolonne}, from {bomber_node.rad}, {bomber_node.kolonne}, rem bombs {self.remaining_bombs}")
                        self.place_bomb_here(target)
                        bomb_placed = True
                        self.check_bomb_solution()
                # if int(bomber_node.value) - int(bomber_node.connected_bombs) - int(bomber_node.connected_Tbombs) > 0:
                #     self.bomb_plaser(bomber_node)
                if bomber_node.next != None:
                    #print("The next rec call")
                    self.bomb_plaser(bomber_node.next) # Neste recusive runde.                
                if bomb_placed == True:
                    bomb_placed = False
                    self.remove_placed_bomb(target)
                    #print(f"Bomb removed at: {target.rad}, {target.kolonne}, from {bomber_node.rad}, {bomber_node.kolonne}")
            return

        # def refactor_solutions(self):
        #     for solution_list in self.solutions:
        #         for solution in solution_list:

        def check_total_solution(self, game_map):
            
            for solution_list in self.solutions:
                print("")
                for solution in solution_list:
                    print(f"The solution: [{solution.rad}, {solution.kolonne}]", end = " - ")
                print(f"Number of bombs left: {game_map.total_bombs}")
            

            for solution_list in self.solutions:
                    if len(solution_list) == game_map.total_bombs:
                        self.solutions = []
                        self.solutions.append(solution_list)


            if len(self.solutions) == 1:
                for solution_list in self.solutions:
                    for solution in solution_list:
                        game_map.node_map[solution.rad][solution.kolonne].value = "x"
                        game_map.total_bombs -=1
                        for connected in game_map.node_map[solution.rad][solution.kolonne].adj_list:
                            connected.connected_bombs += 1
                            connected.connected_unknowns -=1

                return True
            else:
                return False
        
        
        def check_bomb_solution(self):

            # Testes all the border nodes if that have their required bombs.
            for item in self.border_list:
                if item.max_Tbombs == False:
                    return False
            
            # #Thests that all nodes in the target group has at least one connected bomb.
            for item in self.target_group:
                if self.target_group[item].connected_Tbombs == 0:
                    if self.target_group[item].connected_bombs == 0:
                        if self.target_group[item].attached_Tbomb == False:
                            return False
            
            solution = self.find_nodes_with_test_bombs()

            if solution not in self.solutions:
                self.solutions.append(solution)

        
        def find_nodes_with_test_bombs(self):
            nodes_with_test_bombs = []
            for item in self.target_group:
                if self.target_group[item].attached_Tbomb == True:
                    nodes_with_test_bombs.append(self.target_group[item])
            return nodes_with_test_bombs

        
        def remove_placed_bomb(self, target):
            target.attached_Tbomb = False
            self.remaining_bombs +=1
            for connected in target.adj_list:
                connected.connected_Tbombs -= 1
                if str(connected.value) != "?" and str(connected.value) != "x":
                    if int(connected.connected_bombs) + int(connected.connected_Tbombs) < int(connected.value):
                        connected.max_Tbombs = False


        def place_bomb_here(self, target):
            target.attached_Tbomb = True
            self.remaining_bombs -=1
            for connected in target.adj_list:
                connected.connected_Tbombs += 1
                if str(connected.value) != "?" and str(connected.value) != "x":
                    if int(connected.connected_bombs + connected.connected_Tbombs) == int(connected.value):
                        connected.max_Tbombs = True

                # if connected.connected_bombs + connected.connected_Tbombs > int(connected.value): # Dev tests
                #     print("WARNING")
                #     print(f"To many bombs at: {connected.rad}, {connected.kolonne}")
                #     print(f"Normal bombs: {connected.connected_bombs}, Tbombs: {connected.connected_Tbombs}, Value: {connected.value}")
            

        def can_bomb_be_placed_here(self, target):
            if self.remaining_bombs == 0:
                return False
            if target.attached_Tbomb == True:
                return False
            for connected in target.short_adj_list:
                if connected.max_Tbombs == True:
                    return False
            return True
            
        
        def reset_node_variables(self, the_node_map): # Her er det mulighet for forbedringer når det kommer til kjøretid.
            for row in the_node_map:
                for item in row:
                    item.part_of_cluster = False
                    item.previous = None
                    item.next = None
                    item.short_adj_list = []
                    item.connected_Tbombs = 0
                    item.attached_Tbomb = False
                    item.max_Tbombs = False
                    item.initial_Tbombs_to_place = 0
                    item.Tbombs_to_place = 0
            
            

    # Setup game board
    print(f"The number of bombs: {n}")
    my_game_board = game_board(map, n)
    my_game_board.node_map_creator()

    # Handles 1 lenght boards.
    if len(my_game_board.node_map) == 1 and n == 0:
        return "0"
    # Handles 1 lenght boards.
    if len(my_game_board.node_map) == 1 and n == 1:
        return "x"

    my_game_board.adj_list_populator()
    my_game_board.open_connected_to_zero()
    
    if my_game_board.any_zero == False:
        return "?"
    
    my_game_board.set_num_of_conections_to_bombs_and_unknowns()

    #my_game_board.print_map()
    

    for num in range(1):
        # Opens all the easy nodes and flags all the easy bombs.

        my_game_board.assert_bombs_open_safe_and_repeat()
        #print(f"Number of bombs left: {my_game_board.total_bombs}")
        
        print(my_game_board.solved_map().strip())

        #my_game_board.print_map() # Denne er bare for feilsøking
        print("")

        #print("Board after flag and open.")
        #my_game_board.print_map()

        
        ### Special edge case
        
        my_game_board.only_bombs_left()
        my_game_board.are_all_bombs_accounted_for()  # usikker på denne...
        
        
        seed_points_1 = Seed_point_groups(my_game_board.node_map)
        seed_points_1.find_all_unconected_seed_points()
        
        
        

        
        lenght_compensator = 1

        for num in range(len(seed_points_1.seed_point_groups)):
            #print(f"ROUND {num}")

            remaining_bombs = my_game_board.total_bombs - len(seed_points_1.seed_point_groups) + lenght_compensator

            #print(f"Remaining bombs: {remaining_bombs}")           

            group_test_1 = GroupTest(my_game_board.node_map, seed_points_1.seed_point_groups[num], remaining_bombs)
            group_test_1.create_border_and_target_lists()
            group_test_1.solve_puzzle()
            if group_test_1.check_total_solution(my_game_board) == True:
                lenght_compensator += 1

            my_game_board.assert_bombs_open_safe_and_repeat()
            print("")
            print(my_game_board.solved_map().strip())
            #my_game_board.print_map()
            
            my_game_board.are_all_bombs_accounted_for() # usikker på denne...

        

        if my_game_board.total_bombs != 0:
            return "?"
        
        else:
            return my_game_board.solved_map().strip()



print(solve_mine(map, num_of_bombs))