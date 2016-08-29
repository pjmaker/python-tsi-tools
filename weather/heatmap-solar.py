import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
sns.set()

ngui = 0
titree = 1

seasons = ['Summer', 'Autumn', 'Winter', 'Spring']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# by month
data = np.zeros((2, 12))
data[ngui] = np.array([-0.220277633505, -0.187297445331,
                       -0.177601999993, -0.264236899064, -0.276552253506, -0.259026836204,
                       -0.297641810655, -0.251679394314, -0.273472221503, -0.27176012664,
                       -0.19931211828, -0.195672708552])

data[titree] = np.array([-0.500292787545, -0.337059372316,
                         -0.272931515882, -0.479363716906, -0.624282838955, -0.590731545994,
                         -0.538216910567, -0.499072940762, -0.518405340184, -0.312133974784,
                         -0.119893635669, -0.106503002362])

f, ax = plt.subplots(figsize=(9, 5))
ax.set_title("Demand/temperature cross-correlation by month")
sns.heatmap(data, ax=ax, xticklabels=months, yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)

# by season
f, ax = plt.subplots(figsize=(9, 5))
data = np.zeros((2, 4))

data[ngui] = np.array([-0.164359530136, -0.24629642116,
                       -0.252465996529, -0.17841338525])
data[titree] = np.array([-0.359506723638, -0.556724389737,
                         -0.509627920874, -0.100924120072])
ax.set_title("Demand/temperature cross-correlation by season")
sns.heatmap(data, ax=ax, xticklabels=seasons, yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)

# by wet/dry
f, ax = plt.subplots(figsize=(9, 5))
data = np.zeros((2, 2))
data[ngui] = np.array([-0.207546309935, -0.243115943644])
data[titree] = np.array([-0.369008167252, -0.315672629908])
ax.set_title("Demand/temperature cross-correlation by tropical season")
sns.heatmap(data, ax=ax, xticklabels=['Wet', 'Dry'], yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)
plt.show()
