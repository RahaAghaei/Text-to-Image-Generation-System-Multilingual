from diffusers import AutoPipelineForText2Image
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import gradio as gr
import torch



def Load_sdxl():
    # To re-upload the downloaded model and tokenizer from the saved path
    sdxl_path = './models/sdxl-turbo'
    pipe = AutoPipelineForText2Image.from_pretrained(sdxl_path)
    


def Load_LangID():
    # To re-upload the downloaded model and tokenizer from the saved path
    LangID_path = './models/LangID'
    model = AutoModelForSequenceClassification.from_pretrained(LangID_path)
    tokenizer = AutoTokenizer.from_pretrained(LangID_path)