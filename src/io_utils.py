from pathlib import Path
import pandas as pd


def load_health_data():
    project_dir = Path(__file__).resolve().parent.parent
    data_path = project_dir / "data" / "health_study_dataset.csv"

    return pd.read_csv(data_path)