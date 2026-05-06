
import os
import datetime

def save_document(response_text:str , directory: str = "./output"):
    """Export travel plan to markdown file with proper formatting"""
    os.makedirs(directory, exist_ok=True)

    markdown_content = f"""# AI Travel Agent Plan
    # **Generated:** {datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}
    # **Created By:** Travel Assistant Agent

    {response_text}

    
    """

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{directory}/travel_plan_{timestamp}.md"

        print(filename)

        with open(filename, "w", encoding = "utf-8") as file:
            file.write(markdown_content)
        
        print(f"markdown file saved as : {filename}")
        return filename
    except Exception as e:
        print(f"Error saving travel plan to {filename}: {e}")
        return None

