class Calculator:
    @staticmethod
    def multiply(a:int , b : int)-> int:
        """Multiply The integers.
    
    Args:
        a(int): The first Integer
        b(int): The second Integer
        
    Returns: 
        int : The product of a and b"""
    
        return a*b
    
    @staticmethod 
    def calculate_total(*x: float)->float:
        """Calculate sum of given list of numbers"""

        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float , days:int)->float:
        """Calculate Daily Budget"""

        return total / days if days> 0 else 0 