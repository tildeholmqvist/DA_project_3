import streamlit as st


def about_body():

    st.write("## About This Project")

    st.info(
        "**Data source:** European Forest Fire Information System (EFFIS), "
        "Copernicus Emergency Management Service (European Commission Joint "
        "Research Centre).\n\n"
        "**Coverage:** 31 countries, 1980-2024.\n\n"
        "**License:** Reuse authorised provided the source is acknowledged."
    )

    st.write("### Author")
    st.write("Tilde Holmqvist — Data Analytics & AI Diploma, Code Institute")

    st.write("---")

    st.write(
        "For full methodology, data cleaning steps, and source code, see the "
        "project's GitHub repository."
    )
    st.write(
        "https://github.com/tildeholmqvist/DA_project_3"
    )
