import streamlit as st
from utils import write_message
from agent import generate_response

# tag::setup[]
# Page Config
st.set_page_config("LegalGPT-proto", page_icon=":movie_camera:")
# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the Sid's chatbot!  How can I help you?"},
    ]
# end::session[]

# tag::submit[]
# Submit handler


def write_message(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """
# Submit handler


def handle_submit(message):
    # Handle the response
    with st.spinner('Thinking...'):

        response = generate_response(message)
        write_message('assistant', response)

    # Handle the response
#    with st.spinner('Thinking...'):
 #       # # TODO: Replace this with a call to your LLM
 #       from time import sleep
 #       sleep(1)
 #       write_message('assistant', message)

# end::submit[]


# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    generate_response(prompt)
# end::chat[]
