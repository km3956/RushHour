import util
import rushhour
import agent

DEFAULT_STATE = '  b aa|  b   |xxb   |ccc  d|     d|     d'

if __name__ == '__main__':

    cmd = util.get_arg(1)
    if cmd:
        string = util.get_arg(2) or DEFAULT_STATE
        state = rushhour.State(string)
        agent = agent.Agent()

        if cmd == 'random':
            list_states = agent.random_walk(state, 8)
            util.pprint(list_states)

        if cmd == 'bfs':
            list_states, numOfTries = agent.bfs(state)
            print(numOfTries)
        
        if cmd == 'dfs':
            list_states, numOfTries = agent.dfs(state)
            print(numOfTries)

        if cmd == 'a_star':
            list_states, numOfTries = agent.a_star(state)
            print(numOfTries)