from collections import deque
import time
class MyNewStack(deque):
    isLocked = bool
import itertools
import random
print("""Welcome to the tube game!
The goal of the game is to make all tubes have 4 of the same number
The max number of numbers a tube can fit is 4! Give it a try!
Before every tube there is a number. You can move the rightmost number from one tube to the other.
To move a number, enter the source tube followed by the distnation tube separted by a space!""")
try:
    NoOfTubes = int(input("Please enter the number of tubes you wish to play with (3 to 8): "))
    StartTime = time.time()
except:
    NoOfTubes = 3
    StartTime = time.time()
Tube1 = MyNewStack()
Tube2 = MyNewStack()
Tube3 = MyNewStack()
Tube4 = MyNewStack()
Tube5 = MyNewStack()
Tube6 = MyNewStack()
Tube7 = MyNewStack()
Tube8 = MyNewStack()
AllTubes = [Tube1,Tube2,Tube3,Tube4,Tube5,Tube6,Tube7,Tube8]
TubesLocked = 0
def DrawTube(Nums,TubeID):
    print("""        -----------------
Tube {1}  | {0}         
        -----------------""".format(Nums,TubeID))
AllNums = []
for i in range (1,NoOfTubes):
    for ii in range(4):
        AllNums.append(i)
random.shuffle(AllNums)
for i in range(NoOfTubes-1):
    for ii in AllNums[4*i:4*(i+1)]:
        AllTubes[i].append(ii)
def Move(S,D):
    try:
        AllTubes[D-1].append(AllTubes[S-1].pop())
    except:
        print("Can't move from/to this tube")
while TubesLocked < NoOfTubes-1:
    for i in range(NoOfTubes):
        DrawTube(" ".join(map(str,AllTubes[i])),i+1)
    try:
        S,D = [int(x) for x in input("Please enter the source and destination(0 0 to exit): ").split()]
        if S == 0 and D == 0:
            exit()
        else:
            if AllTubes[S-1].count == 0 or AllTubes[D-1].count == 4 or AllTubes[S-1].isLocked == True or AllTubes[D-1].isLocked == True or D > NoOfTubes:
                print("Can't move from/to this tube")
            else:
                Move(S,D)
                TubesLocked = 0
                for i in range(NoOfTubes):
                    if len(list(itertools.groupby(AllTubes[i]))) == 1 and len(AllTubes[i]) == 4:
                        AllTubes[i].isLocked = True
                        TubesLocked += 1
    except ValueError:
        print("Invalid source/destination! Please try again.")
    except IndexError:
        print("Invalid source/destination! Please try again.")
for i in range(NoOfTubes):
    DrawTube(" ".join(map(str,AllTubes[i])),i+1)
print("Congrats! You Won!")
X = "{0:.3f}".format(time.time() - StartTime)
print(f"You took {X} seconds!")
