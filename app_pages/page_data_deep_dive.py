import streamlit as st
import pandas as pd
import plotly.express as px


def data_deep_dive_body():

    st.write("## Data & Trends Deep Dive")

    st.info(
        f"This page takes a closer look at wildfire patterns in Spain, "
        f"Portugal, France, and Greece (1980-2024), and compares them to "
        f"the rest of Europe."
    )

    # --- Hypothesis, stated BEFORE any data is shown ---
    st.write("### Hypothesis")
    st.info(
        f"**H1:** Wildfire severity in Southern Europe is not uniform "
        f"across countries — some countries experience frequent, smaller "
        f"fires, while others experience rarer but more severe fires, "
        f"despite sharing a similar Mediterranean climate."
    )

    # Load the processed dataset
    df = pd.read_csv("inputs/processed/wildfires_long_format.csv")

    # Filter down to the four focus countries
    focus_countries = ['Spain', 'Portugal', 'France', 'Greece']
    df_focus = df[df['country_name'].isin(focus_countries)]

    # --- Section 1: Burnt area trends over time ---
    st.write("### Burnt Area Over Time")

    fig = px.line(df_focus, x='Year', y='burnt_area_ha', color='country_name',
                  title='Burnt Area Over Time: Spain, Portugal, France, Greece (1980-2024)',
                  labels={'burnt_area_ha': 'Burnt Area (hectares)', 'Year': 'Year', 'country_name': 'Country'})
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.write(
        f"Spain shows the largest year-to-year swings, with several years "
        f"exceeding 400,000 hectares burnt. Portugal recorded the single "
        f"highest spike in the dataset. Greece shows an isolated but extreme "
        f"spike around 2007. France stays consistently lower than the other "
        f"three countries throughout the entire period."
    )

    # --- Section 2: Average fire size per country (ha per fire) ---
    st.write("### Average Fire Size by Country")

    st.write(
        f"Burnt area alone doesn't tell the whole story — a country could "
        f"have many small fires or few very large ones. Dividing burnt area "
        f"by number of fires gives the average size of a single fire."
    )

    # Average burnt area and number of fires per year, per country
    avg_fires_focus = df_focus.groupby('country_name')[['burnt_area_ha', 'number_of_fires']].mean().reset_index()

    # ha_per_fire = average hectares burnt per single fire
    avg_fires_focus['ha_per_fire'] = avg_fires_focus['burnt_area_ha'] / avg_fires_focus['number_of_fires']
    avg_fires_focus = avg_fires_focus.sort_values('ha_per_fire', ascending=False)

    fig = px.bar(avg_fires_focus, x='country_name', y='ha_per_fire',
                 title='Average Fire Size by Country (Hectares per Fire)',
                 labels={'ha_per_fire': 'Average Hectares per Fire', 'country_name': 'Country'},
                 text_auto='.1f')
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.success(
        f"**Key takeaway:** Greece's average fire burns roughly 32 hectares — "
        f"three times larger than Spain's and over five times larger than "
        f"Portugal's or France's. Greece's wildfire problem is driven by fewer "
        f"but far more destructive fires, while Portugal and France experience "
        f"many more frequent but smaller fires."
    )

    # --- Section 3: Europe-wide comparison ---
    st.write("### Europe-Wide Comparison")

    st.write(
        f"How do the four focus countries rank against the rest of Europe? "
        f"Here are the top 15 countries by average annual burnt area."
    )

    # Average burnt area per year, across all countries in the dataset
    avg_by_country = df.groupby('country_name')['burnt_area_ha'].mean().sort_values(ascending=False).reset_index()
    top15 = avg_by_country.head(15)

    fig = px.bar(top15, x='burnt_area_ha', y='country_name', orientation='h',
                 title='Average Annual Burnt Area by Country (Top 15, 1980-2024)',
                 labels={'burnt_area_ha': 'Average Burnt Area (hectares/year)', 'country_name': 'Country'})
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.write(
        f"Spain tops the list — even ahead of Portugal and Italy, which are "
        f"often associated more strongly with wildfire risk in public "
        f"perception. France ranks only 6th overall, with a relatively low "
        f"historical average compared to the other three focus countries."
    )

    # --- Validation, stated AFTER the evidence above ---
    st.write("### Validation")
    st.success(
        f"This hypothesis is confirmed by the data: Greece has the fewest "
        f"fires per year (1,371) but the largest average size (32 ha/fire), "
        f"while Portugal has the most fires (18,214/year) but the smallest "
        f"average size (6.25 ha/fire). Spain and France fall between these "
        f"two patterns."
    )
