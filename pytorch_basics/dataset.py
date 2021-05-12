import torch
from torch.utils.data import Dataset
from torchvision import transforms


# To Building data set class Importing Abstract class from the PyTorch
# It is a subclass of data set class
# Initializing the constructor

class toy_set(Dataset):
    # Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign
    # values) to the data members of the class when an object of class is created.
    def __init__(self, length=100, transform=None):
        self.x = 2 * torch.ones(length, 2)
        self.y = torch.ones(length, 1)
        self.len = length
        self.transform = transform

    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample

    def __len__(self):
        return self.len


def loop_toy_set(num=5):
    for i in range(num):
        dt = toy_set()
        x, y = dt[i]
        print("index: ", i, "x value: :", x, "y value : ", y)


loop_toy_set()


class add_multiply(object):
    def __init__(self, addx=1, muly=1):
        self.addx = addx
        self.muly = muly

    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x + self.addx
        y = y * self.muly
        sample = x, y
        return sample


class multi(object):
    def __init__(self, x=2, y=2):
        self.x = x
        self.y = y

    def __call__(self, sam):
        var1 = sam[0]
        var2 = sam[1]
        var1 = var1 * self.x
        var2 = var2 * self.y
        mul_sample = var1, var2
        return mul_sample


# Creating an instance of a data_set object from toy_set subclass
# Its an object instance without transformation
data_set = toy_set()


#  Creating the object with transformation - Add 5 and Multiply by 12
a_m = add_multiply(5, 12)
dt_ = toy_set(transform=a_m)


#  Creating the object with transformation - Multiply by 4 and 3
mul = multi(4, 3)
dt1_ = toy_set(transform=mul)


print("Without transformation: ", data_set[0])
print("With applying add_multiply transformation : ", dt_[0])
print("With applying mul transformation : ", dt1_[3])

# Logic to compose and apply series of transformations
series_trans = transforms.Compose([add_multiply(), multi()])

print("After 1st and 2nd transformation : ", series_trans(data_set[0]))
