# Text to Image Generation System (Multilingual)

Welcome to the **Text-to-Image Generation System**, a multilingual AI project that transforms your ideas into vivid images.  
This system automatically detects the input language, translates non-English prompts into English, and generates high-quality images using **Stable Diffusion XL Turbo**.

---

## 🚀 Overview

With the rise of generative AI, the need for multilingual and intuitive interfaces has grown significantly.  
This project bridges the gap by combining **language detection**, **automatic translation**, and **powerful diffusion models** to create a seamless text-to-image generation experience.

---

## ✨ Features

- **Multilingual Input**: Supports prompt generation in 10 different languages.
- **Automatic Language Detection**: Fine-tuned XLM-Roberta model.
- **Seamless Translation**: Powered by Argos Translate.
- **High-Quality Image Generation**: Based on Stable Diffusion XL Turbo.
- **Multiple Image Outputs**: Generate multiple diverse images per prompt.
- **Simple Deployment**: Minimal setup needed.

---

## 🌍 Supported Languages

- Persian
- Arabic
- Italian
- Basque
- Catalan
- Chinese (China)
- Polish
- Russian
- Swedish
- English (no translation needed)

---

## 🛠 Technologies Used

- [diffusers](https://huggingface.co/docs/diffusers/index)
- [transformers](https://huggingface.co/docs/transformers/index)
- [torch (PyTorch)](https://pytorch.org/)
- [argostranslate](https://argosopentech.com/)
- [mediapy](https://pypi.org/project/mediapy/)
- [gradio](https://gradio.app/) (optional for UI extension)

---

## 📦 Installation

First, clone the repository:

```bash
git clone https://github.com/your-username/text-to-image-generation.git
cd text-to-image-generation
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ⚡ How to Run the Project

> **Step 1 – Download the Models**  
> Before running the system, you must first download the pre-trained models:

```bash
python download_models.py
```
(This will automatically download and prepare all the required models.)

> **Step 2 – Run the Notebook**  
> After downloading the models, simply open and run the notebook:

```bash
run.ipynb
```

✅ That’s it! The system will automatically detect language, translate if needed, and generate images based on your input.

---

## 📊 Example

Input (Persian):

> "یک گربه‌ی سفید با چشمان آبی در یک باغ پر از گل"

Output:

- Language Detected: **Persian**
- Prompt After Translation: **"A white cat with blue eyes in a garden full of flowers"**
- Generated Images: ✅ (Saved under `output/` folder)

---

## 🙌 Acknowledgments

- Hugging Face for `diffusers` and `transformers`
- Argos OpenTech for open-source translation models
- Stability AI for Stable Diffusion XL Turbo

---

# 🎨 Unlock your imagination — in any language.
