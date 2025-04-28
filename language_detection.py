
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import gradio as gr
import torch

def LangID(LangID_path):

    model_ckpt = "ivanlau/language-detection-fine-tuned-on-xlm-roberta-base"
    model = AutoModelForSequenceClassification.from_pretrained(model_ckpt)
    tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

    # Save the model and tokenizer to the specified path
    model.save_pretrained(LangID_path)
    tokenizer.save_pretrained(LangID_path)

