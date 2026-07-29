import streamlit as st


def about_body():

    st.write("## About This Project")

    st.info(
        f"**Data source:** European Forest Fire Information System (EFFIS), "
        f"Copernicus Emergency Management Service (European Commission Joint "
        f"Research Centre).\n\n"
        f"**Coverage:** 31 countries, 1980-2024.\n\n"
        f"**License:** Reuse authorised provided the source is acknowledged."
    )

    st.write("### Author")
    st.write("Tilde Holmqvist — Data Analytics & AI Diploma, Code Institute")

    st.write("---")

    st.write(
        f"For full methodology, data cleaning steps, and source code, see the "
        f"project's GitHub repository."
    )
    st.write(
        "https://github.com/tildeholmqvist/DA_project_3"
    )