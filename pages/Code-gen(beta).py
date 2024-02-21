import streamlit as st


st.write("S-GPT ASSISTANT")

"""
Generate Code with a trained model
"""

from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("AhmedSSoliman/MarianCG-DJANGO")
tokenizer = AutoTokenizer.from_pretrained("AhmedSSoliman/MarianCG-DJANGO")


with st.form(key='my_form'):
	user_input = st.text_input(label='Enter Prompt')
	submit_button = st.form_submit_button(label='Submit')


if submit_button:
    try:
#NL_input = "define the method help with two arguments a and b"
        output = model.generate(**tokenizer(user_input, padding="max_length", truncation=True, max_length=512, return_tensors="pt"))
        output_code = tokenizer.decode(output[0], skip_special_tokens=True)
        st.write(output_code)
    except:
        st.warning("please provide a prompt")
