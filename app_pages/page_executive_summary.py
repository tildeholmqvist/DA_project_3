import streamlit as st
import pandas as pd
import plotly.express as px


def executive_summary_body():

    st.write("## Executive Summary")

    st.info(
        f"This page summarises wildfire trends in Southern Europe "
        f"(1980-2024) in plain language, with a focus on Spain, "
        f"Portugal, France and Greece."
    )

    st.warning(
        f"**Why this matters now:** As of July 2026, France and Spain "
        f"are experiencing severe wildfire activity — France has "
        f"recorded 3.4 times its annual average number of fires "
        f"(Copernicus data, via CNN, 27 July 2026). This dashboard "
        f"analyses historical data (1980-2024) to provide context for "
        f"the current crisis, but the current events themselves are "
        f"not part of the dataset analysed below."
    )

    df = pd.read_csv("inputs/processed/wildfires_long_format.csv")
    focus_countries = ['Spain', 'Portugal', 'France', 'Greece']
    df_focus = df[df['country_name'].isin(focus_countries)]

    st.write("### Burnt Area Over Time")
    fig = px.line(
        df_focus,
        x='Year',
        y='burnt_area_ha',
        color='country_name',
        title=(
            'Burnt Area Over Time: Spain, Portugal, France, '
            'Greece (1980-2024)'
        ),
        labels={
            'burnt_area_ha': 'Burnt Area (hectares)',
            'Year': 'Year',
            'country_name': 'Country'
        }
    )
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.success(
        f"**Key takeaway:** Spain has recorded the highest average "
        f"annual burnt area among these four countries, while France "
        f"has historically had the lowest."
    )
