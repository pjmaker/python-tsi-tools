import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
sns.set()

ngui = 0
titree = 1

seasons = ['Summer', 'Autumn', 'Winter', 'Spring']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

data = np.zeros((2, 12))
data[ngui] = np.array([0.199871427202, 0.296006091029, 0.297957212043,
                       0.444831361115, 0.470577208274, 0.498978707318,
                       0.472658156097, 0.454615530798, 0.401374091686,
                       0.427869749377, 0.396290417027,
                       0.404837422725])

data[titree] = np.array([-0.00929752271785, 0.278511301958,
                         0.476211414739, 0.172027484045, -0.43235800762, -0.363226256687,
                         -0.432280799661, 0.386542213945, -0.17144691649, 0.272193887916,
                         0.538816374073, 0.536721908574])

f, ax = plt.subplots(figsize=(9, 5))
ax.set_title("Demand/temperature cross-correlation by month")
sns.heatmap(data, ax=ax, xticklabels=months, yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)

f, ax = plt.subplots(figsize=(9, 5))
data = np.zeros((2, 4))
data[ngui] = np.array([0.296538086976, 0.487189324256, 0.514526139168, 0.450245171872])
data[titree] = np.array([0.214817805306, -0.305728939378, -0.165815327627, 0.482964775041])
ax.set_title("Demand/temperature cross-correlation by season")
sns.heatmap(data, ax=ax, xticklabels=seasons, yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)

f, ax = plt.subplots(figsize=(9, 5))
data = np.zeros((2, 2))
data[ngui] = np.array([0.453218666825, 0.508308225015])
data[titree] = np.array([0.216289105258, 0.171861624369])
ax.set_title("Demand/temperature cross-correlation by tropical season")
sns.heatmap(data, ax=ax, xticklabels=['Wet', 'Dry'], yticklabels=['Ngui', 'TiTree'], annot=True, linewidth=2)
plt.show()
