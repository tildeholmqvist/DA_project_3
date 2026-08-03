# Wildfires and Climate Change: Trends in Southern Europe (1980–2024)

*Ethical practice and communication in data — Capstone Project*

## Table of Contents
1. [Introduction & Motivation](#introduction--motivation)
2. [Dataset Content](#dataset-content)
3. [Business Requirements](#business-requirements)
4. [Project Hypothesis and Validation](#project-hypothesis-and-validation)
5. [Audience](#audience)
6. [Ethics, Privacy and Data Governance](#ethics-privacy-and-data-governance)
7. [Dashboard Design](#dashboard-design)
8. [Project Plan](#project-plan)
9. [Reflection on Challenges](#reflection-on-challenges)
10. [Technologies Used](#technologies-used)
11. [Credits and Acknowledgements](#credits-and-acknowledgements)

---

## Introduction & Motivation

In July 2026, wildfires forced over 300,000 evacuations across Spain and
France; Spain declared its first-ever national wildfire emergency. As of
July 2026, France had recorded 3.4 times its annual average number of fires,
and Spain 1.7 times its average (Copernicus data, via CNN, 27 July 2026).

This project uses 45 years of official EU wildfire statistics (1980-2024) to
explore whether the current crisis reflects a longer-term pattern, or whether
it marks a departure from historical norms — with a particular focus on
Spain, Portugal, France, and Greece.

*Note: this dataset covers 1980-2024. The 2025-2026 crisis referenced above
is not part of the statistical analysis, but provides real-world context for
why this topic is relevant today. See the Ethics section for more on how
these are kept separate.*

---

## Dataset Content

- **Source:** European Forest Fire Information System (EFFIS), Copernicus
  Emergency Management Service (European Commission Joint Research Centre)
- **Original download:** https://forest-fire.emergency.copernicus.eu/applications/data-and-services
  ("Country totals" report)
- **License:** EFFIS data reuse terms — source must be acknowledged
- **Coverage:** 31 countries across Europe, MENA; 1980-2024 (individual
  countries joined EFFIS reporting at different times — see Data Cleaning
  notebook for details)
- **Public data, no personal or sensitive information** — this is
  country-level aggregate government statistical data, not individual
  records, so no anonymisation was required

### Raw Data Structure

The raw data was provided as two separate files, each in **wide format**
(one column per country, one row per year):
- `burnt_area_ha_1980_2024.csv` — burnt area in hectares
- `number_of_fires_1980_2024.csv` — number of recorded forest fires

### Processed Data

These two files were cleaned and combined into a single, tidy **long-format**
dataset (`inputs/processed/wildfires_long_format.csv`, 922 rows), with one
row per country-year combination. This was necessary for two reasons:
1. **Reshaping (wide → long)** made it possible to filter and group by
   country using simple pandas code, rather than referencing 31 separate
   columns
2. **Merging** the two files into one table made it possible to calculate
   new metrics — such as average hectares burnt per fire — by combining
   both indicators in the same row

Full methodology is documented in `jupyter_notebooks/01_data_cleaning.ipynb`.

---

## Business Requirements

- **BR1:** As a policymaker or member of the public, I want to see how burnt
  area and number of wildfires have evolved over time in Spain, Portugal,
  France, and Greece, so that I can judge whether recent fire seasons are
  part of a long-term trend or an anomaly.
- **BR2:** As a non-technical user, I want a simple comparison between
  countries, so that I can understand which countries are most affected
  without needing to interpret raw statistics myself.
- **BR3:** As an analyst, I want to understand whether wildfire severity
  differs in *character* (frequent small fires vs. rare large fires) between
  countries, not just in total scale.

---

## Project Hypothesis and Validation

**H1:** Among Spain, Portugal, France, and Greece, wildfire severity patterns
are not uniform — some of these countries experience frequent, smaller fires,
while others experience rarer but more severe fires, despite sharing a
similar Mediterranean climate.

**Validation:** This hypothesis is confirmed by the data: Greece has the
fewest fires per year (1,371) but the largest average size (32 ha/fire),
while Portugal has the most fires (18,214/year) but the smallest average
size (6.25 ha/fire). Spain and France fall between these two patterns.

Full analysis, charts, and supporting evidence are documented in
`jupyter_notebooks/02_eda.ipynb` and reproduced in the Streamlit dashboard's
Data & Trends Deep Dive page.

---

## Audience

- **Non-technical audience** (general public, policymakers without a data
  background): interested in "what does this mean for my region/country" —
  served via the Executive Summary dashboard page, with plain-language
  takeaways and simple, clearly-labelled charts. This project is written for
  a reader with zero prior knowledge of climate science or data analysis.
- **Technical audience** (mentors, fellow students, data-literate
  stakeholders): interested in data source, cleaning methodology, and
  statistical detail — served via the Jupyter notebooks and the Data &
  Trends Deep Dive dashboard page.

---

## Ethics, Privacy and Data Governance

### Data Source & Privacy

The data comes from EFFIS (European Forest Fire Information System), a
public dataset published by Copernicus. It only contains country-level
totals — burnt area and number of fires per year. There is no personal or
identifiable information in this dataset, so there are no privacy concerns.

### Known Limitations

The dataset does not record the *cause* of each fire (e.g. arson,
agricultural burning, lightning, or accidental ignition). This means the
analysis can describe patterns in wildfire frequency and severity, but it
cannot explain why fires started, or how much of the trend is due to
climate change versus other factors such as land management or population
changes.

Countries also joined EFFIS reporting at different points in time, so some
countries have missing data in the earlier years. This was accounted for
during data cleaning, but readers should still be cautious when comparing
very early years across countries.

Fire cause matters ethically. In Spain, official data shows 55% of fires
between 1983-2021 were started intentionally
([Civio, based on Spanish government data](https://civio.es/en/environment/forest-fires-map/))
— a figure available because the fire season is long over and the data has
been compiled and published.

In France, President Macron has publicly stated that around 9 out of 10
wildfires during the still-ongoing 2026 season were human-caused. Unlike
Spain's figure, this is a political statement made during an active crisis,
not a verified, published statistic — official cause data for an ongoing
fire season is simply not yet available. It is included here only to show
that fire cause is being taken seriously as an issue, not as a data point
comparable to Spain's figure.

This dataset itself does not distinguish fire cause at all, which further
limits how findings should be interpreted.

### Responsible Use

Country comparisons (e.g. Spain vs. France) should not be used to assign
blame or make policy claims about a country's land management. Wildfire
risk depends on many factors — climate, terrain, vegetation, and
firefighting resources — that this dataset does not capture.

### Responsible Use of Current Events Context

This project explicitly separates its historical dataset (EFFIS, 1980-2024)
from real-time news context about the 2025-2026 wildfire crisis. Blending
these without clear attribution and date-stamping would risk misleading
readers into thinking recent, still-unfolding events are reflected in the
statistical analysis. Each source and its time period is stated explicitly
wherever current events are referenced.

**Key takeaway:** This dashboard is intended for educational and exploratory
purposes, not as a definitive scientific or policy tool.

### AI Usage Disclosure

Claude (Anthropic) was used to assist with project structure, code
scaffolding, README drafting, and debugging support during development.

**Important distinction:** The ethical reasoning in this section — including
the observation that wildfires could be human-caused (including arson), and
the decision to keep this historical analysis separate from real-time news
— originated from the author's own critical thinking, not from AI
suggestion. The 2025-2026 wildfire crisis is used elsewhere in this project
(e.g. as motivation above) to explain why this topic matters today, but it
is not blended into the analysis, since doing so would risk implying the
dataset covers events it does not. Claude was used only to fact-check
specific statistics (e.g. arson rates, current event figures) once the
author had already identified these as relevant ethical concerns.

The choice of dataset, business requirements, project hypothesis, and all
interpretation of results are the author's own. AI-suggested data sources
were fact-checked against their original documentation before use, and
AI-drafted text was reviewed and adjusted to reflect the author's own
analysis and voice.

---

## Dashboard Design

## Project Plan

## Reflection on Challenges

## Technologies Used

## Credits and Acknowledgements

### VIKTIGT ATT TA MED!!!

ANG PLOTEN DÄR VI JÄMFÖR ALLA LÄNDER I 02_EDA i stapeldiagrammet

*Note: This dataset covers 1980-2024. As of writing (July 2026), France and Spain
are experiencing a severe ongoing wildfire season — France has recorded 3.4 times
its typical annual number of fires (Copernicus data, via CNN, 27 July 2026). This
recent crisis is not reflected in the analysis above but provides real-world context
for why this topic remains highly relevant.*
