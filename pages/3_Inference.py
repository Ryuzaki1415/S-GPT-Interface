import streamlit as st

st.set_page_config(layout="wide")
st.title("INFERENCE")
prompt='python sample.py '
col1, col2,= st.columns((2,2))
with col1:
    ch_model=st.radio("Choose your model",["resume","Pre-trained Model 1","Pre-trained Model 2","Pre-trained Model 3","Lyrics-Bot","SGPT-ORACLE :red[(beta)]","Code-generation :red[(beta)]"],
                   captions = ["Select resume if you want to use  custom model you trained", "1555M param Text generation ","125M param Text generation","772.7M param Text generation","0.80M param Lyrics Generation","600M param","353.7M param"])
    if ch_model=='resume':
        model=' --init_from=resume'
        saved_model=st.text_input('Enter the saved model folder ("out-folder-name")')
        prompt+=' --out_dir='+saved_model
    elif ch_model=='Pre-trained Model 1':
        model=' --init_from=gpt2-xl'
    elif ch_model=='Pre-trained Model 2':
        model=' --init_from=gpt2'
    elif ch_model=='Pre-trained Model 3':
        model=' --init_from=gpt2-large'
    elif ch_model=="Lyrics-Bot":
        model=' --init_from=resume'
        prompt+=' --out_dir=out-song-10k'
    elif ch_model=="Code-generation :red[(beta)]":
        st.switch_page("pages/Code-gen(beta).py")
    else:
        prompt="python chat.py"    
                       
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
if ch_model=="SGPT-ORACLE :red[(beta)]":
    prompt="python chat.py"
else:
    prompt=prompt+model+device+num_samples+max_new_token+temperature+top_k+num_samples+start
st.write("Command :")
st.code(prompt,language='python')
st.divider()
if st.button("HOME"):
    st.switch_page("HoMe.py")
    
    
    