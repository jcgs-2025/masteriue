def mean(data):
    """
    Function to calculate the mean of a list of numbers
    
    Args:
        data (list): List of numbers
        
    Returns:
        float: Mean of the list of numbers
        
    Raises:
        ZeroDivisionError: If the list is empty
    """
    return sum(data) / len(data)

def median(data):
    """
    Function to calculate the median of a list of numbers
    
    Args:
        data (list): List of numbers
        
    Returns:
        float: Median of the list of numbers
        
    Raises:
        ZeroDivisionError: If the list is empty
    """    
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    return data[n // 2]

def variance(data):
    """
    Function to calculate the variance of a list of numbers
    
    Args:
        data (list): List of numbers
        
    Returns:
        float: Variance of the list of numbers
        
    Raises:
        ZeroDivisionError: If the list is empty
    """
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

def mode(data):
    """
    Function to calculate the mode of a list of numbers
    
    Args:
        data (list): List of numbers
    
    Returns:
        float: Mode of the list of numbers
    
    Raises:
        ZeroDivisionError: If the list
    """
    return max(data, key = data.count)