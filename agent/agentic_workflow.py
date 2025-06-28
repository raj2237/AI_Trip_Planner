
from langgraph.graph import StateGraph, MessagesState, END , START 
from langgraph.prebuilt import ToolNode , tools_condition
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currency_conversion import CurrencyConverterTool



class GraphBuilder():
    def __init__(self):
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass