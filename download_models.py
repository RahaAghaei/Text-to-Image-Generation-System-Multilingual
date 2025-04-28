from stable_diffusion import sdxl
from language_detection import LangID

pipe_path = './models/sdxl-turbo'
LangID_path = "./models/LangID"

sdxl(pipe_path)
LangID(LangID_path)