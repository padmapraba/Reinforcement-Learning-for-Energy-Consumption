import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import numpy as np


def plot_actions(action_list,title):
  fig, ax = plt.subplots(figsize=(8,1))
  data = pd.DataFrame(action_list, columns=['Building_2','Building_3'])
  x = list(range(data.shape[0]))
  for i, col in enumerate(data.columns):
    y = data[col]
    ax.plot(x,y,label=str(col))
  ax.set_xlabel('Time Step')
  ax.set_ylabel('Elecrical Storage')
  ax.set_title(f'{title} Agent Actions')
  ax.legend(loc='upper left', framealpha=0.0,bbox_to_anchor=(1.0, 1.0))
  ax.xaxis.set_major_locator(ticker.MultipleLocator(24))
  plt.savefig(f'{title} Agent Actions.png',dpi=900,bbox_inches='tight')
  # plt.tight_layout()
  plt.show()

def plot_soc(env):
  building_count = len(env.buildings)
  fig, axes = plt.subplots(1, 2, figsize=(10,2))

  for i, ax in enumerate(axes[:building_count]):
    building = env.buildings[i]
    soc = np.array(building.electrical_storage.soc)
    capacity = building.electrical_storage.capacity_history[0]
    y = soc/capacity
    x = range(len(y))
    ax.plot(x, y, label=building.name)
    ax.set_title(building.name)
    ax.set_xlabel('Time step')
    ax.set_ylabel('SoC')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(24))

  for j in range(building_count, len(axes)):
    fig.delaxes(axes[j])

  plt.tight_layout()

