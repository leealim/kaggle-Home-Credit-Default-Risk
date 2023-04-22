import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset
import numpy as np
import pandas as pd
from sklearn import preprocessing


class MyDataset(Dataset):
    def __init__(self, data_root, data_label):
        super(MyDataset, self).__init__()
        self.data = data_root
        self.label = data_label

    def __getitem__(self, index):
        data = self.data[index]
        labels = self.label[index]
        return data, labels

    def __len__(self):
        return len(self.data)


def get_dataset():
    FileName = './data/app_tr.csv'
    df = pd.read_csv(FileName)

    le = preprocessing.LabelEncoder()
    le_count = 0

    # Iterate through the columns
    for col in df:
        if df[col].dtype == 'object':
            # If 2 or fewer unique categories
            if len(list(df[col].unique())) <= 2:
                # Train on the training data
                le.fit(df[col])
                # Transform both training and testing data
                df[col] = le.transform(df[col])

                # Keep track of how many columns were label encoded
                le_count += 1

    data = pd.get_dummies(df)
    data = np.array(data)
    data = torch.tensor(data).to(torch.float32)
    source_data = data[:, 3:]
    source_label = data[:, 2].type(torch.LongTensor)
    dataset = MyDataset(source_data, source_label)
    datas = DataLoader(dataset, batch_size=256, shuffle=False, sampler=None, \
                       batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, \
                       drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None)
    # 307511*240
    return datas
