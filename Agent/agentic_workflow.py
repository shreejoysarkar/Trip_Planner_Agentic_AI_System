from utils.model_loader import ModelLoader 
from prompt_library.prompt import SystemPrompt
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuild import ToolNode, tools_condition

from tooools.weather_info_tool import WeatherInfoTool
from tooools.place_search_tool import PlaceSearchTool
from tooools.currency_conversion_tool import CurrencyConversionTool
from tooools.expense_calculator_tool import CalculatorTool



class GraphBuilder():
    def __init__(self, model_provider : str = "groq"):
        self.model_provider = model_provider
        self.llm = self.ModelLoader.load_llm()

        self.tools = []
        
        self.weather_info_tool = WeatherInfoTool()
        self.place_search_tool = PlaceSearchTool()
        self.currency_conversion_tool = CurrencyConversionTool()
        self.calculator_tool = CalculatorTool()

        self.tools.extend([*self.weather_info_tool.weather_tools_list,
                            *self.place_search_tool.place_search_tools_list,
                            *self.currency_conversion_tool.currency_conversion_tools_list,
                            *self.calculator_tool.calculator_tools_list])
        
        self.llm_with_tools = self.llm.bind_tools(tools = self.tools)
        
        self.graph = None


        self.system_prompt = SystemPrompt()

    def agent_function(self):
        """main agent function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages" : [response]}

    def build_graph(self):
        """
        build the graph for the agentic workflow. The graph should have the following structure:
        """
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools = self.tools))
        graph_builder.add_edge(START , "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent", END)

    
        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()
     