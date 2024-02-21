import streamlit as st

st.title("Training Hyperparameter documentation")
st.markdown('''
            
            
            # GPT Training Hyperparameters

Below are the hyperparameters commonly used in training and inference with GPT models:

### n_head (Number of Attention Heads)
- **Description:** Number of attention heads in the multi-head self-attention mechanism. Each attention head attends to different parts of the input sequence.
- **Common Standard Value:** 4-12

### num_layers (Number of Transformer Layers)
- **Description:** Total number of transformer layers in the GPT model. Each layer consists of multi-head self-attention and feedforward neural network modules.
- **Common Standard Value:** 4-12

### embedding_dim (Embedding Dimension)
- **Description:** Dimensionality of the input embeddings and the transformer layers' hidden states. It determines the size of the token embeddings and the intermediate representations.
- **Common Standard Value:**  384-768

### dropout (Dropout Probability)
- **Description:** Probability of dropout used for regularization during training. Dropout randomly sets a fraction of input units to zero to prevent overfitting.
- **Common Standard Value:** 0.01

### learning_rate (Learning Rate)
- **Description:** Initial learning rate for optimization algorithms like Adam or SGD. It controls the size of the updates to the model weights during training.
- **Common Standard Value:** 3e-4

### learning_rate_decay (Learning Rate Decay)
- **Description:** Rate at which the learning rate decays over time. Learning rate decay helps the model to converge more effectively by gradually reducing the step size.
- **Common Standard Value:** 0.95

### batch_size (Batch Size)
- **Description:** Number of training examples processed in a single iteration (batch) during training. Larger batch sizes can improve computational efficiency but may require more memory.
- **Common Standard Value:** 32-64

### block_size (Block Size)
- **Description:** Maximum sequence length or block size considered by the model. Inputs longer than this size are truncated or split into multiple blocks for processing.
- **Common Standard Value:** 128-512
            ''')

if st.button("Home"):
    st.switch_page("HoMe.py")
if st.button("Train a GPT!"):
    st.switch_page("pages/2_Training.py")
