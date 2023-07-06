# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
    # To be honest, I am doing this to get a visual perception of problem:
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # from time import sleep
    # sleep(15)

    first_state = problem.getStartState()    # Let's start with a starting node. It is equivalent to S node in the lecture.

    stack = util.Stack()    # Generating our stack as LIFO queue.
    checked = []    # Generating a list for nodes which are already checked.

    # Every block of stack is a singleton dictionary, which contains node name as the key and the chain of successor functions to reach the node as its value.
    first_stack_block = {first_state: []}    # Generating first block.
    stack.push(first_stack_block)    # Pusing it into stack.

    while True:    # Iterating stack, from the last block pushed into it until reaching the goal. This will get time limit error if there is no answer for problem.
        stack_block = stack.pop()    # Bring the block out of stack.
        new_node = list(stack_block.keys())[0]    # Get name of the node. 

        if new_node in checked:    # If this node has been previously checked and it hasn't been the answer, it'll be skipped. 
            pass
        else:
            if problem.isGoalState(new_node):    # Checking whether this node is GOAL or not.
                return stack_block[new_node]    # If yes, the function will return the successor functions needed to reach it from the first node.

            successors = problem.getSuccessors(new_node)    # If this line of code is running, this means the answer has not yet reached. So we check all successor stats related to this node.
            for successor_node in successors:    # Iterating successors stats.
                node_name = successor_node[0]    # According to the format of getSuccessor function return value, the first element is the name of the successor function node.
                new_stack_block = {node_name: stack_block[new_node] + [successor_node[1]]}    # Generating a new block with successor. The key is the name of node and the value is the path to get it.
                stack.push(new_stack_block)    # Adding the new block to the stack.

            checked.append(new_node)    # Appends the checked node to checked nodes list.


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
    # I told you why I am doing this, in dfs section. :)
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # from time import sleep
    # sleep(15)

    first_state = problem.getStartState()

    queue = util.Queue()
    checked = []
    
    queue.push({first_state: []})

    while True:
        queue_block = queue.pop()
        new_node = list(queue_block.keys())[0]

        if new_node not in checked:
            if problem.isGoalState(new_node):
                return queue_block[new_node]

            successors = problem.getSuccessors(new_node)
            for successor in successors:
                queue.push({successor[0]: queue_block[new_node] + [successor[1]]})

            checked.append(new_node)

    #####################################################################################################################################
    #####################################################################################################################################
    ########    Algorithms are very similar, the point is that BFS uses FIFO queue while DFS uses a stack, as a LIFO queue.    ##########
    #####################################################################################################################################
    #####################################################################################################################################

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
