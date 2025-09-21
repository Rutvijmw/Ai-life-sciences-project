from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def load_csv(rel_path: str) -> pd.DataFrame:
    path = DATA_DIR / rel_path
    return pd.read_csv(path)

def save_csv(df: pd.DataFrame, rel_path: str) -> None:
    path = DATA_DIR / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
