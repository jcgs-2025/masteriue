def mean(data):
    """
    Calculate the mean of a list of numbers.
    
    Parameters:
    data (list): A list of numerical values
    
    Returns:
    float: The mean of the data    
    """
    if len(data) == 0:
        return None
    return sum(data) / len(data)

def median(data):
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2