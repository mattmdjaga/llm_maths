import itertools
import random
from typing import List, Tuple, Set


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
    n: int, pairs_per_combination: int = 1
) -> Set[Tuple[int, int]]:
    """
    Args:
        n (int): max digits
        pairs_per_combination (int, optional): number of pairs per combination. Defaults to 1.

    Returns:
        (Set[Tuple[int, int]]): list of pairs
    """
    pairs = set()
    for digits1, digits2 in itertools.product(range(1, n + 1), repeat=2):
        while len(pairs) < pairs_per_combination * (digits1 + digits2 - 1):
            num1 = random.randint(10 ** (digits1 - 1), 10**digits1 - 1)
            num2 = random.randint(10 ** (digits2 - 1), 10**digits2 - 1)
            pair = (num1, num2)
            pair_reverse = (num2, num1)

            pairs.update([pair, pair_reverse])

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
        (Set[Tuple[int, int]]): list of pairs
    """
    pairs = list
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
