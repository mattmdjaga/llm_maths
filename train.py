import random
import argparse
from typing import List, Tuple, Dict, Union

from utils import zero_padding_multiplicatn, MathsDataset
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from accelerate import Accelerator
from tqdm import tqdm

def validation():
    pass

def train():
    pass

def main():
    parser = argparse.ArgumentParser()
    pass

if __name__ == "__main__":
    main()