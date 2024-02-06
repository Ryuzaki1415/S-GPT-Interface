import streamlit as st
import os
import pandas as pd
import tiktoken
import numpy as np
import shutil
import pickle

st.header("Preprocess Data")
choice=st.radio("Choose Tokenization",options=['Tiktoken','Character-level'])
if choice=='Tiktoken':
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
else:
    try: 
        path=st.text_input("Please enter the path to the dataset")
        df=pd.read_csv(path)
        st.write("Dataset:")
        st.write(df)
        data=df['text'].str.cat(sep='\n')
        chars = sorted(list(set(data)))
        vocab_size = len(chars)
        st.write("All the unique characters are :", ' '.join(chars))
        st.write(f"Vocab size: {vocab_size:,}")

        # create a mapping from characters to integers
        stoi = { ch:i for i,ch in enumerate(chars) }
        itos = { i:ch for i,ch in enumerate(chars) }
        def encode(s):
            return [stoi[c] for c in s] # encoder: take a string, output a list of integers
        def decode(l):
            return ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

        # create the train and test splits
        n = len(data)
        train_data = data[:int(n*0.9)]
        val_data = data[int(n*0.9):]

        # encode both to integers
        train_ids = encode(train_data)
        val_ids = encode(val_data)
        st.write(f"train has {len(train_ids):,} tokens")
        st.write(f"val has {len(val_ids):,} tokens")

        # export to bin files
        train_ids = np.array(train_ids, dtype=np.uint16)
        val_ids = np.array(val_ids, dtype=np.uint16)
        train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
        val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

        # save the meta information as well, to help us encode/decode later
        meta = {
            'vocab_size': vocab_size,
            'itos': itos,
            'stoi': stoi,
        }
        with open(os.path.join(os.path.dirname(__file__), 'meta.pkl'), 'wb') as f:
            pickle.dump(meta, f)
    except Exception as e:
        print(e)




#'data/lyrics/spotify_millsongdata.csv'




# train.bin has 301,966 tokens
# val.bin has 36,059 tokens



