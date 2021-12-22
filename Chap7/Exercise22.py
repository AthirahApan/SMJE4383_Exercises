import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

rolls = [random.randrange(1,7) for i in range(int(sys.argv[1]))]

values, frequencies = np.unique(rolls, return_counts=True)

sns.set_style('whitegrid')
axes = sns.barplot(values, frequencies, palette='bright')

axes.set(xlabel='Die Value', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
   text_x = bar.get_x() + bar.get_width()/ 2.0
   text_y = bar.get_height()
   
   axes.text(text_x, text_y, text_y, 
             fontsize=11, ha='center', va='bottom')
             
plt.show()
