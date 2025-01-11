# Step 1: Import necessary libraries
import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv 
from smolagents import CodeAgent, LiteLLMModel, tool, GradioUI 


# Step 2: Load environment variables, including API keys, from a .env file
load_dotenv()  


# Step 3: Define the Language Model (LLM). Here, we use Google's Gemini model
model = LiteLLMModel(model_id="gemini/gemini-1.5-flash",  api_key=os.environ["GOOGLE_API_KEY"])


# Step 4: Define a custom tool for loading the Titanic dataset, tailored to our EDA task,
@tool
def get_titanic_data() -> dict:
    """Returns titanic dataset in a dictionary format.
    """    
    df = sns.load_dataset('titanic')    
    return df.to_dict()

@tool
def save_data(dataset:dict, file_name:str) -> None:
    """Takes the dataset in a dictionary format and saves it as a csv file.

       Args:
           dataset: dataset in a dictionary format
           file_name: name of the file of the saved dataset
    """    
    df = pd.DataFrame(dataset)
    df.to_csv(f'{file_name}.csv', index = False)    


# Step 5: Define the Agent
# Using SmolAgents, we configure the agent with tools, the chosen LLM, and authorized library imports
agent = CodeAgent(tools=[get_titanic_data, save_data],    
                  model=model, 
                  additional_authorized_imports=['numpy', 'pandas', 'matplotlib.pyplot', 'sklearn'],)


# Step 6: Launch a user-friendly chat interface with a single line of code
GradioUI(agent).launch()
