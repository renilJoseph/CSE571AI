# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        print "*************************************************scores final ", scores

        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        print "chosenIndex***************", chosenIndex
        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]



    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        score = successorGameState.getScore()

        prevFood = currentGameState.getFood()
        newFood = currentGameState.getFood()

        score = 0

        currentPosition = currentGameState.getPacmanPosition()
        currentGhostPoition = currentGameState.getGhostPositions()

        ghostPositions = [ghostState.getPosition() for ghostState in newGhostStates]


        print "currentPacmanPosition", currentPosition
        print "currentGhostPosition", currentGhostPoition
        print "newghostPositions ", ghostPositions
        print "newPacmanpos", newPos

        ghostShortest = ()
        for ghosts in ghostPositions:
            if len(ghostShortest) > 0:
                if ghostShortest[0] > manhattanDistance(newPos, ghosts):
                    ghostShortest = (manhattanDistance(newPos, ghosts), ghosts)
            else:
                ghostShortest = (manhattanDistance(newPos, ghosts), ghosts)


        foodShortDist = ()
        largestFoodDist =0

        width = newFood.width
        height = newFood.height
        i=0
        j=0
        while i < width:
            j=0
            while j < height:
                if prevFood[i][j]:
                    manh = manhattanDistance(newPos, (i, j))
                    if largestFoodDist < manh:
                        largestFoodDist = manh
                    if len(foodShortDist) > 0:
                        if foodShortDist[0] >= manh:
                            foodShortDist = (manh, (i, j))
                    else:
                        foodShortDist = (manh, (i, j))
                j+=1
            i+=1

        i = 0
        j = 0
        latestShortest = -1
        while i < width:
            j = 0
            while j < height:
                if prevFood[i][j]:
                    manh = manhattanDistance(newPos, (i, j))
                    if latestShortest > 0:
                        if latestShortest >= manh:
                            latestShortest = manh
                    else:
                        latestShortest = manh
                j += 1
            i += 1

        # import pdb
        # pdb.set_trace()
        print "latestSHortest", latestShortest
        print "score before editin", score
        # if newScaredTimes[0] >= latestShortest:
        # score = score - latestShortest

        score =score - (foodShortDist[0])

        if ghostShortest[0] <= 2:
            score = score -(largestFoodDist)



        # if len(foodShortDist) <=0:
        #     return score



        print "foodShortDist[0]", foodShortDist[0]
        print "ghostShortest[0]", ghostShortest[0]

        # print("ghostStates", successorGameState.getGhostPosition(currentGameState))
        # print "successorGameState", successorGameState
        print "newPos ", newPos
        # print "newFood ", newFood
        print "newGhostStates ", ghostPositions
        print "foodshortest", foodShortDist[1]
        print "newScaredTimes", newScaredTimes
        print "currentGhostPoition",currentGhostPoition




        "*** YOUR CODE HERE ***"
        # print("***************************************successorGameState.getScore()", score)
        return score

