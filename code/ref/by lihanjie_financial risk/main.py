import torch
import torch.nn as nn
import torch.utils.data as data
import torch.nn.functional as F
import lightning as L
from module import MLP

from dataset import get_dataset


dataset = get_dataset()
train_size = int(len(dataset)*0.7)
val_size = len(dataset)-train_size
train, val = data.random_split(dataset, [train_size, val_size])

autoencoder = MLP()
trainer = L.Trainer(max_epochs=20)
trainer.fit(autoencoder, dataset)






