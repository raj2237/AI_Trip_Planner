import os
from dotenv import load_dotenv
from typing import Literal ,Optional , Any
from pydantic import BaseModel , Field
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.config_loader import load_config
from langchain_groq import ChatGroq

load_dotenv()

class ConfigLoader():
    def __init__(self):
        print(f"Loading COnfig..")
        self.config = load_config()
    def __getitem__(self,key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider = Literal["groq","openai"] = "groq"
    config = Optional[ConfigLoader] = Field(default=None, exclude = True)

    def model_post_init(self,__context:Any)->None:
        self.config = ConfigLoader()

    class Config:
        arbitary_types_allowed = True

    def load_llm(self):
        """Load and return the LLM model"""

        print("LLM LOADING....")
        print("Loading model from the provider: " ,{self.model_provider})
        if self.model_provider == "groq":
            print("Initializing GROQ...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model_name , api_key= groq_api_key)
        
        else:
            print("NAHI HAI")

        return llm