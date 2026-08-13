import streamlit as st
import pandas as pd
import plotly.express as px


def data_deep_dive_body():

    st.write("## Data & Trends Deep Dive")

    st.info(
        "This page takes a closer look at wildfire patterns in Spain, "
        "Portugal, France, and Greece (1980-2024), and compares them to "
        "the rest of Europe."
    )

    # Load the processed dataset
    df = pd.read_csv("inputs/processed/wildfires_long_format.csv")

    # --- Section: Europe-wide comparison (comes first) ---
    st.write("### Europe-Wide Comparison")

    st.write(
        "Compare average annual burnt area across all 31 countries in "
        "the dataset, to identify which countries are most affected by "
        "wildfires in Europe."
    )

    avg_by_country = (
        df.groupby('country_name')['burnt_area_ha']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    top15 = avg_by_country.head(15)

    fig = px.bar(
        top15,
        x='burnt_area_ha',
        y='country_name',
        orientation='h',
        title='Average Annual Burnt Area by Country (Top 15, 1980-2024)',
        labels={
            'burnt_area_ha': 'Average Burnt Area (hectares/year)',
            'country_name': 'Country'
        }
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.write(
        "Spain tops the list — even ahead of Portugal and Italy, which "
        "are often associated more strongly with wildfire risk in "
        "public perception. France ranks only 6th overall, with a "
        "relatively low historical average (23k hectares/year) — a "
        "notable contrast to Spain's high ranking."
    )

    st.success(
        "This confirms why Spain, Portugal, France, and Greece are the "
        "focus of the deeper analysis that follows."
    )

    # --- Hypothesis, stated BEFORE the focus-country data is shown ---
    st.write("### Hypothesis")
    st.info(
        "**H1:** Among Spain, Portugal, France, and Greece, wildfire "
        "severity patterns are not uniform — some of these countries "
        "experience frequent, smaller fires, while others experience "
        "rarer but more severe fires, despite sharing a similar "
        "Mediterranean climate."
    )

    # Filter down to the four focus countries
    focus_countries = ['Spain', 'Portugal', 'France', 'Greece']
    df_focus = df[df['country_name'].isin(focus_countries)]

    # --- Section: Burnt area trends over time ---
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

    st.write(
        "Spain shows the largest year-to-year swings, with several "
        "years exceeding 400,000 hectares burnt. Portugal recorded the "
        "single highest spike in the dataset. Greece shows an isolated "
        "but extreme spike around 2007. France stays consistently "
        "lower than the other three countries throughout the entire "
        "period."
    )

    # --- Section: Average fire size per country (ha per fire) ---
    st.write("### Average Fire Size by Country")

    st.write(
        "Burnt area alone doesn't tell the whole story — a country "
        "could have many small fires or few very large ones. Dividing "
        "burnt area by number of fires gives the average size of a "
        "single fire."
    )

    avg_fires_focus = (
        df_focus.groupby('country_name')
        [['burnt_area_ha', 'number_of_fires']]
        .mean()
        .reset_index()
    )
    avg_fires_focus['ha_per_fire'] = (
        avg_fires_focus['burnt_area_ha']
        / avg_fires_focus['number_of_fires']
    )
    avg_fires_focus = avg_fires_focus.sort_values(
        'ha_per_fire', ascending=False
    )

    fig = px.bar(
        avg_fires_focus,
        x='country_name',
        y='ha_per_fire',
        title='Average Fire Size by Country (Hectares per Fire)',
        labels={
            'ha_per_fire': 'Average Hectares per Fire',
            'country_name': 'Country'
        },
        text_auto='.1f'
    )
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.success(
        "**Key takeaway:** Greece's average fire burns roughly 32 "
        "hectares — three times larger than Spain's and over five "
        "times larger than Portugal's or France's. Greece's wildfire "
        "problem is driven by fewer but far more destructive fires, "
        "while Portugal and France experience many more frequent but "
        "smaller fires."
    )

    # --- Section: Fire frequency vs fire size (scatter) ---
    st.write("### Fire Frequency vs Average Fire Size")

    fig = px.scatter(
        avg_fires_focus,
        x='number_of_fires',
        y='ha_per_fire',
        text='country_name',
        size='burnt_area_ha',
        title='Fire Frequency vs Average Fire Size',
        labels={
            'number_of_fires': 'Average Number of Fires per Year',
            'ha_per_fire': 'Average Hectares per Fire'
        }
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig)
    st.caption("Source: EFFIS / Copernicus, 1980-2024")

    st.write(
        "This chart plots each country by two measurements at once: "
        "how often fires happen (left to right) and how large each "
        "fire tends to be (bottom to top). A country in the "
        "bottom-right has many small fires; a country in the top-left "
        "has few large fires."
    )

    st.success(
        "This chart confirms the pattern directly: Portugal and "
        "France sit toward the bottom-right (frequent, smaller "
        "fires), while Greece sits clearly in the top-left "
        "(infrequent but very large fires). Spain falls in between — "
        "a moderate number of fires, but each noticeably larger than "
        "Portugal's or France's."
    )

    # --- Validation, stated AFTER all the evidence above ---
    st.write("### Validation")
    st.success(
        "This hypothesis is confirmed by the data: Greece has the "
        "fewest fires per year (1,371) but the largest average size "
        "(32 ha/fire), while Portugal has the most fires (18,214/"
        "year) but the smallest average size (6.3 ha/fire). Spain and "
        "France fall between these two patterns."
    )
