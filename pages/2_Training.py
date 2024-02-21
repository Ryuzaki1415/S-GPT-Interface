import streamlit as st

st.set_page_config(layout="wide")
prompt='python train.py config/'
st.title("TRAIN A GPT!")
col1, col2,= st.columns((2,2))

with col1:
    st.write("Structural Hyperparameters")
    file_name='train_template.py'
    out_dir=" --out_dir="+st.text_input("Enter Folder name to store checkpoint")
    st.caption("enter name as 'out-folder_name'")
    choice = st.radio(
    "Enter Device",
    [":rainbow[CPU]", "***CUDA***"],
    captions = ["Select if your device does not support CUDA.", "Use CUDA for faster training"])
    if choice == ':rainbow[CPU]':
        device=' --device=cpu'
    else:
        device=" --device=cuda"
    n_head=' --n_head='+st.text_input('Number of attention heads')
    n_layer=' --n_layer='+st.text_input("enter number of layers")
    n_embed=' --n_embd='+st.text_input("enter embedding dimension")
    dropout=' --dropout='+st.text_input("enter dropout rate")
    if st.button("Training Documentation"):
      st.switch_page("pages/‎ .py")
with col2:
    st.write("Learning Rate")
    learning_rate=" --learning_rate="+st.text_input('enter learning rate')
    choice = st.radio(
    "Save Checkpoints",
    ["***True***", "***False***"],
    captions=['‎ ‎ ‎ ','‎ ‎ ‎ '],index=1,help="Select False if you want to save checkpoints only when the val_accuracy improves")

    if choice == '***True***':
        save=' --always_save_checkpoint='+'True'
    else:
        save=' --always_save_checkpoint='+'False'
    min_lr=' --min_lr='+st.text_input('enter minimum learning rate')
    max_iters=' --max_iters='+st.text_input('enter maximum number of iterations')
    lr_decay=' --lr_decay_iters='+st.text_input('enter learning rate decay iterations')
    block_size=' --block_size='+st.text_input('enter Block size')
    batch_size=' --batch_size='+st.text_input('enter Batch size')

    
st.divider()
prompt=prompt+file_name+n_head+n_layer+device+dropout+save+block_size+learning_rate+min_lr+lr_decay+max_iters+batch_size+out_dir+n_embed
#st.write(f"the prompt is {prompt}")
code = prompt
st.write("Command :")
st.code(code, language='python')
st.divider()
if st.button("HOME"):
    st.switch_page("HoMe.py")
if st.button("Continue to Inference"):
    st.switch_page("pages/3_Inference.py")