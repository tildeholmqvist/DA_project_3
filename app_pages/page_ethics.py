import streamlit as st


def ethics_body():

    st.write("## Ethics & Data Governance")

    st.info(
        f"This page reflects on the ethical considerations and limitations "
        f"of the data used in this project."
    )

    # --- Data source & privacy ---
    st.write("### Data Source & Privacy")
    st.write(
        f"The data comes from EFFIS (European Forest Fire Information "
        f"System), a public dataset published by Copernicus. It only "
        f"contains country-level totals — burnt area and number of fires "
        f"per year. There is no personal or identifiable information in "
        f"this dataset, so there are no privacy concerns."
    )

    # --- Known limitations of the dataset ---
    st.write("### Known Limitations")
    st.write(
        f"The dataset does not record the *cause* of each fire (e.g. "
        f"arson, agricultural burning, lightning, or accidental ignition). "
        f"This means the analysis can describe patterns in wildfire "
        f"frequency and severity, but it cannot explain why fires started, "
        f"or how much of the trend is due to climate change versus other "
        f"factors such as land management or population changes."
    )
    st.write(
        f"Countries also joined EFFIS reporting at different points in "
        f"time, so some countries have missing data in the earlier years. "
        f"This was accounted for during data cleaning, but readers should "
        f"still be cautious when comparing very early years across "
        f"countries."
    )

    st.write(
    f"Fire cause matters ethically. In Spain, official data shows 55% of "
    f"fires between 1983-2021 were started intentionally (Civio, based on "
    f"government data). In France's 2026 wildfire season, authorities "
    f"confirmed 9 out of 10 fires were human-caused (deliberate or "
    f"accidental), with 111 arrests made (French Interior Ministry, via "
    f"Euronews, July 2026). This dataset does not distinguish cause, which "
    f"limits how findings should be interpreted."
    )

    # --- Responsible use of the dashboard ---
    st.write("### Responsible Use")
    st.write(
        f"Country comparisons (e.g. Spain vs. France) should not be used "
        f"to assign blame or make policy claims about a country's land "
        f"management. Wildfire risk depends on many factors — climate, "
        f"terrain, vegetation, and firefighting resources — that this "
        f"dataset does not capture."
    )

    st.write("### Responsible Use of Current Events Context")
    st.write(
        f"This project explicitly separates its historical dataset (EFFIS, "
        f"1980-2024) from real-time news context about the 2025-2026 wildfire "
        f"crisis. Blending these without clear attribution and date-stamping "
        f"would risk misleading readers into thinking recent, still-unfolding "
        f"events are reflected in the statistical analysis. Each source and "
        f"its time period is stated explicitly wherever current events are "
        f"referenced."
    )

    st.success(
        f"**Key takeaway:** This dashboard is intended for educational and "
        f"exploratory purposes, not as a definitive scientific or policy "
        f"tool."
    )

    st.write("### AI Usage Disclosure")
    st.write(
        f"Claude (Anthropic) was used to assist with project structure, code "
        f"scaffolding, README drafting, and debugging support during "
        f"development."
    )
    st.write(
        f"**Important distinction:** The ethical reasoning in this section — "
        f"including the observation that wildfires could be human-caused "
        f"(including arson), and the decision to keep this historical "
        f"analysis separate from real-time news — originated from the "
        f"author's own critical thinking, not from AI suggestion. The "
        f"2025-2026 wildfire crisis is used elsewhere in this project (e.g. "
        f"as motivation in the README) to explain why this topic matters "
        f"today, but it is not blended into the analysis above, since doing "
        f"so would risk implying the dataset covers events it does not. "
        f"Claude was used only to fact-check specific statistics (e.g. arson "
        f"rates, current event figures) once the author had already "
        f"identified these as relevant ethical concerns."
    )
    st.write(
        f"The choice of dataset, business requirements, project hypothesis, "
        f"and all interpretation of results are the author's own. AI-suggested "
        f"data sources were fact-checked against their original documentation "
        f"before use, and AI-drafted text was reviewed and adjusted to reflect "
        f"the author's own analysis and voice."
    )