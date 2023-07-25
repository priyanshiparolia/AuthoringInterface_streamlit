
import streamlit as st
import pandas as pd
import base64

st.title("Authoring Interface")
def main():
    st.header("Upload and edit the USR")

    #file upload widget
    uploaded_file = st.file_uploader("Choose a usr file", type=["csv", "txt"])

    if uploaded_file is not None:
        # Check the file type and read accordingly
        if uploaded_file.type == "text/csv":
            # Read the uploaded CSV file as a Pandas DataFrame
            df = pd.read_csv(uploaded_file)

            # Display the DataFrame for CSV files
            st.write("Uploaded USR:")
            st.dataframe(df)
        elif uploaded_file.type == "text/plain":
            # Read the uploaded text file as a string
            text_content = uploaded_file.read().decode("utf-8")

            # Display the contents of the text file
            st.write("Uploaded Text File Content:")
            edited_text = st.text_area("Edit the text below:", value=text_content, height=300)

            # button to save the edited text to a file
            if st.button("Save Text"):
                download_link(edited_text, file_name="modified_USR.txt")

def download_link(text_content, file_name):

    # Encode the text content to base64
    b64_text = base64.b64encode(text_content.encode()).decode()

    # Create a download button with the encoded content
    href = f'<a href="data:text/plain;charset=utf-8;base64,{b64_text}" download="{file_name}">Download {file_name}</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

