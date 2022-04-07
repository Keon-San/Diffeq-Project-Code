import math
import numpy

ballX = 4
ballY = 4

robotX = 0
robotY = 0
robotTheta = 0

timeStep = 0.01

currentTime = 0

maxWheelSpeed = 1

trackWidth = 1

def getDist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def getMovementSpeed():
    angleDotProduct = math.cos(robotTheta)*((ballX-robotX)/(math.sqrt(math.pow(ballX-robotX, 2) + math.pow(ballY-robotY, 2)))) + math.sin(robotTheta)*((ballY-robotY)/(math.sqrt(math.pow(ballX-robotX, 2) + math.pow(ballY-robotY, 2))))
    return math.pow(angleDotProduct, angleDotProductScalingPower)*kPMove*getDist(robotX, robotY, ballX, ballY)

def getXMovement(wheelSpeeds):
    return math.cos(robotTheta)*(wheelSpeeds[0] + wheelSpeeds[1])/2

def getYMovement(wheelSpeeds):
    return math.sin(robotTheta)*(wheelSpeeds[0] + wheelSpeeds[1])/2

def getThetaMovement():
    return kPTurn*(math.atan2(ballX-robotX, ballY-robotY) - robotTheta)

def getRealTheta(wheelSpeeds):
    return (wheelSpeeds[1] - wheelSpeeds[0])/trackWidth

def capSpeed(speed):
    return max(-maxWheelSpeed, min(speed, maxWheelSpeed))

def findWheelSpeeds(thetaSpeed, movementSpeed):
    rawWheelDifferential = (thetaSpeed*trackWidth)/2
    return [capSpeed(movementSpeed-rawWheelDifferential), capSpeed(movementSpeed+rawWheelDifferential)]

angleDotProductScalingPower = 1

bestTime = 9999999999

bestkPTurn = 0
bestkPMove = 0

counter = 0


for kPTurnTemp in range(0, 100, 1):
    kPTurn = kPTurnTemp/2
    for kPMoveTemp in range(0, 100, 1):
        kPMove = kPMoveTemp/1000
        currentTime = 0
        for x in range (0, 10000):
            thetaSpeed = getThetaMovement()
            movementSpeed = getMovementSpeed()
            wheelSpeeds = findWheelSpeeds(thetaSpeed, movementSpeed)

            robotThetaChange = getRealTheta(wheelSpeeds)*timeStep
            robotXChange = getXMovement(wheelSpeeds)*timeStep
            robotYChange = getYMovement(wheelSpeeds)*timeStep

            robotTheta += robotThetaChange
            robotX += robotXChange
            robotY += robotYChange
            currentTime += timeStep
            if getDist(robotX, robotY, ballX, ballY) < 0.5:
                break
        counter += 1
        print(counter)
        print(currentTime)
        robotX = 0
        robotY = 0
        robotTheta = 0
        if currentTime < bestTime:
            bestTime = currentTime
            bestkPMove = kPMove
            bestkPTurn = kPTurn

print(bestTime)
print(bestkPMove)
print(bestkPTurn)