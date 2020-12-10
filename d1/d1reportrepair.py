import os
import itertools
import memoize

#Set absolute location of current folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#Create full location of input file using absolute file path
filepath = os.path.join(THIS_FOLDER, 'input.txt')

#Open input.txt and read each new line as integer into a list called content
with open(filepath) as fp:
    content = [int(i) for i in fp.readlines()]

result = memoize.findsubset(content, 2020)

print(result[0] * result[1])