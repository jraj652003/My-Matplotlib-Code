import matplotlib.pyplot as plt
import pandas as pd

data = {
    'cricket_bat': ['SG', 'BDM', 'SS', 'GM', 'Kookaburra', 'Spartan'],
    'mrp': [2000, 2200, 2400, 2700, 2800, 3000],
    'weight_grams': [1100, 1200, 1250, 1330, 1480, 1600]
}

df = pd.DataFrame(data)

plt.plot(df['mrp'], df['weight_grams'])
plt.xlabel('Bat Price (MRP)')
plt.ylabel('Bat Weight (Grams)')
plt.grid()
plt.title('Bat price depends on the weight')
plt.show()