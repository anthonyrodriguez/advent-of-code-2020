testRawInput = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

testRawInput2 = """16
10
15
5
1
11
7
19
6
12
4"""

rawInput = """80
87
10
122
57
142
134
59
113
139
101
41
138
112
46
96
43
125
36
54
133
17
42
98
7
114
78
67
77
28
149
58
20
105
31
19
18
27
40
71
117
66
21
72
146
90
97
94
123
1
119
30
84
61
91
118
2
29
104
73
13
76
24
148
68
111
131
83
49
8
132
9
64
79
124
95
88
135
3
51
39
6
60
108
14
35
147
89
34
65
50
145
128"""

testRawInput3 = """1
4
5
6
7
10"""

inputList = rawInput.splitlines()
inputList = [int(x) for x in inputList]
inputList.sort()
inputList.insert(0, 0)

pathLists = []
pathCountList = [1]

for i in range(len(inputList) - 1, -1, -1):
    curPathList = []
    #multiplier = 0
    #postMultTotal = 0
    
    for j in range(1, 4):
        if i-j >= 0 and inputList[i] - inputList[i-j] <= 3:
            curPathList.append(i-j)
        else: 
            break
    pathLists.insert(0, curPathList)
        
for i in range(1, len(pathLists)):
    curPathCount = 0
    for j in pathLists[i]:
        curPathCount += pathCountList[j]
    pathCountList.append(curPathCount)

#print(inputList)
#print(pathLists)
print(pathCountList[-1])
