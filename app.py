import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_executive_summary import executive_summary_body
from app_pages.page_data_deep_dive import data_deep_dive_body
from app_pages.page_ethics import ethics_body
from app_pages.page_about import about_body

app = MultiPage(app_name="Wildfires & Climate Change: Southern Europe")

app.add_page("📌 Executive Summary", executive_summary_body)
app.add_page("🔬 Data & Trends Deep Dive", data_deep_dive_body)
app.add_page("⚖️ Ethics & Data Governance", ethics_body)
app.add_page("ℹ️ About", about_body)

app.run()