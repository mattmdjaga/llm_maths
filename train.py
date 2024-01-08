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


def train(args):
    accelerator = Accelerator(log_with="wandb", project_dir=args.save_path)

    # Get configs that will be repeatedly used
    model_name = args.model_name
    batch_size = args.batch_size
    max_digits = args.max_digits
    save_path = args.save_path

    # Set random seed
    random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # init tracking
    accelerator.init_trackers(
        project_name="llm_maths",
        config=args,
        #init_kwargs={"wandb": {"entity": "my-wandb-team"}},
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, default="gpt2")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument(
        "--max_digits",
        type=int,
        default=5,
        help="The number of maximum digits used for multiplication",
    )
    parser.add_argument(
        "--num_pairs",
        type=int,
        default=10000,
        help="The number of pairs used for training",
    )
    parser.add_argument(
        "--validation_pairs_per_combination",
        type=str,
        default="20,40,60,80,100",
        help="The number of pairs used for validation per combination of digits",
    )
    parser.add_argument(
        "--num_epochs", type=int, default=10, help="The number of epochs to train"
    )
    parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    parser.add_argument(
        "--save_path", type=str, default="/testing", help="Path to save the results"
    )
    parser.add_argument(
        "--save_every", type=int, default=1000, help="Save the model every n steps"
    )
    parser.add_argument("--log_every", type=int, default=100, help="Log every n steps")
    args = parser.parse_args()

    train(args)


if __name__ == "__main__":
    main()