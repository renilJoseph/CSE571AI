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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack();
    visited=[]
    stack.push([problem.getStartState(),[''], 1]);

    currentState = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "succccccccc",problem.getSuccessors(problem.getStartState())

    while not stack.isEmpty():
        import pdb
        # pdb.set_trace()

        currentState = stack.pop()
        # print "currentState  after pop",currentState
        
        if problem.isGoalState(currentState[0]):
            return currentState[1][1:]

        # print "currentState********", currentState, "asd"
        currentStatePath = currentState[1]
        if currentState[0] not in visited:
            visited.append(currentState[0])
            # print "currentState in not visited", currentState
            # print "visited after appending", visited          
            succ = problem.getSuccessors(currentState[0])
            for sucEach in (succ):
                currentStatePath = [e for e in currentState[1]]
                if sucEach[0] not in visited:  
                    # if problem.isGoalState(sucEach[0]):
                    #     currentState[1].append(sucEach[1])
                    #     return currentState[1][1:]
                    currentStatePath.append(sucEach[1])
                    l=[]
                    l.append(sucEach[0])
                    l.append(currentStatePath)
                    # l.append(sucEach[2])
                    # print "l*********",l
                    # print "currentStatePath before pushing", currentStatePath         
                    stack.push(l)
                   
        # print " current**",currentState    
        # print "succ********", succ
        # print "visited***", visited
  
    
    print "currentState",currentState[1][1:]
    return  []
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    stack = util.Queue();
    visited=[]
    stack.push([problem.getStartState(),[''], 1]);

    currentState = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "succccccccc",problem.getSuccessors(problem.getStartState())

    print "****************************************************************"
    while not stack.isEmpty():
        import pdb
        # pdb.set_trace()

        currentState = stack.pop()
        # print "currentState  after pop",currentState
        
        if problem.isGoalState(currentState[0]):
            # print "******************************************returning"
            return currentState[1][1:]

        # print "currentState********", currentState
        currentStatePath = currentState[1]
        if currentState[0] not in visited:
            visited.append(currentState[0])
            # print "currentState in not visited", currentState
            # print "visited after appending", visited          
            succ = problem.getSuccessors(currentState[0])
            for sucEach in (succ):
                currentStatePath = [e for e in currentState[1]]
                if sucEach[0] not in visited:  
                    # print "successor not in visited", sucEach
                    # if problem.isGoalState(sucEach[0]):
                    #     currentState[1].append(sucEach[1])
                    #     return currentState[1][1:]
                    currentStatePath.append(sucEach[1])
                    l=[]
                    l.append(sucEach[0])
                    l.append(currentStatePath)
                    # l.append(sucEach[2])
                    # print "l*********",l
                    # print " before pushing", l         
                    stack.push(l)
                   
        # print " current**",currentState    
        # print "succ********", succ
        # print "visited***", visited
  
    print "is stack is isEmpty******************************", stack.isEmpty()
    print "currentState",currentState[1][1:]
    return  []


    # util.raiseNotDefined()
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    stack = util.PriorityQueue();
    visited=[]
    stack.update([problem.getStartState(),[''], 1], 1);

    currentState = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "succccccccc",problem.getSuccessors(problem.getStartState())

    while not stack.isEmpty():
        import pdb
        # pdb.set_trace()

        currentState = stack.pop()
        # print "currentState  after pop",currentState
        
        if problem.isGoalState(currentState[0]):
            return currentState[1][1:]

        # print "currentState********", currentState, "asd"
        currentStatePath = currentState[1]
        if currentState[0] not in visited:
            visited.append(currentState[0])
            # print "currentState in not visited", currentState
            # print "visited after appending", visited          
            succ = problem.getSuccessors(currentState[0])
            for sucEach in (succ):
                currentStatePath = [e for e in currentState[1]]
                if sucEach[0] not in visited:  
                    currentStatePath.append(sucEach[1])
                    l=[]
                    l.append(sucEach[0])
                    l.append(currentStatePath)
                    l.append(sucEach[2]+currentState[2])
                    # print "l*********",l
                    # print "currentStatePath before pushing", currentStatePath         
                    stack.update(l, sucEach[2]+currentState[2])
                   
        # print " current**",currentState    
        # print "succ********", succ
        # print "visited***", visited
  
    
    print "currentState",currentState[1][1:]
    return  []



    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # print heuristic(problem)
    def priorityFunction(item):
        return item[2]+heuristic(item[0],problem)

    stack = util.PriorityQueueWithFunction(priorityFunction);
    visited=[]
    stack.push([problem.getStartState(),[''], 0]);
    fringelist=[]
    fringelist.append([problem.getStartState(),[''], 0])

    currentState = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "succccccccc",problem.getSuccessors(problem.getStartState())

    while not stack.isEmpty():
        import pdb
        # pdb.set_trace()

        currentState = stack.pop()
        # print "currentState", currentState
        # print "currentState  after pop",currentState
        
        if problem.isGoalState(currentState[0]):
            return currentState[1][1:]

        # print "currentState********", currentState, "asd"
        currentStatePath = currentState[1]
        if currentState[0] not in visited:
            # print "currentState not in visited", currentState
            visited.append(currentState[0])
            # print "currentState in not visited", currentState
            # print "visited after appending", visited          
            succ = problem.getSuccessors(currentState[0])
            # print "successors", succ
            for sucEach in (succ):
                currentStatePath = [e for e in currentState[1]]
                if sucEach[0] not in visited:
                    breakLoop = False
                    for fringeElm in fringelist:
                        if fringeElm[0] == sucEach[0] and fringeElm[2]< (sucEach[2]+currentState[2]+ heuristic(sucEach[0],problem)):
                            # print "inside continue ,visitedElm ", fringeElm ,"and sucEach[2]+currentState[2]+ nullHeuristic(problem)", sucEach[2]+currentState[2]+ nullHeuristic(problem)                            
                            breakLoop = True   
                    if breakLoop:
                        continue        
                    # print "adding sucEach[0] to stack", sucEach
                    currentStatePath.append(sucEach[1])
                    l=[]
                    l.append(sucEach[0])
                    l.append(currentStatePath)
                    l.append(sucEach[2]+currentState[2])
                    fringelist.append(l)
                    # print "pushing " , l
                    # print "l*********",l
                    # print "currentStatePath before pushing", currentStatePath         
                    stack.push(l)
                   
        # print " current**",currentState    
        # print "succ********", succ
        # print "visited***", visited
  
    
    print "currentState",currentState[1][1:]
    return  []

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
