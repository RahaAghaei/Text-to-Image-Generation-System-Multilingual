from diffusers import AutoPipelineForText2Image
import mediapy as media
import random
import sys
import torch


def sdxl(pipe_path):
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo",
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
        )
    # Save the model to a specific path
    pipe.save_pretrained(pipe_path)

