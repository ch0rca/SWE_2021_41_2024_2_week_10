from typing import List

def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and returns a list of even integers.
    
    Args:
        int_list: A list of integers.
        
    Returns:
        A list of even integers from the input list.
    """
    return [num for num in int_list if num % 2 == 0]