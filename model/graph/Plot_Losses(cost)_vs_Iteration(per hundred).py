
plt.figure(figsize=(16,10))
plt.plot(np.squeeze(costs),)
plt.ylabel('Losses')
plt.xlabel('iterations (per hundred)')
plt.title("Learning rate =" + str(learning_rate))
plt.show()
