from utils.currency_converter import CurrencyConverter
from typing import List
from langchain.tools import tool 
from dotenv import load_dotenv 
import os 

class CurrencyConverterTool:

    def __init__(self):
        load_dotenv()

        self.api_key = os.environ.get("EXCHANGE_RATE_aPI_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_convertor_tool_list = self._setup_tools()

    def _setup_tools(self)->List:
        """setup all tools for currency convertor tool"""

        @tool
        def convert_currency(amount:float , from_currency:str,to_currency:str):
            """convert amount from one currency to another"""
            return self.currency_service.convert(amount , from_currency,to_currency)
        
        return [convert_currency]
    
    