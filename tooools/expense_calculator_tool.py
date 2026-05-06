from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.tools = self._setup_tools()
    
    def _setup_tools(self):
        '''
        setup all tools for the calculator tool.
        '''
        @tool
        def estimate_total_hotel_cost(price_per_night:str, total_days:float) -> float:
            """
            Estimate the total cost of the hotel stay.
            """
            return self.calculator.multiply(price_per_night, total_days)

        @tool
        def calculate_total_expanse(costs: List[float]) -> float:
            """
            Calculate the total cost of the expenses.
            """
            return self.calculator.add(*costs)

        @tool
        def calculate_daily_expanse_budget(total_cost:float, days:int) -> float:
            """
            Calculate the daily expense budget.
            """
            return self.calculator.calculate_daily_expenses(total_cost, days)

        return [
            estimate_total_hotel_cost,
            calculate_total_expanse,
            calculate_daily_expanse_budget
        ]

        