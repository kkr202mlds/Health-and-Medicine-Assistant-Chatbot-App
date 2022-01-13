from Creating_X_train_Y_train import X_train
from Data_Preprocessing import tags


num_epochs = 1000
batch_size = 10
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)
