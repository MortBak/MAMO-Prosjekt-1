import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leser csv filer fra github
df1 = pd.read_csv('https://raw.githubusercontent.com/richbi/CatTrack_public/main/DATA/cat%20GPS%20data/cat_51.csv').head(100)
df2 = pd.read_csv('https://raw.githubusercontent.com/richbi/CatTrack_public/main/DATA/cat%20GPS%20data/cat_52.csv').head(100)
df3 = pd.read_csv('https://raw.githubusercontent.com/richbi/CatTrack_public/main/DATA/cat%20GPS%20data/cat_53.csv').head(100)

# Beregn avstand mellom nabopunkter for hver fil
df1['distance'] = np.sqrt((df1['x'].diff())**2 + (df1['y'].diff())**2)
df2['distance'] = np.sqrt((df2['x'].diff())**2 + (df2['y'].diff())**2)
df3['distance'] = np.sqrt((df3['x'].diff())**2 + (df3['y'].diff())**2)


fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

ax[0].plot(df1['x'], df1['y'], marker="o", linestyle="-")
ax[0].set_ylabel('y')
ax[0].set_xlabel('x')
ax[0].set_title('Cat gps fil1')

ax[1].plot(df2['x'], df2['y'], marker="o", linestyle="-")
ax[1].set_ylabel('y')
ax[1].set_xlabel('x')
ax[1].set_title('Cat gps fil2')

ax[2].plot(df3['x'], df3['y'], marker="o", linestyle="-")
ax[2].set_ylabel('y')
ax[2].set_xlabel('x')
ax[2].set_title('Cat gps fil3')

plt.tight_layout()
plt.show()

# Lag histogram for avstand mellom nabopunkter
fig1, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

# Histogram for fil 1
ax[0].hist(df1['distance'], bins=10, edgecolor='black')
ax[0].set_title('Histogram for Avstand mellom Nabopunkter - Fil 1')
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')

# Histogram for fil 2
ax[1].hist(df2['distance'], bins=10, edgecolor='black')
ax[1].set_title('Histogram for Avstand mellom Nabopunkter - Fil 2')
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')

# Histogram for fil 3
ax[2].hist(df3['distance'], bins=10, edgecolor='black')
ax[2].set_title('Histogram for Avstand mellom Nabopunkter - Fil 3')
ax[2].set_xlabel('X')
ax[2].set_ylabel('Y')

plt.tight_layout()
plt.show()


