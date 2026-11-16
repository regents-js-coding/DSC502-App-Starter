import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Works locally and on Streamlit Community Cloud: the path is built from this file's location.
DATA_PATH = Path(__file__).parent / "data" / "fitframe_classes_extended.csv"


def get_api_key():
    """Local runs read .env; deployed runs read Streamlit's secrets manager."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        return None


st.set_page_config(page_title="FitFrame", layout="wide")
st.title("FitFrame")

df = pd.read_csv(DATA_PATH)
st.write(f"Loaded {len(df)} classes.")
st.dataframe(df.head())

if get_api_key() is None:
    st.warning("No API key found. Add one to .env locally, or to Secrets when deployed.")
