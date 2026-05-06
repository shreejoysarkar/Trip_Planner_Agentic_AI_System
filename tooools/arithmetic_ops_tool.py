import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper


@tool
def multiply(a:int, b:int) -> int:
    """ multiply two number

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: multipliaction of a and b
    """


    return a*b

@tool
def add(a:int, b:int)-> int:
    """add two number

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: add a and b
    """
    return a+b

@tool
def currency_converter(from_curr: str, to_curr: str, value: float) -> float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv("ALPHAVANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    exchange_rate = response["Realtime Currency Exchange Rate"]["5. Exchange Rage"]
    return value * float(exchange_rate)