from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

st.header("Research Assistant")
chat = ChatOpenAI(
      model='gpt-4o',
      temperature= 1.0,
  )
research_paper = st.selectbox("Select Paper:",
                          [
                            "Attention Is All You Need",
                            "Deep Residual Learning for Image Recognition",
                            "Generative Adversarial Nets",
                            "Sequence to Sequence Learning with Neural Networks",
                            "Adam: A Method for Stochastic Optimization",
                            "Playing Atari with Deep Reinforcement Learning",
                            "Neural Machine Translation by Jointly Learning to Align and Translate",
                            "ImageNet Classification with Deep Convolutional Neural Networks",
                            "Long Short-Term Memory",
                            "Auto-Encoding Variational Bayes"
                          ])

type = st.selectbox("Select Type:",
                          [
                            "Abstract",
                            "Introduction",
                            "Methodology",
                            "Results",
                            "Conclusion",
                            "References",
                            'Mathematical',
                            'Code',
                          ])
length_of_reply = st.selectbox("Length of Reply:",
                          [
                            "Short",
                            "Medium",
                            "Long",
                          ])


template_ = load_prompt('template.json')

if st.button("Submit"):
    chain = template_ | chat
   
    result = chain.invoke(
        {
            'research_paper': research_paper,
            'type': type,
            'length_of_reply': length_of_reply,
        }
    )

    st.write(result.content)