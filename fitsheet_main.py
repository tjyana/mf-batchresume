import streamlit as st
# from fitsheet_functions import fit_sheet

# dummy code for the demo. add back code later

# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# additional features:
# job match mode: take resume input > compare to JD database and find best matches
# pdf upload: upload resume and JD as pdfs

def main():
    # Title
    st.sidebar.title("ResumeFit")
    st.sidebar.write("""Upload resumes to see how well they fit a job description.""")

    # Input fields
    resume_files = st.sidebar.text_area("Resume Files", height=200)
    jd_text = st.sidebar.text_area("Job Description", height=200)

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.resume_files = resume_files
        st.session_state.jd_text = jd_text
        st.header("Fit Scores")
        # output = fit_sheet(resume_files, jd_text)
        process_inputs()


def process_inputs():
    # Function to display the final output
    # Process the inputs here
    # st.dataframe(" ", input1)
    st.image('image.png')


if __name__ == "__main__":
    main()
