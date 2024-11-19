import numpy as np
import matplotlib.pyplot as plt

tid = np.array(list(range(25)))
temp = np.array([80, 75, 71, 69, 67, 65, 63.5, 62, 60.5, 59, 57.5, 56, 54.5, 53.5, 52.5, 51.5, 50.5, 49.5, 48.5, 47.5, 47, 46.5, 46, 45.5, 45])

T0 = 80
Tk = 22
alpha = (np.log(23/58))/24
    
tid_teori = np.linspace(0, max(tid), 100)

def T(t):
    return (T0 - Tk) * np.exp(alpha * tid_teori) + Tk

# Plot
plt.plot(tid, temp, label='Målt temperatur', color='pink')
plt.plot(tid_teori, T(tid_teori), label='Newtons avkjølningslov', color='aquamarine')
plt.title("Temperaturendringen til teen over tid")
plt.xlabel('Tid (min)')
plt.ylabel('Temperatur (°C)')
plt.grid(True)
plt.legend()
plt.show()