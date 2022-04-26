import math
import numpy

ballX = 4
ballY = 4

ballXMovement = 0.5
ballYMovement = 0.5

robotX = 0
robotY = 0
robotTheta = 0

timeStep = 0.01

currentTime = 0

maxWheelSpeed = 1

trackWidth = 1

def getDist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def getMovementSpeed(baseSpeed, desiredVelocity):
    angleDotProduct = math.cos(robotTheta)*((desiredVelocityVector[0])/(math.sqrt(math.pow(desiredVelocityVector[0], 2) + math.pow(desiredVelocityVector[1], 2)))) + math.sin(robotTheta)*(desiredVelocityVector[1])/(math.sqrt(math.pow(desiredVelocityVector[0], 2) + math.pow(desiredVelocityVector[1], 2)))
    return math.pow(angleDotProduct, angleDotProductScalingPower)*baseSpeed

def getXMovement(wheelSpeeds):
    return math.cos(robotTheta)*(wheelSpeeds[0] + wheelSpeeds[1])/2

def getYMovement(wheelSpeeds):
    return math.sin(robotTheta)*(wheelSpeeds[0] + wheelSpeeds[1])/2

def getThetaMovement(desiredAngle):
    return kPTurn*(desiredAngle - robotTheta)

def getRealTheta(wheelSpeeds):
    return (wheelSpeeds[1] - wheelSpeeds[0])/trackWidth

def capSpeed(speed):
    return max(-maxWheelSpeed, min(speed, maxWheelSpeed))

def findWheelSpeeds(thetaSpeed, movementSpeed):
    rawWheelDifferential = (thetaSpeed*trackWidth)/2
    return [capSpeed(movementSpeed-rawWheelDifferential), capSpeed(movementSpeed+rawWheelDifferential)]

def to360Wrap(angleWrap):
    if (angleWrap < 0):
        return angleWrap + 360
    else:
        return angleWrap


angleDotProductScalingPower = 1

bestTime = 9999999999

bestkPTurn = 0
bestkPMove = 0

counter = 0




kPTurn = 27.7
kPMove = 0.222
currentTime = 0
for x in range (0, 100000):
    lastBallX = ballX
    lastBallY = ballY

    ballX += ballXMovement * timeStep
    ballY += ballYMovement * timeStep

    ballVelocity = [(ballX - lastBallX)/timeStep, (ballY - lastBallY)/timeStep]

    desiredVelocityVector = [kPMove*getDist(robotX, robotY, ballX, ballY)*math.cos(math.atan2(ballY-robotY, ballX-robotX)), kPMove*getDist(robotX, robotY, ballX, ballY)*math.sin(math.atan2(ballY-robotY, ballX-robotX))]
    desiredVelocityVector[0] += ballVelocity[0]
    desiredVelocityVector[1] += ballVelocity[1] 

    thetaSpeed = getThetaMovement(math.atan2(desiredVelocityVector[1], desiredVelocityVector[0]))
    movementSpeed = getMovementSpeed(math.sqrt(math.pow(desiredVelocityVector[0], 2) + math.pow(desiredVelocityVector[1], 2)), desiredVelocityVector)
    wheelSpeeds = findWheelSpeeds(thetaSpeed, movementSpeed)

    robotThetaChange = getRealTheta(wheelSpeeds)*timeStep
    robotXChange = getXMovement(wheelSpeeds)*timeStep
    robotYChange = getYMovement(wheelSpeeds)*timeStep

    robotTheta += robotThetaChange
    robotX += robotXChange
    robotY += robotYChange
    
    print(getDist(robotX, robotY, ballX, ballY))

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