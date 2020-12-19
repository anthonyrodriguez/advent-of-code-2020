import time as timer
start_time = timer.time()
testRawInput = """939
7,13,x,x,59,x,31,19"""

testRawInput2 = """x
1789,37,47,1889"""

rawInput = """1006401
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,449,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,607,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

inputList = rawInput.splitlines()

busIds = inputList[1].split(',')

largestIdIndex = -1
largestID = -1
for i in range(len(busIds)):
    if busIds[i] != 'x' and int(busIds[i]) > largestID:
        largestID = int(busIds[i])
        largestIdIndex = i

# noted in the question that the answer is above 100000000000000
time = 100000000000000
while(time % largestID != 0):
    time += 1

time -= largestIdIndex
correctTimestamp = -1
while(correctTimestamp == -1):
    time += largestID
    correctTimestamp = time
    tempTime = time
    for busId in busIds:
        if busId != 'x':
            if tempTime % int(busId) != 0:
                correctTimestamp = -1
                break
        tempTime += 1
        

print(time)
print("--- %s seconds ---" % (timer.time() - start_time))