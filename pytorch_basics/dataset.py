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


# Use loop to print out first N elements in dataset
def loop_toy_set(N=5):
    for i in range(N):
        dt = toy_set()
        x, y = dt[i]
        print("index: ", i, "x value: :", x, "y value : ", y)


print("Input N value to print N no of elements in the toy_dataset")
N = int(input())
loop_toy_set(N)


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
    def __init__(self, mul_val=200):
        self.mul_val = mul_val

    def __call__(self, sam):
        var1 = sam[0]
        var2 = sam[1]
        var1 = var1 * self.mul_val
        var2 = var2 * self.mul_val
        mul_sample = var1, var2
        return mul_sample


# Creating an instance of a data_set object from toy_set subclass
# Its an object instance without transformation
data_set = toy_set()

#  Creating the object with transformation - Add 5 and Multiply by 12
add_n_mul = add_multiply(5, 12)
add_n_mul_transform_ = toy_set(transform=add_n_mul)

#  Creating the object with transformation - Multiply by 4 and 3
mul = multi()
mul_transform_ = toy_set(transform=mul)

# Logic to compose and apply series of transformations
series_trans_ = transforms.Compose([add_multiply(), multi()])

print("Our toy_set object: ", data_set)
print("Value on Index 0 - Without transformation: ", data_set[0])
print("Our toy_set length: ", len(data_set))
print("Value on Index 0 - With applying add_multiply transformation : ", add_n_mul_transform_[0])
print("Value on Index 3 - With applying mul transformation : ", mul_transform_[3])
print("Value on Index 0  After 1st and 2nd transformation : ", series_trans_(data_set[0]))

try:
    print("Enter index to access the elements from toy_set object: ")
    index_input = int(input())
    element_val = series_trans_(data_set[index_input])
    print("Elements in the index {} after series of transform :{}".format(index_input, element_val))

except (IndexError, TypeError, NameError):
    print(" Error !!!")
