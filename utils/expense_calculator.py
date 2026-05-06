
class Calculator:
    @staticmethod
    def multiply(self, a:int, b:int) -> int:
        """
        Multiply two integers
        
        Args:
            a: int
            b: int
            
        Returns:
            int: product of a and b
        """
        return a * b
    
    @staticmethod
    def calculate_total_expense(*x:float) -> int:
        """
        Calculate total expense from a list of items
        
        Args:
            items: list of items
            
        Returns:
            int: total expense
        """
        return sum(x)

    @staticmethod
    def calculate_daily_expenses(total:float, days:int)->float:
        """
        Calculate daily expenses from a dictionary of expenses
        
        Args:
            total: total expense
            days: number of days
            
        Returns:
            float: total expense per day
        """
        return total/ days if days> 0 else 0
    