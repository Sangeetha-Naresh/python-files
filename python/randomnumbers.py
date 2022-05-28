import random

import pandas as pd
from matplotlib import pyplot as plt

numlist1=random.sample(range(20,100),15)
print(numlist1)

numlist2= random.sample(range(200,300),15)
print(numlist2)

plt.plot(numlist1,numlist2)
plt.show()