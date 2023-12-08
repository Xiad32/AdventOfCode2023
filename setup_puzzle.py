import os
import subprocess

day = "02"
try:
    os.mkdir(day)
except:
    print("exception")
puzzle = "02b"

files = ["_test_input.txt", "_test_output.txt", "_input.txt","_output.txt"]
for file in files:
    with open(day + os.sep + puzzle + file, 'w') as f:
        pass

os.system("copy template.py "+ day + os.sep + puzzle + ".py")