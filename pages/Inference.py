import streamlit as st
st.set_page_config(layout="wide")
st.title("INFERENCE")
prompt='python sample.py '
col1, col2,= st.columns((2,2))
with col1:
    model=st.radio("Choose your model",["resume","Pretrained-Model1","Pre-trained Model 2"],
                   captions = ["Select resume if you want to use  custom model", "1555M param","125M param"])
    if model=='resume':
        model=' --init_from=resume'
        saved_model=st.text_input('Enter the saved model folder ("out-folder-name")')
        prompt+=' --out_dir='+saved_model
    elif model=='Pretrained-Model1':
        model=' --init_from=gpt2-xl'
    else:
        model=' --init_from=gpt2'

        
                       
    device_ch=st.radio("Choose your device",["cpu","cuda"],
                    captions=["Select cpu if you dont have a gpu","Select cuda for fast processing"])
    if device_ch=='cpu':
        device=" --device=cpu"
    else:
        device=" --device=cuda"
    if st.button("Inference Documentation"):
      st.switch_page("pages/‎‎.py")
        
        
with col2:
    start=" --start="+st.text_input("Enter the prompt for your GPT")
    st.caption("Please use quotes while providing prompt")
    num_samples=" --num_samples="+st.text_input("Enter the number of samples")
    max_new_token=" --max_new_tokens="+st.text_input("Enter the max token")
    temperature=" --temperature="+st.text_input("Enter temperature")
    top_k=" --top_k="+st.text_input("Enter top k ")
        
        
st.divider()
prompt=prompt+model+device+num_samples+max_new_token+temperature+top_k+num_samples+start
st.write("Command :")
st.code(prompt,language='python')
st.divider()
if st.button("HOME"):
    st.switch_page("HoMe.py")
    
    
    