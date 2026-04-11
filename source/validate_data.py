import pandera.pandas as pa
from pandera import Column, Check
import pandas as pd
import logging

logger = logging.getLogger(__name__)

# Define schema
wine_schema = pa.DataFrameSchema(
    {
        "fixed_acidity": Column(float, Check.between(3, 20)),
        "volatile_acidity": Column(float, Check.between(0, 2)),
        "citric_acid": Column(float, Check.between(0, 1)),
        "residual_sugar": Column(
    float,
    [
        Check.ge(0),
        Check(lambda s: s.isna().mean() <= 0.05,
              error="Too many missing values in residual_sugar"),
    ],
    nullable=True
),
        "chlorides": Column(float, Check.ge(0)),
        "free_sulfur_dioxide": Column(float, Check.ge(0)),
        "total_sulfur_dioxide": Column(float, Check.ge(0)),
        "density": Column(float, Check.between(0.9, 1.1)),
        "ph": Column(float, Check.between(0, 14)),
        "sulphates": Column(float, Check.ge(0)),
        "alcohol": Column(float, Check.between(5, 20)),
        "quality": Column(int, Check.between(0, 10)),
        "wine_type": Column(str, Check.isin(["red", "white"]))
    },
    checks=[
        pa.Check(lambda df: ~df.duplicated().any(),
                 error="Duplicate rows found"),
        pa.Check(lambda df: ~(df.isna().all(axis=1)).any(),
                 error="Empty rows found"),
        pa.Check(
                lambda df: df["quality"].nunique() > 1,
                error="Quality column has no variation"
),
    ],
    drop_invalid_rows=False
)

# Validation function
def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and clean wine dataset using Pandera schema.
    Returns cleaned DataFrame with invalid rows removed.
    """
    try:
        validated_df = wine_schema.validate(df, lazy=True)
        return validated_df

    except pa.errors.SchemaErrors as e:
        logger.warning("Validation errors detected:\n%s", e.failure_cases)

        bad_rows = e.failure_cases["index"].dropna().unique()
        cleaned_df = df.drop(index=bad_rows)
        cleaned_df = cleaned_df.drop_duplicates()
        cleaned_df = cleaned_df.dropna(how="all")

        return cleaned_df