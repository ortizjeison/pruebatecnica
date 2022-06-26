import robot

logFile = open('mylog.txt', 'w')
robot.run("first.robot", stdout=logFile)