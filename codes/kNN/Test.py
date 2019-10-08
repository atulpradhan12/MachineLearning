import pathlib
import matplotlib.pyplot as plt
from codes.kNN.kNN import *

""" First Test Sample """
# group, labels = create_dataSet()
# print(classify0([0, 0], group, labels, 3))

""" 2nd Test Sample: Dating ML Model """
filePath = pathlib.Path(__file__).parent / '../../resources/datingTestSet.txt'
datingDataMat, datingLabels = file2matrix(filePath)
# print(datingDataMat)
# print(datingLabels)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
plt.show()

