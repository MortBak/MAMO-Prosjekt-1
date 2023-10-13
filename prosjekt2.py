
import numpy as np
import matplotlib.pyplot as plt

# Antall steg
NI = 100

# Definisjon av x- og y-koordinater for brownske bevegelser som arrayer
# med NI elementer, alle lik 0.
Xb = np.zeros(NI)
Yb = np.zeros(NI)

# Definisjon av x- og y-koordinater for Levy walks som arrayer
# med NI elementer, alle lik 0.
Xl = np.zeros(NI)
Yl = np.zeros(NI)

for i in range(1,NI):
    rb = abs(np.random.normal(0,1,1))
    thb = np.random.uniform(0,2*np.pi,1)
    Xb[i] = Xb[i-1] + rb*np.cos(thb)
    Yb[i] = Yb[i-1] + rb*np.sin(thb)
    
    rl = abs(np.random.standard_cauchy(1))
    thl = np.random.uniform(0,2*np.pi,1)
    Xl[i] = Xl[i-1] + rl*np.cos(thl)
    Yl[i] = Yl[i-1] + rl*np.sin(thl)
    
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.plot(Xb, Yb, '-o')
plt.title("Brownske bevegelser")

plt.subplot(122)
plt.plot(Xl, Yl, '-o')
plt.title('Levy walks')

plt.tight_layout()
plt.show()


def distanse_histogram(x, y, title):
    D = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
    plt.hist(D, bins=20)
    plt.title('Histogram for ' + title)
    plt.xlabel('Avstand mellom nabopunkter')
    plt.ylabel('Antall')

plt.figure(figsize=(10, 5))
plt.subplot(121)
distanse_histogram(Xb, Yb, 'Brownske bevegelser')

plt.subplot(122)
distanse_histogram(Xl, Yl, 'Levy walks')

plt.tight_layout()
plt.show()


