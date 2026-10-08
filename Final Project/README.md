# Final Project — Applied NLP on Persian Data

**Goal:** Apply the course to real, messy, mostly Persian text, on problems taken from industry.

1. **Gender detection (social media profiles):** engineered features (bio length, emoji count, etc.) plus a stacked approach. A TF-IDF + XGBoost model over name, username and bio produces a prediction that becomes a feature for a tuned XGBoost main classifier. **Test F1 ≈ 0.82** (accuracy 0.81); the required minimum was 0.75.
2. **Topic classification of Persian web pages:** Persian text cleaning and tokenization (Hazm), TF-IDF on title + content, and XGBoost with stratified splitting. **Weighted F1 ≈ 0.76.**
3. **Search-log analysis (travel booking):** service popularity, most searched cities and provinces, and population vs. search-demand analysis.
4. **City-name autocomplete / suggestion system:** a hybrid system that suggests the top 5 cities for a partial or misspelled query, evaluated with Rank-Biased Overlap (RBO).
   - *Rule-based stage:* exact match, then prefix, then substring, then edit distance 1 (Levenshtein), then fuzzy prefix.
   - *Probabilistic fallback:* learned from historical typed → accepted strings.
   - Handles normalizing Persian characters (e.g. آ → ا), English city names, and **wrong keyboard layout** (Persian typed on an English layout, e.g. `dcn` → یزد).

Notebook: [`Project.ipynb`](Project.ipynb)

*Datasets are in [`data/`](data/) (except `topic_modeling.csv`, which is not included).*
