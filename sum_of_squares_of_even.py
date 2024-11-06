from typing import List
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list.
    
    Args:
        even_int_list: A list of even integers.
        
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    return sum(num ** 2 for num in even_int_list)