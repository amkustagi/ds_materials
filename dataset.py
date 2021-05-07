import torch
from torch.utils.data import Dataset
from sklearn.model_selection import cross_val_score

cross_val_score()


# To Building data set class Importing Abstract class from the PyTorch
# It is a subclass of data set class
# Initializing the constructor

class toy_set(Dataset):
    # Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign
    # values) to the data members of the class when an object of class is created.
    def __init__(self, length=100, transform=None):
        self.x = 2 * torch.ones(length, 5)
        self.y = torch.ones(length, 10)
        self.len = length
        self.transform = transform

    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample

    def __len__(self):
        return self.len


# Creating an instance of a data_set object from toy_set sub class
data_set = toy_set()
print("data set", data_set[0])
