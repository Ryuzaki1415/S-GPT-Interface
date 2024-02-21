import streamlit as st
st.set_page_config(
   initial_sidebar_state="collapsed",
   
)
st.title("S-GPT STUDIO")


tab1, tab2, = st.tabs(["‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Overview‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ","Docs‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ "])




with tab1:
   st.header("Welcome to SGPT Studio! :rocket: :sparkles: ")
   st.subheader("This is your one-stop shop for all your GPT Training needs!")
   st.write("SGPT Studio is a framework designed to empower you in unleashing the full potential of GPT models for your specific tasks. Whether you're a researcher, developer, or enthusiast, SGPT Studio puts the tools you need right at your fingertips.")
   st.write("")
   st.write("")

   st.write("With SGPT Studio, you can easily preprocess your chosen dataset,Customize all the hyperparameters required for training a GPT and then run inference seamlessly.")
   st.page_link("pages/1_Preprocess.py", label="Preprocess your dataset!", icon="🛠️")
   st.page_link("pages/2_Training.py", label="Train Custom GPT", icon="🤖")	
   st.page_link("pages/3_Inference.py", label="Generate!", icon="🔮")	
   st.caption("Please refer to our detailed docs for help")
   

with tab2:
   st.title("Documentation")
   st.markdown('''## Introduction to Generative Pre-trained Transformers (GPTs)

Generative Pre-trained Transformers (GPTs) are state-of-the-art language generation models.They belong to a family of transformer-based models renowned for their ability to generate coherent and contextually relevant text across a wide range of tasks.

GPTs leverage the transformer architecture, consisting of self-attention mechanisms and feedforward neural networks, allowing them to capture long-range dependencies and contextual information effectively. They have achieved remarkable success in various natural language processing (NLP) tasks, including text generation, summarization, translation, and question-answering.

GPTs are pre-trained on massive corpora of text data using unsupervised learning objectives, enabling them to learn rich representations of language patterns and structures. These pre-trained models can then be fine-tuned on specific downstream tasks with supervised learning, further enhancing their performance and adaptability to diverse applications.

               
               ''')
   st.write("The documentation for SGPT studio is divided into two parts.Refer Training docs for help with Training Hyperparameters and Inference docs to help with Inference Hyperparameters.")
   if st.button("Training Docs"):
      st.switch_page("pages/‎ .py")
   if st.button("Inference Docs"):
      st.switch_page("pages/‎‎.py")
   
 