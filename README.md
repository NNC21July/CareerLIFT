# 🚀 StreamlitApp_RAG_n8n

This repository demonstrates how quickly you can launch a **web app** using **n8n** and **Streamlit**.

## ✅ Prerequisites
Before running the app, ensure you have:
- **Python 3.8+** installed.
- **Virtual environment (venv)** support.
- **Streamlit** and dependencies installed.

---

## **🔧 Step 1: Clone the Repository**
First, clone this repository to your local machine:
```bash
git clone https://github.com/Josh1313/Streamlit_n8n_chat_llm.git
cd StreamlitApp_RAG_n8n
```
## **🔧 Step 1.1: Configure  Main.py**
1. Navigate to the `main.py` file.
2. Open `main.py` with a text editor.
3. Update your **WEBHOOK N8N**.

Example:
```main.py
[configuration]
WEBHOOK_URL = Your webhook from n8n
```

---

## **🔐 Step 2: Configure Secrets**
1. Navigate to the `.streamlit` folder.
2. Open `secrets.toml` with a text editor.
3. Update your **BEARER_TOKEN**as needed.

Example:
```toml
[secrets]
BEARER_TOKEN = Your new credentials
```
🔹 **Save the file before proceeding.**

---

## **🐍 Step 3: Create a Virtual Environment**
To ensure a clean environment, create and activate a **virtual environment**:

```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Linux/macOS)
venv\Scripts\activate  # Activate (Windows)
```

---

## **📦 Step 4: Install Dependencies**
Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## **🚀 Step 5: Run the Streamlit App**
Now, launch the Streamlit app with the following command:

```bash
streamlit run main.py
```

---

## **⭐ Support the Project**
If you find this repository useful, **don't forget to ⭐ Star it!**  
This helps others discover it and ensures you stay updated with new improvements.

---

## **🔍 Troubleshooting**
If you encounter issues, try the following:
- Ensure **Python 3.8+** is installed.
- Run `pip install --upgrade pip` before installing dependencies.
- Check for missing **API secrets** in `secrets.toml`.

---

🔥 **Now your Streamlit app is live and integrated with n8n!** 🚀  
```

---

### **📌 Key Improvements:**
✅ **Clear, step-by-step structure** from setup to execution.  
✅ **Ensures commands are copy-paste ready** for a smooth experience.  
✅ **Includes a "Support the Project" section** encouraging users to ⭐ the repo.  
✅ **Troubleshooting section** to help users debug issues quickly.  

**Now it's ready to be shared!** 🚀✨
