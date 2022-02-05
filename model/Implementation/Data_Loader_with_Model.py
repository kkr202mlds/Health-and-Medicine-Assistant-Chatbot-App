#PyTorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from Chat_Dataset  import ChatDataset
from Hyper-parameters import batch_size, input_size, hidden_size, output_size
from Neural_Network_Model import NeuralNet
from Creating_X_train_Y_train import X_train, y_train 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

model = NeuralNet(input_size, hidden_size, output_size).to(device)
