import sys
import os
import dotenv
from langchain.llms import HuggingFaceHub

dotenv.load_dotenv()

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

hf = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    model_kwargs={"temperature":0.8}
    )

text = "Why did the chicken cross the road?"

print(hf(text))