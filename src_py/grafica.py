import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line 1', color='blue')
plt.title('Mi primer grafico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()