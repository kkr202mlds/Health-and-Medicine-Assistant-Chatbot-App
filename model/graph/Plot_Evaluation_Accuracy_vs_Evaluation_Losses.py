import matplotlib.pyplot as plt
%matplotlib inline
from Implementation.Train_the_model import eval_accu, eval_losses


plt.figure(figsize=(16,10))
plt.plot(eval_accu)
plt.plot(eval_losses)
plt.xlabel('accurancy')
plt.ylabel('losses')
plt.legend(['Accuracy','Losse'])
plt.title('Evaluation Accuracy  vs Evaluation Losses')
 
plt.show()
