import pandas as pd
import pyspark.sql.functions as F


def create_sample_dataset():
    df = pd.DataFrame({"number":list(range(1000))})
    return df

