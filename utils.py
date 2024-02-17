from langchain.chat_models import ChatOpenAI

from constants import chat_openai_model_kwargs, langchain_chat_kwargs

import os
# Optional, set the API key for OpenAI if it's not set in the environment.
# os.environ["OPENAI_API_KEY"] = "xxxxxx"
os.environ["OPENAI_API_KEY"] = "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"

def get_chat_openai(model_name):
    """
    Returns an instance of the ChatOpenAI class initialized with the specified model name.

    Args:
        model_name (str): The name of the model to use.

    Returns:
        ChatOpenAI: An instance of the ChatOpenAI class.

    """
    llm = ChatOpenAI(
        model_name=model_name,
        model_kwargs=chat_openai_model_kwargs,
        **langchain_chat_kwargs
    )
    return llm
