import requests

class CurrencyConverter:
    def __init__(self, api_key:str):
        self.base_url  = f"https://v6.exchangerate-api.com/v6/{api_key}/latest"
    

    def convert(self, amount: float, from_currency: str, to_currency:str):
        """
        Convert an amount from one currency to another currency
        
        Args:
            amount (float): The amount to convert
            from_currency (str): The currency to convert from
            to_currency (str): The currency to convert to
            
        Returns:
            float: The converted amount
        """
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to fetch exchange rates")
        rates = response.json()["conversion_rates"]
        if to_currency not in rates:
            raise Exception(f"Currency {to_currency} not found")
        
        return amount * rates[to_currency]
    