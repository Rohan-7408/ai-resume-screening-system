import streamlit as st
import pandas as pd
import re
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening System")
st.write(
    "Compare resume text with a job description using TF-IDF "
    "and cosine similarity."
)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_resume_text(uploaded_file):
    if uploaded_file.name.lower().endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8", errors="ignore")

    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

    return ""

job_description = st.text_area(
    "Paste the Job Description",
    height=200,
    placeholder="Enter the job requirements here..."
)

uploaded_files = st.file_uploader(
    "Upload resumes (PDF or TXT)",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

threshold = st.slider(
    "Demo similarity threshold (%)",
    min_value=0,
    max_value=100,
    value=30
)

if st.button("Screen Resumes"):
    if not job_description.strip():
        st.warning("Please enter a job description.")

    elif not uploaded_files:
        st.warning("Please upload at least one resume.")

    else:
        candidate_names = []
        resume_texts = []

        for uploaded_file in uploaded_files:
            text = extract_resume_text(uploaded_file)

            if text.strip():
                candidate_names.append(uploaded_file.name)
                resume_texts.append(text)

        if not resume_texts:
            st.error(
                "No readable text found. Scanned PDFs may need OCR."
            )

        else:
            clean_job = preprocess_text(job_description)
            clean_resumes = [
                preprocess_text(text) for text in resume_texts
            ]

            documents = [clean_job] + clean_resumes

            vectorizer = TfidfVectorizer(stop_words="english")
            tfidf_matrix = vectorizer.fit_transform(documents)

            scores = cosine_similarity(
                tfidf_matrix[0:1],
                tfidf_matrix[1:]
            )[0]

            results = pd.DataFrame({
                "Candidate": candidate_names,
                "Match Score (%)": (scores * 100).round(2)
            })

            results = results.sort_values(
                by="Match Score (%)",
                ascending=False
            ).reset_index(drop=True)

            results.index = results.index + 1
            results.index.name = "Rank"

            results["Status"] = results["Match Score (%)"].apply(
                lambda score: (
                    "Meets demo threshold"
                    if score >= threshold
                    else "Below demo threshold"
                )
            )

            st.subheader("Screening Results")
            st.dataframe(results, use_container_width=True)

            st.subheader("Candidate Similarity Scores")
            chart_data = results.set_index("Candidate")[
                "Match Score (%)"
            ]
            st.bar_chart(chart_data)

            csv_data = results.to_csv().encode("utf-8")
            st.download_button(
                "Download Results as CSV",
                data=csv_data,
                file_name="resume_screening_results.csv",
                mime="text/csv"
            )

            st.caption(
                "Similarity scores measure text overlap with the job "
                "description. They are not validated hiring scores "
                "or a substitute for human review."
            )
