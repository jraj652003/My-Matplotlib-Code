import matplotlib.pyplot as plt
import pandas as pd

data = {
    'cricket_bat': ['SG', 'BDM', 'SS', 'GM', 'Kookaburra', 'Spartan'],
    'mrp_jan': [2000, 2200, 2400, 2700, 2800, 3000],
    'mrp_feb': [2100, 2300, 2500, 2800, 2900, 3100],
    'weight_grams': [1100, 1200, 1250, 1330, 1480, 1600]
}

df = pd.DataFrame(data)

fig = plt.figure()
ax = plt.subplot()
ax.plot(df['weight_grams'], df['mrp_jan'], '--', label='January')
ax.plot(df['weight_grams'], df['mrp_feb'], ':', label='February')
legend = ax.legend()
legend.get_frame().set_facecolor('gray')
plt.xlabel('Bat Weight (Grams)')
plt.ylabel('Bat Price (MRP)')
plt.title('Bat price depends on the weight')
plt.show()