def eucl(pos, goal ):
    xy1 = pos
    xy2 = goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        # *******************************************************8

        def maxValue(gameState, depth, totalAgents):
            # print "num of food remiaing :", noOfFoods
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = -float("inf")
            finalScore = v

            legalPacActions = gameState.getLegalActions(0)
            for eachAction in legalPacActions:
                # print "each action in loop::", eachAction
                v = minValue(gameState.generateSuccessor(0, eachAction), depth, 1, totalAgents)
                if v > finalScore:
                    finalScore = v
                    finalAction = eachAction

            return finalScore

        def minValue(gameState, depth, ghostNumber, totalAgents):
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = float("inf")
            finalScore = v
            legalPacActions = gameState.getLegalActions(ghostNumber)
            for eachAction in legalPacActions:
                if ghostNumber == totalAgents - 1:
                    # print "current ghost :", ghostNumber
                    # print "action in loop ", eachAction
                    # print "depth", depth
                    # print "self.depth", self.depth
                    v = maxValue(gameState.generateSuccessor(ghostNumber, eachAction), depth + 1, totalAgents)
                else:
                    # print "ghostnumber in else", ghostNumber
                    v = minValue(gameState.generateSuccessor(ghostNumber, eachAction), depth, ghostNumber + 1,
                                 totalAgents)
                # print "each action value", v
                if v < finalScore:
                    finalScore = v
                    finalAction = eachAction

            return finalScore


        finalScore = float("-inf")
        v = finalScore
        # print "self. depth", self.depth

        agentsNum = gameState.getNumAgents
        if agentsNum > 0:
            agentsNum
            # print "current food", foods

        possibleActions = gameState.getLegalActions(0)
        # print "******************************"

        for eachAction in possibleActions:

            # depth 1
            v = minValue(gameState.generateSuccessor(0, eachAction), 0, 1, gameState.getNumAgents())

            # print "max value from each actions", v, " for action:", eachAction
            if v > finalScore:
                # print "v in final score check loop", v
                finalScore = v
                finalAction = eachAction
                # print "finalAction", finalAction

            if v<finalScore:
                print "v value", v
                # print "low final score in loop", v

        # print "finalAction", finalAction
        return finalAction

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def maxValue(gameState, depth, totalAgents, alpha, beta):
            # print "num of food remiaing :", noOfFoods
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = -float("inf")
            finalScore = v

            legalPacActions = gameState.getLegalActions(0)
            for eachAction in legalPacActions:
                # print "each action in loop::", eachAction
                v = minValue(gameState.generateSuccessor(0, eachAction), depth, 1, totalAgents, alpha, beta)
                if v > finalScore:
                    finalScore = v
                    finalAction = eachAction

                if finalScore > beta:
                    return finalScore

                if (finalScore > alpha):
                    alpha = v

            return finalScore

        def minValue(gameState, depth, ghostNumber, totalAgents, alpha, beta):
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = float("inf")
            finalScore = v
            legalPacActions = gameState.getLegalActions(ghostNumber)
            for eachAction in legalPacActions:
                if ghostNumber == totalAgents - 1:
                    # print "current ghost :", ghostNumber
                    # print "action in loop ", eachAction
                    # print "depth", depth
                    # print "self.depth", self.depth
                    v = maxValue(gameState.generateSuccessor(ghostNumber, eachAction), depth + 1, totalAgents, alpha, beta)
                else:
                    # print "ghostnumber in else", ghostNumber
                    v = minValue(gameState.generateSuccessor(ghostNumber, eachAction), depth, ghostNumber + 1,
                                 totalAgents, alpha, beta)
                # print "each action value", v
                if v < finalScore:
                    finalScore = v
                    finalAction = eachAction

                if finalScore < alpha:
                    return finalScore

                if (finalScore < beta):
                    beta = finalScore

            return finalScore

        possibleActions = gameState.getLegalActions(0)
        # print "******************************"

        finalScore = float("-inf")
        v = finalScore
        # print "self. depth", self.depth

        alpha = float("-inf")
        beta = float("inf")

        agentsNum = gameState.getNumAgents
        if agentsNum > 0:
            agentsNum
            # print "current food", foods

        for eachAction in possibleActions:

            # depth 1
            v = minValue(gameState.generateSuccessor(0, eachAction), 0, 1, gameState.getNumAgents(), alpha, beta)

            # print "max value from each actions", v, " for action:", eachAction
            if v > finalScore:
                finalScore = v
                finalAction = eachAction
                # print "finalAction", finalAction

            if v >= beta:
                return v

            if(v > alpha):
                alpha = v

            if v < finalScore:
                v
                # print "low final score in loop", v

        # print "finalAction", finalAction
        return finalAction





        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"



        def maxValue(gameState, depth, totalAgents):
            # print "num of food remiaing :", noOfFoods
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = -float("inf")
            finalScore = v

            legalPacActions = gameState.getLegalActions(0)
            lenLegalActions = len(legalPacActions)
            avgScore = 0.0
            for eachAction in legalPacActions:
                # print "each action in loop::", eachAction
                v = expect(gameState.generateSuccessor(0, eachAction), depth, 1, totalAgents)
                avgScore+=v
                if v > finalScore:
                    finalScore = v
                    finalAction = eachAction

            return finalScore
            # return float(avgScore)/float(lenLegalActions)

        def expect(gameState, depth, ghostNumber, totalAgents):
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            # print "value of depth", depth
            # print "gameState", gameState
            v = float("inf")
            finalScore = v
            legalPacActions = gameState.getLegalActions(ghostNumber)
            lenLegalActions = len(legalPacActions)
            avgScore = 0.0
            for eachAction in legalPacActions:
                if ghostNumber == totalAgents - 1:
                    # print "current ghost :", ghostNumber
                    # print "action in loop ", eachAction
                    # print "depth", depth
                    # print "self.depth", self.depth
                    v = maxValue(gameState.generateSuccessor(ghostNumber, eachAction), depth + 1, totalAgents)
                else:
                    # print "ghostnumber in else", ghostNumber
                    v = expect(gameState.generateSuccessor(ghostNumber, eachAction), depth, ghostNumber + 1,
                                 totalAgents)
                # print "each action value", v
                avgScore += v
                if v < finalScore:
                    finalScore = v
                    finalAction = eachAction

            # return finalScore

            return float(avgScore) / float(lenLegalActions)



        finalScore = float("-inf")
        v = finalScore
        # print "self. depth", self.depth

        agentsNum = gameState.getNumAgents
        if agentsNum > 0:
            agentsNum
            # print "current food", foods

        possibleActions = gameState.getLegalActions(0)
        # print "******************************"

        lenLegalActions = len(possibleActions)
        avgScore = 0.0
        for eachAction in possibleActions:

            # depth 1
            v = expect(gameState.generateSuccessor(0, eachAction), 0, 1, gameState.getNumAgents())

            # print "max value from each actions", v, " for action:", eachAction

            if v > finalScore:
                # print "v in final score check loop", v
                finalScore = v
                finalAction = eachAction
                # print "finalAction", finalAction

            if v<finalScore:
                v
                # print "low final score in loop", v

        # print "finalAction", finalAction
        return finalAction


        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"





    ghostPositions = currentGameState.getGhostPositions
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    score = currentGameState.getScore()


    # score = 0

    ghostPositions = [ghostState.getPosition() for ghostState in newGhostStates]

    print "newghostPositions ", ghostPositions

    ghostShortest = ()
    ghostLargest = 0
    for ghosts in ghostPositions:
        if manhattanDistance(newPos, ghosts) > ghostLargest:
            ghostLargest = manhattanDistance(newPos, ghosts)
        if len(ghostShortest) > 0:
            if ghostShortest[0] > manhattanDistance(newPos, ghosts):
                ghostShortest = (manhattanDistance(newPos, ghosts), ghosts)
        else:
            ghostShortest = (manhattanDistance(newPos, ghosts), ghosts)

    foodShortDist = ()
    largestFoodDist = 0

    width = newFood.width
    height = newFood.height
    i = 0
    j = 0
    while i < width:
        j = 0
        while j < height:
            if newFood[i][j]:
                manh = manhattanDistance(newPos, (i, j))
                if largestFoodDist < manh:
                    largestFoodDist = manh
                if len(foodShortDist) > 0:
                    if foodShortDist[0] >= manh:
                        foodShortDist = (manh, (i, j))
                else:
                    foodShortDist = (manh, (i, j))
            j += 1
        i += 1

    print "score before editin", score
    # if newScaredTimes[0] >= latestShortest:
    # score = score - latestShortest

    scaredTimes = newScaredTimes[0]
    if newScaredTimes[0]==0:
        scaredTimes =1

    walls = currentGameState.getWalls()

    # if len(foodShortDist)>0:
    #     if foodShortDist[0] ==1 or foodShortDist[0]==1.0:
    #         scaredTimes = scaredTimes+2


    # if ghostShortest[0] < 2:
    #     score = score - (ghostLargest)
    # else:
    if len(foodShortDist)>0:
        score = score + 4 * float(1.0) / float(foodShortDist[0]) - 0.001*ghostShortest[0]

            # score = score + 1*ghostLargest + 4* float(1.0)/float(foodShortDist[0]) + scaredTimes*5

    # + ghostLargest * newScaredTimes[0]
    # score = score + (1.0 / float(foodShortDist[0])) + max(newScaredTimes)




    # ************************

    if len(ghostShortest)==0:
        ghostShort =1
    else:
        ghostShort=ghostShortest[0]
    #
    # if newScaredTimes[0] > 0:
    #     score = score + ((float(1.0) / float(foodShortDist[0])))*1.5
    #     else:
    #         if ghostShortest[0] < 2:
    #             score = score - ghostShortest[0]
    #         else:

    # if ghostShortest[0] < 2:
    #     score = score - 1
    # else:
    #     if len(foodShortDist) > 0:
    #         score = score + float(1.0) / float(foodShortDist[0]



    # if len(foodShortDist) <=0:
    #     return score

    if len(ghostShortest) >0:
        print "ghostShortest[0]", ghostShortest[0]
        print "ghostShortest[1]", ghostShortest[1]

    print "newPos ", newPos
    print "newGhostStates ", ghostPositions
    if len(foodShortDist)>0:
        print "foodshortest", foodShortDist[1]
        print "foodShortDist[0]", foodShortDist[0]
    print "newScaredTimes", newScaredTimes

    "*** YOUR CODE HERE ***"
    print("***************************************successorGameState.getScore()", score)

    import pdb
    # pdb.set_trace()
    return score

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

