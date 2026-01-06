# Physics-Informed Neural Networks - A simple example

This repository contains a simple example of a Physics-Informed Neural Network (PINN). 
The simple tutorial is the minimal, barebones code you need to train a PINN. The more detailed tutorial contains a few extra features, such as seeing how the different loss functions behave during training. 

## Getting started

Open a new terminal window and run the following commands:

    git clone https://github.com/markbugden/PINNs
    cd PINNS
    poetry install --no-root

The tutorial in this repo is very small so you won't need a GPU. , but if you wish to see if Pytorch can use your GPU you can run the check_env.py script using
```poetry run python check_env.py```.