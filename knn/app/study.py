import numpy as np
import collections as c

data = np.array([
    [154,1],
    [126,1],
    [70,2],
    [196,2],
    [161,2],
    [371,4]
])

feature = (data[:,0])

label = data[:,-1]

predictPoint = 200

distance = list(map(lambda x: abs(predictPoint - x), feature))

sortindex = (np.argsort(distance))

sortedlabel = (label[sortindex])

k = 3

print(c.Counter(sortedlabel[0:k]) . most_common(1)[0][0])
