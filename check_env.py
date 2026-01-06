import torch

print(f"PyTorch version: {torch.__version__}")
print(f"Is CUDA available? {torch.cuda.is_available()}") # Should be False
print(f"Is MPS (Mac GPU) available? {torch.backends.mps.is_available()}")

# A quick PINN-style test: can we compute a derivative?
x = torch.tensor([[1.0]], requires_grad=True)
y = x**3
y.backward()
print(f"Derivative of x^3 at x=1: {x.grad.item()}") # Should be 3.0