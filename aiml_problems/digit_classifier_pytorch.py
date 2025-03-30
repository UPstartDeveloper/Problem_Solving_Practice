import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    # Source: https://neetcode.io/problems/handwritten-digit-classifier
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        pass
        # Define the architecture here
        self.h1 = nn.Linear(
            784, 512
        )
        self.a1 = nn.ReLU()
        self.dropout1 = nn.Dropout(p=0.2)
        self.h2 = nn.Linear(
            512, 10
        )
        self.a2 = nn.Sigmoid()
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        # Return the model's prediction to 4 decimal places
        flattened_images = torch.flatten(images, start_dim=1)
        first_layer_out = self.a1(self.h1(flattened_images))
        dropped = self.dropout1(first_layer_out)
        second_layer_out = self.a2(self.h2(dropped))
        return second_layer_out
