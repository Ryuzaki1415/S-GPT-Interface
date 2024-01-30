import streamlit as st

st.set_page_config(layout="wide")
prompt='python train.py/config/'
st.title("TRAIN A GPT!")
col1, col2,= st.columns((2,2))

with col1:
    st.write("Structural Hyperparameters")
    file_name=st.text_input("enter file name")
    choice = st.radio(
    "Enter Device",
    [":rainbow[CPU]", "***CUDA***"],
    captions = ["Select if your device does not support CUDA.", "Use CUDA for faster training"])
    if choice == ':rainbow[CPU]':
        device=' --device=cpu'
    else:
        device=" --device=cuda"
    n_head=' --n_head='+st.text_input('enter number of attention heads')
    n_layer=' --n_layer='+st.text_input("enter number of layers")
    n_embed=' --n_embed='+st.text_input("enter embedding dimension")
    dropout=' --dropout='+st.text_input("enter dropout rate")
with col2:
    st.write("Learning Rate")
    learning_rate=st.text_input('enter learning rate')
    choice = st.radio(
    "Save Checkpoints",
    ["***True***", "***False***"],
    captions=['False if only save when val accuracy improves','‎ ‎ ‎ '])

    if choice == '***True***':
        save=' --save_checkpoints='+'True'
    else:
        save=' --save_checkpoints='+'False'
    min_lr=' --min_lr='+st.text_input('enter minimum learning rate')
    lr_decay=' --lr_decay='+st.text_input('enter learning rate decay iterations')
    max_iters=' --max_iters='+st.text_input('enter maximum number of iterations')
    block_size=' --block_size='+st.text_input('enter Block size')
    batch_size=' --batch_size='+st.text_input('enter Batch size')

    
st.divider()
prompt=prompt+file_name+n_head+n_layer+device+dropout+save+block_size+min_lr+lr_decay+max_iters+block_size+batch_size
#st.write(f"the prompt is {prompt}")
code = prompt
st.code(code, language='python')