import torch


def sum_one_to_n(n: int) -> int:
    """
    Sum numbers from 1 to n.
    """
    return torch.sum(torch.arange(1, n + 1)).item()
