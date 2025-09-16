import streamlit as st
import pathlib
import requests
import uuid
from streamlit_extras.floating_button import floating_button

WEBHOOK_URL = "https://sap-hackathon.app.n8n.cloud/webhook/bf4dd093-bb02-472c-9454-7ab9af97bd1d"  # Webhook URL
BEARER_TOKEN = st.secrets.get("BEARER_TOKEN")  # Token for authorization

def generate_session_id():
    return str(uuid.uuid4())

def send_message_to_llm(session_id, message):

    headers = {
        "Authorization": BEARER_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "sessionId": session_id,
        "chatInput": message
    }
    print(session_id)
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error: {response.status_code} - {response.text}"

@st.dialog("Chat with LLM", width="large")
def chat_dialog():
    # Create a container for chat messages with fixed height
    messages_container = st.container(height=400, border=False)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = generate_session_id()
    if "welcomed" not in st.session_state:
        st.session_state.welcomed = False
        
    # Initial welcome message
    if not st.session_state.welcomed:
        welcome_message = send_message_to_llm(st.session_state.session_id, "Hi.")
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})
        st.session_state.welcomed = True
        
    # Display messages in the container
    with messages_container:
        # Display all messages from session state
        for message in st.session_state.messages:
            st.chat_message(message["role"]).write(message["content"])

    # Chat input (placed below the messages container in the UI)
    user_input = st.chat_input("Type a message...")

    # Handle new user input
    if user_input:
        messages_container.chat_message("user").write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get LLM response        
        llm_response = send_message_to_llm(st.session_state.session_id, user_input)

        # Add bot response to chat history
        messages_container.chat_message("assistant").write(llm_response)
        st.session_state.messages.append({"role": "assistant","content": llm_response})

st.set_page_config(layout="wide")
left, center, right = st.columns(3, gap=None)

st.html("""<style>
        .stMainBlockContainer {
            padding-left: 0rem;
            padding-right: 0rem;
            padding-top: 2rem;
            padding-bottom: 0rem;
        }
        </style>""")

with open(pathlib.Path("./index.html")) as file:
    st.components.v1.html(file.read(), height=5415)
    if floating_button(":material/chat: Chat"):
        chat_dialog()
    
