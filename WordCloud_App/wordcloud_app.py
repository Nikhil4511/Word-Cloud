import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import PyPDF2
from docx import Document
import base64
from io import BytesIO

# File Readers
def read_file(file):
    return file.getvalue().decode("utf-8")

def read_docx(file):
    doc = Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def read_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Stopword Filter
def filter_stopwords(text, additional_stopwords=[]):
    words = text.split()
    all_stopwords = STOPWORDS.union(set(additional_stopwords))
    filtered_words = [w for w in words if w.lower() not in all_stopwords]
    return " ".join(filtered_words)

# Download Helpers
def get_image_download_link(buffered, format_):
    """Generate a download link for wordcloud image"""
    image_base64 = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/{format_};base64,{image_base64}" download="wordcloud.{format_}">Download {format_.upper()} Image</a>'
    return href

def get_table_download_link(df, filename, file_label):
    """Generate a download link for word frequency table"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">{file_label}</a>'

# Streamlit App
st.title("📊 WordCloud Generator")
st.subheader("Create WordClouds from Text, PDF, or DOCX files")

uploader_file = st.file_uploader("Upload a Text, PDF, or DOCX file", type=['txt', 'pdf', 'docx'])

if uploader_file:
    file_details = {"FileName": uploader_file.name, "FileType": uploader_file.type, "FileSize": uploader_file.size}
    st.write(file_details)

    # Detect file type
    if uploader_file.type == "text/plain":
        text = read_file(uploader_file)
    elif uploader_file.type == "application/pdf":
        text = read_pdf(uploader_file)
    elif uploader_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = read_docx(uploader_file)
    else:
        st.error("Unsupported file type!")
        st.stop()

    # Word Count Table
    words = text.split()
    word_count = pd.DataFrame(words, columns=['Word']).groupby('Word').size().reset_index(name='Count')
    word_count = word_count.sort_values(by='Count', ascending=False)

    # Sidebar Options
    use_standard_stopwords = st.sidebar.checkbox("Use Standard Stopwords", value=True)
    top_words = word_count['Word'].head(50).tolist()
    additional_stopwords = st.sidebar.multiselect("Select Additional Stopwords to Remove", sorted(top_words))

    if use_standard_stopwords:
        all_stopwords = STOPWORDS.union(set(additional_stopwords))
    else:
        all_stopwords = set(additional_stopwords)

    text = filter_stopwords(text, all_stopwords)

    if text.strip():
        # WordCloud dimensions
        width = st.sidebar.slider("Select Word Cloud Width", 400, 2000, 1200, 50)
        height = st.sidebar.slider("Select Word Cloud Height", 200, 2000, 800, 50)

        # Generate WordCloud
        st.subheader("Generated WordCloud")
        fig, ax = plt.subplots(figsize=(width/100, height/100))
        wordcloud_img = WordCloud(width=width, height=height, background_color='white', max_words=200).generate(text)
        ax.imshow(wordcloud_img, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Save Plot Option
        format_ = st.sidebar.selectbox("Select Image Format", ["png", "jpg"])
        buffered = BytesIO()
        fig.savefig(buffered, format=format_)
        st.markdown(get_image_download_link(buffered, format_), unsafe_allow_html=True)

        # Word Frequency Table
        st.subheader("Word Frequency Table")
        st.dataframe(word_count)

        # Word Search Feature
        
        search_word = st.text_input("🔍 Search for a specific word")
        if search_word:
            result = word_count[word_count['Word'].str.lower() == search_word.lower()]
            if not result.empty:
                st.success(f"✅ '{search_word}' found with count: {result['Count'].values[0]}")
            else:
                st.error(f"❌ '{search_word}' not found in the text!")

        # Download CSV link
        st.markdown(get_table_download_link(word_count, "word_count.csv", "📥 Download Word Frequency CSV"), unsafe_allow_html=True)

    else:
        st.warning("No text remaining after stopword removal!")
