from matplotlib_venn import venn2
import matplotlib.pyplot as plt


city1 = {'Tokyo' ,'Madrid' ,'Mumbai' ,'Chennai'}
city2 = {'Tokyo' ,'Manchester' ,'Bangalore' ,'Beijing'}

venn2([city1, city2], ('City 1', 'City 2'))

plt.title('City Venn Diagram')
plt.show()



