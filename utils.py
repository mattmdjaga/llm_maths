import random
from typing import List, Tuple, Set, Union

from torch.utils.data import Dataset


def zero_padding_multiplicatn(
    num_1: int, num_2: int, padding_size: int = 0, reverse: bool = False
) -> str:
    """
    Args:
        num_1 (int): first number
        num_2 (int): second number
        padding_size (int, optional): padding size. Defaults to 0.
        reverse (bool, optional): reverse the answer. Defaults to False.

    Returns:
        (str): multiplication result string
    """
    num_1 = str(num_1)
    num_2 = str(num_2)
    answer = int(num_1) * int(num_2)
    num_1 = "0" * (padding_size - len(num_1)) + num_1 if padding_size else num_1
    num_2 = "0" * (padding_size - len(num_2)) + num_2 if padding_size else num_2
    answer = str(answer)[::-1] if reverse else str(answer)
    answer = "0" * (padding_size - len(answer)) + answer if padding_size else answer
    return f"{num_1} * {num_2} = {answer}"


def generate_validation_set(
    n: int, pairs_per_combination: List[int]
) -> Set[Tuple[int, int]]:
    """
    Args:
        n (int): max digits
        pairs_per_combination (List[int]): number of pairs per combination.

    Returns:
        (Set[Tuple[int, int]]): list of pairs
    """
    pairs = set()
    for digit1 in range(1, n + 1):
        limit = pairs_per_combination[digit1 - 1]
        limit_per_pair = limit // n
        for digit2 in range(1, n + 1):
            cur_pairs = set()
            while len(cur_pairs) < limit_per_pair:
                num1 = random.randint(10 ** (digit1 - 1), 10**digit1 - 1)
                num2 = random.randint(10 ** (digit2 - 1), 10**digit2 - 1)
                pair = (num1, num2)
                # pair_reverse = (num2, num1)

                cur_pairs.add(pair)
            pairs.update(cur_pairs)

    return pairs


def generate_training_set(
    n: int, num_pairs: int, validation_pairs: Set[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    Args:
        n (int): max digits
        num_pairs (int): number of pairs
        validation_pairs (Set[Tuple[int, int]]): validation pairs

    Returns:
        (List[Tuple[int, int]]): list of pairs
    """
    pairs = []
    while len(pairs) < num_pairs:
        # Randomly determine the number of digits for each number
        digits1 = random.randint(1, n)
        digits2 = random.randint(1, n)

        # Generate each number
        num1 = random.randint(10 ** (digits1 - 1), 10**digits1 - 1)
        num2 = random.randint(10 ** (digits2 - 1), 10**digits2 - 1)

        # Skip if the pair is in the validation set
        if (num1, num2) in validation_pairs:
            continue
        pairs.append((num1, num2))

    return pairs


class MathsDataset(Dataset):
    """
    Dataset for the multiplication task
    """
    def __init__(
        self,
        max_int: int,
        train: bool = True,
        num_train_samples: int = None,
        val_samples: List = None,
    ):
        if train:
            self.samples = generate_training_set(
                max_int, num_train_samples, val_samples
            )
        else:
            self.samples = list(generate_validation_set(max_int, val_samples))

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> str:
        return self.samples[idx]
