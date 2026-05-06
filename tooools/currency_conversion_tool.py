from utils.currency_converter import CurrencyConverter
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()


class CurrencyConverterTool:
    def __init__(self):
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        if not self.api_key:
            raise ValueError("EXCHANGE_RATE_API_KEY not found")
        self.currency_service = CurrencyConverter(api_key=self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List[tool]:
        """
        Setup tools for currency conversion
        

        """
        @tool
        def convert_currency(from_currency:str, to_currency:str, amount:float) -> float:
            """
            Convert currency from one currency to another
            
            Args:
            - from_currency: Currency to convert from (e.g., USD)
            - to_currency: Currency to convert to (e.g., EUR)
            - amount: Amount to convert (e.g., 100)
            """
            return self.currency_service.convert(amount=amount, from_currency=from_currency, to_currency=to_currency)
        
        return [convert_currency]