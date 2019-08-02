# Python
from pathlib import Path
import random
import subprocess

# Pytorch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

# Third Party
from PIL import Image

CACHE_ROOT = Path.cwd() / 'dataset' / 'cache'

class UCF101Dataset(Dataset):
    def __init__(self, root, transform=None):
        CACHE_ROOT.mkdir(parents=True, exist_ok=True)

    def __len__(self):
        return len(self.keys)

    def load_ucf_image(self, path):
        img = Image.open(path)
        transformed_img = self.transform(img)
        img.close()
        return transformed_img

    def __getitem__(self, idx):
        values_list = list(self.values)
        value = values_list[idx]
        label = int(value.get('label')) - 1
        video_path = value.get('video_path')
        video_name = value.get('video_name')

        frame_path = 'val-{video_name}-frame-{index}_%d.jpg'.format(video_name=video_name, index=idx)

        subprocess.call([
            'ffmpeg',
            '-i',
            str(video_path),
            '-vf',
            "select='eq(n\,{index})'".format(index=idx),
            '-vsync',
            '0',
            frame_path
            ],
            # stdout=FNULL,
            stderr=subprocess.DEVNULL
        )
            
        return ()


if __name__ == '__main__':
    dataset = UCF101Dataset('')