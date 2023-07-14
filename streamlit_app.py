import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="📝🔗 Proposal Outline Generator App using ChatGPT")
st.title('📝🔗 Proposal Outline Generator App using ChatGPT')
st.subheader('by the Origo Team')
openai_api_key = st.secrets["openai_api_key"]

def generate_response(topic,business):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
  # Prompt
  template = 'As an experienced contractor with the name of my business {business}, generate a base one-page proposal that includes an introductory section, quote section with a table to be filled out later, and contact section about {topic}.'
  prompt = PromptTemplate(input_variables=['topic','business'], template=template)
  prompt_query = prompt.format(topic=topic, business=business)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('business_form'):
  topic_text = st.text_input('Enter your business expertise:', '')
  namebusiness_text = st.text_input('Enter the name of your business:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(topic_text,namebusiness_text)
