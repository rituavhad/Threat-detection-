import streamlit as st
from groq import Groq

# Initialize Groq API client with API key
client = Groq(api_key="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")

def analyze_threats(text_input):
    """Uses Groq API to analyze threats in text input."""
    completion = client.chat.completions.create(
        model="qwen-2.5-32b",
        messages=[{"role": "user", "content": text_input}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response

# Streamlit UI
st.title("AI-Powered Threat Detection System")
st.sidebar.header("Threat Analysis Panel")

# User input for log data or text
user_input = st.text_area("Enter network log, email content, or suspicious text:")
if st.button("Analyze Threat"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = analyze_threats(user_input)
            st.subheader("Threat Analysis Result")
            st.write(result)
    else:
        st.warning("Please enter text for analysis.")