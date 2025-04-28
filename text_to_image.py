
from Load_models import Load_sdxl, LangID
from languages import LANGUANGE_MAP
import argostranslate.package
import argostranslate.translate
import gradio as gr
import torch

pipe = Load_sdxl()


def text_to_image_multilingual(sentence: str):
    pipe = pipe.to("cuda")
    model, tokenizer = LangID()
    
    tokenized_sentence = tokenizer(sentence, return_tensors='pt')
    output = model(**tokenized_sentence)
    predictions = torch.nn.functional.softmax(output.logits, dim=-1)
    _, preds = torch.max(predictions, dim=-1)
    predicted_language = LANGUANGE_MAP[preds.item()]
    print(predicted_language)

    # Define prompt with the original sentence
    prompt = sentence

    if predicted_language != "English":
        LangID = None  # Default to None if language is not supported
        if predicted_language == "Persian":
            LangID = "fa"
        elif predicted_language == "Arabic":
            LangID = "ar"
        elif predicted_language == "Italian":
            LangID = "it"
        elif predicted_language == "Basque":
            LangID = "eu"
        elif predicted_language == "Catalan":
            LangID = "ca"
        elif predicted_language == "Chinese_China":
            LangID = "ny"
        elif predicted_language == "Polish":
            LangID = "pl"
        elif predicted_language == "Russian":
            LangID = "ru"
        elif predicted_language == "Swedish":
            LangID = "sv"

        if LangID is not None:
            # Perform language detection and translation
            argostranslate.package.update_package_index()
            available_packages = argostranslate.package.get_available_packages()
            package_to_install = next(
                filter(
                    lambda x, LangID=LangID: x.from_code == LangID and x.to_code == "en", available_packages
                )
            )
            argostranslate.package.install_from_path(package_to_install.download())

            # Translate
            translatedText = argostranslate.translate.translate(sentence, LangID, "en")
            prompt = translatedText

    # Image generation
    seed = random.randint(0, sys.maxsize)
    num_inference_steps = 4
    images = pipe(
        prompt=prompt,
        guidance_scale=0.0,
        num_inference_steps=num_inference_steps,
        generator=torch.Generator("cuda").manual_seed(seed),
    ).images

    print(f"Prompt:\t{prompt}\nSeed:\t{seed}")
    media.show_images(images)
    images[0].save("./output/output.jpg")
