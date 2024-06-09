import numpy as np
import argparse
import torch
import cv2
import math
from skimage.metrics import structural_similarity as ssim
import lpips
from torchvision import transforms
from PIL import Image
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
from sEDICT_functions import load_im_into_format_from_path

def mse(img1, img2):
    return np.sum((img1-img2)*(img1-img2))/(512*512*3)

def psnr(img1, img2):
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20*math.log10(PIXEL_MAX/math.sqrt(mse))

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Quantitative Evaluation")
    parser.add_argument("--reference_img_path", default="experiment_images/imagenet_dog_7.jpg", type=str, help="original img path")
    parser.add_argument("--generated_img_path", default="results/A dog_0.3_50_0.7_0.8_1.png", type=str, help="generated img path")
    
    args = parser.parse_args()
    print(args)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    loss_fn_alex = lpips.LPIPS(net='alex').to(device)
    
    img1_path = args.reference_img_path
    img2_path = args.generated_img_path
    
    orig_im = load_im_into_format_from_path(img1_path) if isinstance(img1_path, str) else img1_path # trust OK
    new_im = load_im_into_format_from_path(img2_path) if isinstance(img2_path, str) else img2_path # trust OK
    
    img1 = np.array(orig_im) 
    img2 = np.array(new_im) 
    
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    print('L2: ', mse(img1, img2)) # lower, better
    print('PSNR: ', psnr(img1, img2)) # higher, better
    print('SSIM: ', ssim(img1_gray, img2_gray)) # higher, better
    print('LPIPS: ', loss_fn_alex(transform(img1).to(device), transform(img2).to(device)).squeeze().item()) # lower, better
    
    
    
    