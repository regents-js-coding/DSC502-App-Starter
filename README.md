# DSC502 App Starter

Starter repository for the DSC502 week 10 to 12 project: a Streamlit app with an AI feature, deployed to Streamlit Community Cloud, with a portfolio site on GitHub Pages.

This is the repository you submit for assessment, so give it a clear commit history as you go.

## Set up

1. Click **Use this template**, then **Create a new repository**.
2. Set the visibility to **Public**. GitHub Pages on a free account needs a public repo, and your assessors need to see it. This is also why your API key must never be committed.
3. Open it in a Codespace (Code, Codespaces, Create codespace on main). Packages install automatically.
4. Copy `.env.example` to `.env` and paste your Claude API key. `.env` is already in `.gitignore`.
5. Run the app: `streamlit run app.py`

## What is in here

- `app.py`: a minimal starting point that loads the FitFrame data. Replace it with your own app.
- `data/fitframe_classes_extended.csv`: the week 10 dataset. Swap in your own data if your project has it.
- `requirements.txt`: what Streamlit Community Cloud installs when you deploy. Add anything new your app imports.
- `.env.example` and `.streamlit/secrets.toml.example`: templates showing the key name. The real files are ignored by Git.

## Deploying

On Streamlit Community Cloud, create a new app from this repo, set the main file path to `app.py`, and paste the contents of `.streamlit/secrets.toml.example` (with your real key) into **Advanced settings, Secrets**.
