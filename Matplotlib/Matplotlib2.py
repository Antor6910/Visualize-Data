import matplotlib.pyplot as plt

from EnumerateFunction import value

labels=['A','B','C']
values=[1,4,2]

plt.figure(figsize=(5,3),dpi=100)


bars=plt.bar(labels,values)
patterns=['/','O','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

    """
    patterns.pop(0) removes and returns the first element from the patterns
     list ('/' for the first iteration, 'O' for the second, and '*' for the third).
    set_hatch() is a method in matplotlib's BarContainer object that allows 
    you to fill the bar with a specified hatch pattern (e.g., diagonal lines, circles, stars).
    """

#plt.savefig('barchart.png',dpi=300)
plt.show()