total=0  #Global variable

def sum(a,b=0):
    """_summary_

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    
    print("a:", a)
    print("b:", b)
    total= a+b   #Local variable 
    print("total inside function:", total)

    return total

n=sum(5,8)
print("total outside function:", total)
