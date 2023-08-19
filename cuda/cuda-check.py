import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name())
device = torch.device('cuda:0')
a = torch.zeros([2, 4], dtype=torch.int32, device=device)
print(a)
