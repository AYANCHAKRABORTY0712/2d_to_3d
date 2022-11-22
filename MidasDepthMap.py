import cv2
import torch
import time
import numpy as np
import urllib.request

import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageEnhance


# Load a MiDas model for depth estimation
model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

# Move model to GPU if available
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

# Load transforms to resize and normalize the image
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

img = cv2.imread("images/top.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




print("here")

input_batch = transform(img).to(device)
with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

output = prediction.cpu().numpy()
print(output.shape)
print(output)
print(np.amax(output))

cv2.imwrite("images/depthTop.jpg", output)


img = cv2.imread("images/depthTop.jpg", 0)
  
# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
  
cv2.imwrite("images/depthTop.jpg",equ)
# show image input vs output
cv2.imshow('image', equ)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
