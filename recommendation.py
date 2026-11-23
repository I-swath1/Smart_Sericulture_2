import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

RANKING_PATH = (
    BASE_DIR / "data" / "mulberry_variety_recommendation_ranking.csv"
)

def recommend_mulberry():
    if not RANKING_PATH.exists():
        raise FileNotFoundError(
            f"Recommendation dataset not found: {RANKING_PATH}"
        )

    ranking = pd.read_csv(RANKING_PATH)

    best = ranking.sort_values(
        "Overall_Score",
        ascending=False
    ).iloc[0]

    return {
        "recommended_variety": best["Mulberry_Variety"],
        "overall_score": round(float(best["Overall_Score"]), 2),
        "biochemical_score": round(float(best["Biochemical_Score"]), 2),
        "cocoon_performance_score": round(
            float(best["Cocoon_Performance_Score"]), 2
        )
    }
