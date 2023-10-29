#pip install pytorch
#pip install transformers
#pip install huggingface_hub
#pip install python-dotenv

#img2text
# Use a pipeline as a high-level helper
from dotenv import find_dotenv,load_dotenv
from transformers import pipeline
load_dotenv(find_dotenv())

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large") 
    #o nome da task "image to text" vem do site https://huggingface.co/tasks

    text = image_to_text(url)[0]["generated_text"]
    print(text)
    return text

img2text("https://i.pinimg.com/564x/0d/9e/cb/0d9ecb13f53004d37df3e2f901590f0f.jpg")

#llm

#text2speech