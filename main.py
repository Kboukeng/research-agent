# Warning control
import warnings

from utils.utils import get_openai_api_key
warnings.filterwarnings('ignore')


import os
from crewAi import crew

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

from IPython.display import Markdown
Markdown(result)

# topic = "machine learning"
# result = crew.kickoff(inputs={"topic": topic})