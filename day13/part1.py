testRawInput = """939
7,13,x,x,59,x,31,19"""

rawInput = """1006401
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,449,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,607,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

inputList = rawInput.splitlines()

earliestTime = int(inputList[0])
busIds = [int(busId) for busId in inputList[1].split(',') if busId != 'x']

matchingBusId = -1
time = earliestTime
while(matchingBusId == -1):
    time += 1
    for busId in busIds:
        if time % busId == 0:
            matchingBusId = busId
            break

print((time - earliestTime) * matchingBusId)