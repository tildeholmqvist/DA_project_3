import streamlit as st


def ethics_body():

    st.write("## Ethics & Data Governance")

    st.info(
        f"This page reflects on the ethical considerations and "
        f"limitations of the data used in this project."
    )

    # --- Data source & privacy ---
    st.write("### Data Source & Privacy")
    st.write(
        f"The data comes from EFFIS (European Forest Fire Information "
        f"System), a public dataset published by Copernicus. It only "
        f"contains country-level totals — burnt area and number of "
        f"fires per year. There is no personal or identifiable "
        f"information in this dataset, so there are no privacy "
        f"concerns."
    )

    # --- Known limitations of the dataset ---
    st.write("### Known Limitations")
    st.write(
        f"The dataset does not record the *cause* of each fire (e.g. "
        f"arson, agricultural burning, lightning, or accidental "
        f"ignition). This means the analysis can describe patterns in "
        f"wildfire frequency and severity, but it cannot explain why "
        f"fires started, or how much of the trend is due to climate "
        f"change versus other factors such as land management or "
        f"population changes."
    )
    st.write(
        f"Countries also joined EFFIS reporting at different points "
        f"in time, so some countries have missing data in the earlier "
        f"years. This was accounted for during data cleaning, but "
        f"readers should still be cautious when comparing very early "
        f"years across countries."
    )

    st.write(
        f"Fire cause matters ethically. In Spain, official data shows "
        f"55% of fires between 1983-2021 were started intentionally "
        f"(Civio, based on Spanish government data) — a figure "
        f"available because the fire season is long over and the "
        f"data has been compiled and published."
    )
    st.write(
        f"In France, President Macron has publicly stated that "
        f"around 9 out of 10 wildfires during the still-ongoing 2026 "
        f"season were human-caused. Unlike Spain's figure, this is a "
        f"political statement made during an active crisis, not a "
        f"verified, published statistic — official cause data for an "
        f"ongoing fire season is simply not yet available. It is "
        f"included here only to show that fire cause is being taken "
        f"seriously as an issue, not as a data point comparable to "
        f"Spain's figure."
    )
    st.write(
        f"This dataset itself does not distinguish fire cause at "
        f"all, which further limits how findings should be "
        f"interpreted."
    )

    # --- Responsible use of the dashboard ---
    st.write("### Responsible Use")
    st.write(
        f"Country comparisons (e.g. Spain vs. France) should not be "
        f"used to assign blame or make policy claims about a "
        f"country's land management. Wildfire risk depends on many "
        f"factors — climate, terrain, vegetation, and firefighting "
        f"resources — that this dataset does not capture."
    )

    st.write("### Responsible Use of Current Events Context")
    st.write(
        f"This project explicitly separates its historical dataset "
        f"(EFFIS, 1980-2024) from real-time news context about the "
        f"2025-2026 wildfire crisis. Blending these without clear "
        f"attribution and date-stamping would risk misleading "
        f"readers into thinking recent, still-unfolding events are "
        f"reflected in the statistical analysis. Each source and its "
        f"time period is stated explicitly wherever current events "
        f"are referenced."
    )

    st.success(
        f"**Key takeaway:** This dashboard is intended for "
        f"educational and exploratory purposes, not as a definitive "
        f"scientific or policy tool."
    )

    st.write("### AI Usage Disclosure")
    st.write(
        f"Claude (Anthropic) was used to assist with project "
        f"structure, code scaffolding, README drafting, and "
        f"debugging support during development."
    )
    st.write(
        f"**Important distinction:** The ethical reasoning in this "
        f"section — including the observation that wildfires could "
        f"be human-caused (including arson), and the decision to "
        f"keep this historical analysis separate from real-time "
        f"news — originated from the author's own critical thinking, "
        f"not from AI suggestion. The 2025-2026 wildfire crisis is "
        f"used elsewhere in this project (e.g. as motivation in the "
        f"README) to explain why this topic matters today, but it is "
        f"not blended into the analysis above, since doing so would "
        f"risk implying the dataset covers events it does not. "
        f"Claude was used only to fact-check specific statistics "
        f"(e.g. arson rates, current event figures) once the author "
        f"had already identified these as relevant ethical concerns."
    )
    st.write(
        f"The choice of dataset, business requirements, project "
        f"hypothesis, and all interpretation of results are the "
        f"author's own. AI-suggested data sources were fact-checked "
        f"against their original documentation before use, and "
        f"AI-drafted text was reviewed and adjusted to reflect the "
        f"author's own analysis and voice."
    )
