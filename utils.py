



def zero_padding_multiplicatn(num_1: int, num_2: int, padding_size: int = 0, reverse: bool = False) -> str:
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
    answer = str(answer).reverse() if reverse else str(answer)
    answer = "0" * (padding_size - len(answer)) + answer if padding_size else answer
    return f"{num_1} * {num_2} = {answer}"