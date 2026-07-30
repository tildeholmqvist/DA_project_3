import streamlit as st
import pandas as pd
import plotly.express as px


def executive_summary_body():

    st.write("## Executive Summary")

    st.info(
        f"This page summarises wildfire trends in Southern Europe (1980-2024) "
        f"in plain language, with a focus on Spain, Portugal, France and Greece."
    )

    st.warning(
        f"**Why this matters now:** As of July 2026, France and Spain are "
        f"experiencing severe wildfire activity — France has recorded 3.4 "
        f"times its annual average number of fires (Copernicus data, via CNN, "
        f"27 July 2026). This dashboard analyses historical data (1980-2024) "
        f"to provide context for the current crisis, but the current events "
        f"themselves are not part of the dataset analysed below."
    )

    df = pd.read_csv("inputs/processed/wildfires_long_format.csv")
    focus_countries = ['Spain', 'Portugal', 'France', 'Greece']
    df_focus = df[df['country_name'].isin(focus_countries)]

    st.write("### Burnt Area Over Time")
    fig = px.line(df_focus, x='Year', y='burnt_area_ha', color='country_name',
                  title='Burnt Area Over Time: Spain, Portugal, France, Greece (1980-2024)',
                  labels={'burnt_area_ha': 'Burnt Area (hectares)', 'Year': 'Year', 'country_name': 'Country'})
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.success(
        f"**Key takeaway:** Spain has recorded the highest average annual "
        f"burnt area among these four countries, while France has historically "
        f"had the lowest."
    )