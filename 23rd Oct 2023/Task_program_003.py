#Create a function with parameter which can do x^y

def power(x,y):
    """
        This function calculates x^y.

        Args:
            x (int or float): The base.
            y (int or float): The exponent.

        Returns:
            The result of x^y.
        """
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 0:
        return 1 /power(x,-y)
    elif y % 2 == 0:
        return power(power(x, 2), y // 2)
    else:
        return x * power(x, y - 1)
