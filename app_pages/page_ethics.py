import streamlit as st


def ethics_body():

    st.write("## Ethics & Data Governance")

    st.info(
        "This page reflects on the ethical considerations and "
        "limitations of the data used in this project."
    )

    # --- Data source & privacy ---
    st.write("### Data Source & Privacy")
    st.write(
        "The data comes from EFFIS (European Forest Fire Information "
        "System), a public dataset published by Copernicus. It only "
        "contains country-level totals — burnt area and number of "
        "fires per year. There is no personal or identifiable "
        "information in this dataset, so there are no privacy "
        "concerns."
    )

    # --- Known limitations of the dataset ---
    st.write("### Known Limitations")
    st.write(
        "The dataset does not record the *cause* of each fire (e.g. "
        "arson, agricultural burning, lightning, or accidental "
        "ignition). This means the analysis can describe patterns in "
        "wildfire frequency and severity, but it cannot explain why "
        "fires started, or how much of the trend is due to climate "
        "change versus other factors such as land management or "
        "population changes."
    )
    st.write(
        "Countries also joined EFFIS reporting at different points "
        "in time, so some countries have missing data in the earlier "
        "years. This was accounted for during data cleaning, but "
        "readers should still be cautious when comparing very early "
        "years across countries."
    )

    st.write(
        "Fire cause matters ethically. In Spain, official data shows "
        "55% of fires between 1983-2021 were started intentionally "
        "(Civio, based on Spanish government data) — a figure "
        "available because the fire season is long over and the "
        "data has been compiled and published."
    )
    st.write(
        "In France, President Macron has publicly stated that "
        "around 9 out of 10 wildfires during the still-ongoing 2026 "
        "season were human-caused. Unlike Spain's figure, this is a "
        "political statement made during an active crisis, not a "
        "verified, published statistic — official cause data for an "
        "ongoing fire season is simply not yet available. It is "
        "included here only to show that fire cause is being taken "
        "seriously as an issue, not as a data point comparable to "
        "Spain's figure."
    )
    st.write(
        "This dataset itself does not distinguish fire cause at "
        "all, which further limits how findings should be "
        "interpreted."
    )

    # --- Responsible use of the dashboard ---
    st.write("### Responsible Use")
    st.write(
        "Country comparisons (e.g. Spain vs. France) should not be "
        "used to assign blame or make policy claims about a "
        "country's land management. Wildfire risk depends on many "
        "factors — climate, terrain, vegetation, and firefighting "
        "resources — that this dataset does not capture."
    )

    st.write("### Responsible Use of Current Events Context")
    st.write(
        "This project explicitly separates its historical dataset "
        "(EFFIS, 1980-2024) from real-time news context about the "
        "2025-2026 wildfire crisis. Blending these without clear "
        "attribution and date-stamping would risk misleading "
        "readers into thinking recent, still-unfolding events are "
        "reflected in the statistical analysis. Each source and its "
        "time period is stated explicitly wherever current events "
        "are referenced."
    )

    st.success(
        "**Key takeaway:** This dashboard is intended for "
        "educational and exploratory purposes, not as a definitive "
        "scientific or policy tool."
    )

    st.write("### AI Usage Disclosure")
    st.write(
        "Claude (Anthropic) was used to assist with project "
        "structure, code scaffolding, README drafting, and "
        "debugging support during development."
    )
    st.write(
        "**Important distinction:** The ethical reasoning in this "
        "section — including the observation that wildfires could "
        "be human-caused (including arson), and the decision to "
        "keep this historical analysis separate from real-time "
        "news — originated from the author's own critical thinking, "
        "not from AI suggestion. The 2025-2026 wildfire crisis is "
        "used elsewhere in this project (e.g. as motivation in the "
        "README) to explain why this topic matters today, but it is "
        "not blended into the analysis above, since doing so would "
        "risk implying the dataset covers events it does not. "
        "Claude was used only to fact-check specific statistics "
        "(e.g. arson rates, current event figures) once the author "
        "had already identified these as relevant ethical concerns."
    )
    st.write(
        "The choice of dataset, business requirements, project "
        "hypothesis, and all interpretation of results are the "
        "author's own. AI-suggested data sources were fact-checked "
        "against their original documentation before use, and "
        "AI-drafted text was reviewed and adjusted to reflect the "
        "author's own analysis and voice."
    )
