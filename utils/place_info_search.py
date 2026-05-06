import os
import json
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GogglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key = api_key)
        self.places_tool = GooglePlacesTool(api_wrapper = self.places_wrapper)
        
        
    def google_search_attractions(self, place: str) -> dict:
        """
        Search for attractions in a given place
        
        Args:
            place (str): The place to search for attractions in
            
        Returns:
            dict: The attractions found in the place
        """
        results = self.places_tool.run(f"top attractive places in and around {place}")

        return results

    def google_search_restaurants(self, place: str) -> dict:
        """
        Search for restaurants in a given place
        
        Args:
            place (str): The place to search for restaurants in
            
        Returns:
            dict: The restaurants found in the place
        """
        results = self.places_tool.run(f"top restaurants in and around {place}")

        return results

    def google_search_activity(self, place:str) -> dict:
        """
        Search for activities in a given place
        
        Args:
            place (str): The place to search for activities in
            
        Returns:
            dict: The activities found in the place
        """
        results = self.places_tool.run(f"top activities in and around {place}")


        return results


    def google_search_transportation(self, place:str) -> dict:
        """
        Search for transportation in a given place
        
        Args:
            place (str): The place to search for transportation in
            
        Returns:
            dict: The transportation found in the place
        """
        results = self.places_tool.run(f"what are the different mode of transportation available in {place}")

        return results
        
class TavilyPlaceSearchTool:
    def __init__(self):
        self.tool = TavilySearchResults()

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Search for attractions in a given place
        
        Args:
            place (str): The place to search for attractions in
            
        Returns:
            dict: The attractions found in the place
        """
        results = self.tool.invoke(f"top attractive places in and around {place}")
        if isinstance(results, dict) and results.get('answer'):
            return results['answer']
        return results
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Search for restaurants in a given place
        
        Args:
            place (str): The place to search for restaurants in
            
        Returns:
            dict: The restaurants found in the place
        """
        results = self.tool.invoke(f"top restaurants in and around {place}")

        return results
    
    def tavily_search_activity(self, place:str) -> dict:
        """
        Search for activities in a given place
        
        Args:
            place (str): The place to search for activities in
            
        Returns:
            dict: The activities found in the place
        """
        results = self.tool.invoke(f"top activities in and around {place}")

        return results
    
    def tavily_search_transportation(self, place:str) -> dict:
        """
        Search for transportation in a given place
        
        Args:
            place (str): The place to search for transportation in
            
        Returns:
            dict: The transportation found in the place
        """
        results = self.tool.invoke(f"what are the different mode of transportation available in {place}")

        return results
