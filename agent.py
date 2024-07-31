import random
import util
import rushhour

class Node:
    def __init__(self, state, parent=None, value=0):
        self.state = state
        self.parent = parent
        self.value = value
    
    def getPath(self):
        node_ = self
        list_states = []
        while node_ is not None:
            list_states.insert(0, node_.state)
            node_ = node_.parent
        return list_states

class Agent:

    def random_walk(self, state, n):
        parent_state = Node(state)
        for i in range(n-1):
            list_possible_actions = parent_state.state.actions()
            index_ = random.randint(0, len(list_possible_actions)-1)
            action_taken = list_possible_actions[index_]
            child_state = parent_state.state.execute(action_taken)
            node_ = Node(child_state, parent_state)
            parent_state = node_

        return node_.getPath()
    
    def _in_list(self ,list_, node):
        for i in list_:
            if str(i.state) == str(node.state):
                return True
        return False
    
    def manhattan_distance_heuristic(self, current_state):
        exit_x = current_state.SIZE - 1
        exit_y = current_state.EXIT_Y
        goal_x, goal_y = None, None

        for y in range(current_state.SIZE):
            for x in range(current_state.SIZE):
                if current_state.get(x, y) == 'x':
                    goal_x, goal_y = x, y
                    break
                
        if goal_x is None or goal_y is None:
            return float('inf')
        else:
            return abs(exit_x - goal_x) + abs(exit_y - goal_y)
    
    def _sort_list_nodes(self, node_list):
        node_list.sort(key=lambda node: node.value)
        return node_list

    def _search(self, type, state):
        open = [Node(state, value=self.manhattan_distance_heuristic(state))]
        closed = []
        #Counter is 1 as the first state is already in the open list
        counter = 1
        while open:
            if type == 'bfs':
                current_node = open.pop(0)
            elif type == 'dfs':
                current_node = open.pop()
            elif type == 'a_star':
                self._sort_list_nodes(open)
                current_node = open.pop(0)

            util.pprint(current_node.getPath())
            if current_node.state.is_goal():
                return current_node.getPath(), counter    
            if not self._in_list(closed, current_node):
                closed.append(current_node)
                action_options  = current_node.state.actions()
                for i in action_options:
                    child_state = current_node.state.execute(i)
                    node_ = Node(child_state, current_node, self.manhattan_distance_heuristic(child_state))
                    open.append(node_)
                counter += 1
        return None, counter
    
    def bfs(self, state):
        return self._search('bfs', state)

    def dfs(self, state):
        return self._search('dfs', state)
    
    def a_star(self, state):
        return self._search('a_star', state)