import streamlit as st 
col1,col2=st.columns(2,gap="small",vertical_alignment="center")
with col1:
    st.image(r"C:\Users\mk\OneDrive\Pictures\Screenshots\Screenshot 2025-04-16 223545.png",width=230)
with col2:
    st.title("Chatgenie",anchor=False)
    st.write(
        "An AI Powered Virtual Assistant"
    )

st.write("\n")
st.subheader("Welcome to Chatgenie",divider="rainbow",anchor=False)
st.write(
    """ChatGenie is a powerful, all-in-one AI assistant that combines 
       the capabilities of a large language model (LLM) chatbot and an
       advanced image generator. With ChatGenie, users can engage in 
       seamless conversations to answer queries, provide recommendations,
       or explore a variety of topics. Its deep understanding of natural 
       language allows it to provide insightful and relevant responses, 
       making it a valuable companion for any knowledge-seeking individual.
       In addition to its conversational abilities, ChatGenie features a cutting-edge
       image generation system. Users can describe any scene, object, or concept in 
       detail, and ChatGenie will create stunning, customized images based on those 
       descriptions. Whether you need an artistic representation, an illustration 
       for a project, or just want to see your ideas brought to life visually, 
       ChatGenie makes it possible.  
       ChatGenie is your go-to AI assistant for both engaging conversations and unique,
       AI-generated images. Its versatility is perfect for creative professionals, 
       educators, students, and anyone who loves exploring the limitless potential 
       of artificial intelligence.
    """
)

st.write("\n")
st.subheader("Features",anchor=False)
st.write(
    """
    - 🧠 Smart Conversational AI: ChatGenie uses advanced language models to understand and respond naturally to user input.
    - 🎨 PixelSynth: ChatGenie will generate a high-quality image that brings your vision to life using AI-driven image synthesis tools like Stable Diffusion
    - 📁 QueryDocs: Upload PDF or TXT files and ChatGenie can read them, summarize content, or answer questions about the text—making it a powerful study or research companion.
    - 💾 Downloadable Content: Every generated image can be downloaded directly with one click—perfect for presentations, creative projects, or personal use.
    """
)



@st.cache_data
def faq_section():
    st.subheader("FAQs",divider="rainbow")
    
    with st.expander("Q1: What is ChatGenie?"):
        st.write("ChatGenie is an AI-powered assistant that combines a large language model (LLM) chatbot with a text-to-image generator. It can answer questions, have conversations, and create stunning visuals from text descriptions.")

    with st.expander("Q2: How do I generate an image with ChatGenie?"):
        st.write("Simply enter a detailed description of the image you want to generate in the text area and click the 'Generate Image' button. The model will process your input and generate an image based on your description.")

    with st.expander("Q3: Is my data secure on ChatGenie?"):
        st.write(" Yes, ChatGenie includes user authentication, ensuring your chat history, files, and generated content are private and accessible only to you.")

    with st.expander("Q4: Can I use the images commercially?"):
        st.write("Images are generated using AI models that may have specific licensing restrictions. Always check the model’s license before using images for commercial purposes.")

    with st.expander("Q5: What types of files can I upload for Q&A?"):
        st.write(" ChatGenie currently supports .pdf and .txt files. You can ask questions based on the content of these files, and ChatGenie will provide accurate, context-based answers.")

# Display the FAQ
faq_section()