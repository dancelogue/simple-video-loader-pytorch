# Python
from pathlib import Path
import random
import subprocess

# Pytorch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

# Third Party
from PIL import Image


class UCF101Dataset(Dataset):
    def __init__(self, root, transform=None):
        pass

    def __len__(self):
        return len(self.keys)

    def load_ucf_image(self, path):
        img = Image.open(path)
        transformed_img = self.transform(img)
        img.close()
        return transformed_img