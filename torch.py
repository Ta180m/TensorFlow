import torch
from importlib import reload
reload(torch)

print(torch.cuda.is_available())
 
