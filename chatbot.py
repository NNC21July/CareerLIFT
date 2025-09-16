import streamlit as st
import requests
import uuid

# Configuration
WEBHOOK_URL = "https://saphackathon.app.n8n.cloud/webhook-test/4aa98dab-badc-473c-8f84-6eead51af033"  # Webhook URL
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
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Chat with LLM")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = generate_session_id()

    # Initial welcome message
    welcome_message = send_message_to_llm(st.session_state.session_id, "Hi.")
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Get LLM response
        llm_response = send_message_to_llm(st.session_state.session_id, user_input)

        # Add LLM response to chat history
        st.session_state.messages.append({"role": "assistant", "content": llm_response})
        with st.chat_message("assistant"):
            st.write(llm_response)

if __name__ == "__main__":
    main()