#PyTorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset
from Creating_X_train_Y_train import X_train, y_train 


class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples
