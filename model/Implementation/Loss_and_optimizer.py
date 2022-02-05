#PyTorch
import torch
import torch.nn as nn
from Data_Loader_with_Model import model
from Hyper-parameters import learning_rate


criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
