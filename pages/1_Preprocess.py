import streamlit as st
import os
import pandas as pd
import tiktoken
import numpy as np



st.header("Preprocess Data")
try:
    path=st.text_input("Please enter the path to the dataset")
    
    df=pd.read_csv(path)
    data=df['text'].str.cat(sep='\n')
    st.write("Dataset:")
    st.write(df)

    n = len(data)
    train_data = data[:int(n*0.9)]
    val_data = data[int(n*0.9):]

    # encode with tiktoken gpt2 bpe
    enc = tiktoken.get_encoding("gpt2")
    train_ids = enc.encode_ordinary(train_data)
    val_ids = enc.encode_ordinary(val_data)
    st.write(f"Training set has {len(train_ids):,} tokens")
    st.write(f"Validation set has  {len(val_ids):,} tokens")

    # export to bin files
    train_ids = np.array(train_ids, dtype=np.uint16)
    val_ids = np.array(val_ids, dtype=np.uint16)
    train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
    val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
except FileNotFoundError:
    st.warning("Please input a valid file path")
except Exception as e:
    st.warning(e)



#'data/lyrics/spotify_millsongdata.csv'




# train.bin has 301,966 tokens
# val.bin has 36,059 tokens



