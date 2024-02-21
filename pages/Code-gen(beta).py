import streamlit as st



"""
# Welcome to S-GPT Assitant! 
Generate Simple :green[Python] Code using our pretrained model (:red[353.7M ] ) param
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
        st.code(output_code,language="python")
    except:
        st.warning("please provide a prompt")
if st.button("HOME"):
    st.switch_page("HoMe.py")
#add 10 and 15 and store it in VAR 
#print sum
#Call a function FUN to add two numbers A and B
#decode a hex string '4a4b4c' to utf-8.
#if AttributeError exception is caught
#raise an TemplateSyntaxError exception with an argument string "'templatetag' statement takes one argument".
#split instructions by ',' character, substitute the result for styles
#call the function sql_all with 3 arguments: app_config, self.style and connection, substitute the result for statements.
#do nothing
# define the function load_command_class with arguments: app_name and name.
# if num_loopvars is greater than integer 1, unpack is an boolean True, otherwise is an boolean False.
#substitute s1 for s.

