#PyTorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
