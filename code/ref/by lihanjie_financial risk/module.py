import torch
import torch.nn as nn
import torch.utils.data as data
import torch.nn.functional as F
import lightning as L
import pdb

class MLP(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(241, 128), nn.ReLU(),
                                     nn.Linear(128, 64), nn.ReLU(),
                                     nn.Linear(64,2))

    def forward(self, x):
        # in lightning, forward defines the prediction/inference actions
        y_pre = self.encoder(x)
        return y_pre

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop. It is independent of forward
        x, y = batch
        y_pre = F.log_softmax(self.encoder(x), dim=1)
        loss = F.nll_loss(y_pre, y)
        self.log("train_loss", loss,on_step=True)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer