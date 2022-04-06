import math
import numpy

ballX = 4
ballY = 4

robotX = 0
robotY = 0
robotTheta = 0

angleDotProductScalingPower = 1

kPTurn = 10
kPMove = 0.08

timeStep = 0.001

currentTime = 0

def getDist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def getMovementSpeed():
    angleDotProduct = math.cos(robotTheta)*((ballX-robotX)/(math.sqrt(math.pow(ballX-robotX, 2) + math.pow(ballY-robotY, 2)))) + math.sin(robotTheta)*((ballY-robotY)/(math.sqrt(math.pow(ballX-robotX, 2) + math.pow(ballY-robotY, 2))))
    return math.pow(angleDotProduct, angleDotProductScalingPower)*kPMove*getDist(robotX, robotY, ballX, ballY)

def getXMovement():
    return getMovementSpeed()*math.cos(robotTheta)

def getYMovement():
    return getMovementSpeed()*math.sin(robotTheta)

def getThetaMovement():
    return kPTurn*(math.atan2(ballX-robotX, ballY-robotY) - robotTheta)

for x in range (0, 1000000):
    robotThetaChange = getThetaMovement()*timeStep
    robotXChange = getXMovement()*timeStep
    robotYChange = getYMovement()*timeStep
    robotTheta += robotThetaChange
    robotX += robotXChange
    robotY += robotYChange
    currentTime += timeStep
    if (x % 1000 == 0):
        print(getDist(robotX, robotY, ballX, ballY))
    if getDist(robotX, robotY, ballX, ballY) < 0.5:
        break

print(currentTime)
