# League of Legends data study: what wins games, 2020 against 2024

An assessed data project from my 2024 technical training. **Question:** which in-game factors correlate most with winning, and did that change between 2020 and 2024?

Full write-up: [dhk-developer.github.io/riot-analysis.html](https://dhk-developer.github.io/riot-analysis.html) · the method and results are in [`Assessment.ipynb`](Assessment.ipynb).

## Method

| Step | 2020 | 2024 |
|---|---|---|
| Source | Public dataset: ≈9,900 high-rank games, **first 10 minutes** (`high_diamond_ranked_10min.csv`) | Riot Games API: top-ladder players → match IDs → match detail |
| Constraint | n/a | Free developer key: **100 requests per 2 minutes**, so requests were throttled and each stage cached to JSON (`*_cache.json`) |
| Transform | Drop redundant and collinear columns after a correlation check | Rebuild blue-side team features from participant-level JSON to match the 2020 schema; add newer objectives |
| Load | MySQL via SQLAlchemy (`tables/gamestats_2020.csv` export) | MySQL via SQLAlchemy (`tables/gamestats_2024.csv` export) |
| Analyse | Correlation with winning; averages | Same |

3,000 requested games produced **1,847 unique matches**, because top-ladder players keep meeting each other.

## Findings

- Dragons and turrets correlate much more strongly with winning in 2024, consistent with patch changes (permanent dragon buffs, turret bounties).
- First blood matters less, consistent with comeback mechanics.
- Vision stays weakly correlated in both years.

## Limitations

- **Not like-for-like:** the 2020 data covers the first ten minutes only, while the API returns whole games. Correlations are informative, but magnitudes are not comparable.
- **Repository scope:** this repository contains the notebook, cached data, exported tables and the account and match-ID request modules (`routes/`). Some supporting code described in the notebook (the league lookup and the throttling and cache helpers) is not in this commit, so the notebook is the record of the method.

## Running

```bash
pip install pandas matplotlib seaborn sqlalchemy mysql-connector-python requests python-dotenv
```

Create a `.env` with `API_KEY` (a Riot developer key) and `DEFAULT_REGION`. The notebook reads the cached JSON by default, so it runs without calling the API. The database URL in the notebook points to a local MySQL instance; change it to your own.
