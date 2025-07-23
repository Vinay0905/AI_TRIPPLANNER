from utils.currency_converter  import CurrencyConverter
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
import os

class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key=os.environ.get("EXCHANGE_RATE_API")
        self.currency_service=CurrencyConverter(self.api_key)
        self.currency_converter_tool_list=self.setup_tools()
        


    def setup_tools(self):
        """Setup all tools for the currency converter tool."""
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str):
            """Convert the amount from one currency to another"""
            
            return self.currency_service.convert(amount, from_currency, to_currency)
        
        return [convert_currency]
    

