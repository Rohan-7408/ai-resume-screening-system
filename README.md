AI Resume Screening System

An NLP-based AI Resume Screening System that analyzes resumes against a job description, calculates text similarity scores using TF-IDF and Cosine Similarity, and ranks candidates for review.

Live Demo

🚀 "Launch AI Resume Screening System" (https://ai-resume-screening-system-p6gtjd2ghmugrbwz6b8ncc.streamlit.app/)

Project Overview

The AI Resume Screening System helps demonstrate how Natural Language Processing (NLP) techniques can be used to compare candidate resumes with a given job description.

Users can enter a job description, upload resumes in PDF or TXT format, and view similarity scores and a ranked list of candidates.

This project was developed as part of the Sqrock IT Solutions Data Science Internship – Phase 1.

Features

- Enter a job description for a target role.
- Upload candidate resumes in PDF or TXT format.
- Extract text from uploaded resumes.
- Convert resume and job description text into TF-IDF vectors.
- Calculate similarity using Cosine Similarity.
- Rank candidates based on similarity scores.
- Set a configurable shortlisting threshold.
- Visualize candidate similarity scores using a chart.
- Download candidate results as a CSV file.

Technologies Used

- Python – Core programming language
- Streamlit – Web application interface
- Pandas – Data handling and result management
- Scikit-learn – TF-IDF vectorization and Cosine Similarity
- pypdf – Extracting text from PDF resumes

How It Works

1. The user enters a job description.
2. The user uploads one or more resumes.
3. Text is extracted from each uploaded resume.
4. TF-IDF converts the job description and resume text into numerical vectors.
5. Cosine Similarity calculates the textual similarity between each resume and the job description.
6. Candidates are ranked according to their similarity scores.
7. Results are displayed in a table and chart, with an option to download them as a CSV file.

Project Structure

ai-resume-screening-system/
│
├── app.py
├── requirements.txt
└── README.md

Installation and Local Setup

1. Clone the repository

Replace "YOUR-GITHUB-USERNAME" with your GitHub username.

git clone https://github.com/YOUR-GITHUB-USERNAME/ai-resume-screening-system.git

2. Navigate to the project directory

cd ai-resume-screening-system

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open locally in your browser.

Requirements

The project dependencies are listed in "requirements.txt":

streamlit
pandas
scikit-learn
pypdf

Important Notes and Limitations

- Similarity scores represent textual similarity between a resume and the job description. They are not validated measures of candidate suitability or hiring potential.
- The shortlisting threshold is configurable and should be treated as a demonstration setting, not a validated hiring rule.
- Scanned PDFs may not work correctly because they require Optical Character Recognition (OCR) to extract text.
- Resume screening results should be reviewed by a human and should not be used as the sole basis for hiring decisions.
- The system may be affected by resume formatting, wording, and the amount of text available.

Internship

Organization: Sqrock IT Solutions
Program: Data Science Internship
Phase: Phase 1
Project: AI Resume Screening System

Author

Akhand Pratap Vishwakarma
B.Tech – Computer Science & Engineering
NITRA Technical Campus (AKTU)

Live Application

"https://ai-resume-screening-system-p6gtjd2ghmugrbwz6b8ncc.streamlit.app/" (https://ai-resume-screening-system-p6gtjd2ghmugrbwz6b8ncc.streamlit.app/)

---

Developed for learning and demonstration purposes as part of the Data Science Internship.
