import pandas as pd

def create_features(df):

    df = df.copy()

    df["balance_error_orig"] = (
        df["oldbalanceOrg"]
        - df["amount"]
        - df["newbalanceOrig"]
    )

    df["balance_error_dest"] = (
        df["oldbalanceDest"]
        + df["amount"]
        - df["newbalanceDest"]
    )

    df["amount_ratio"] = (
        df["amount"]
        / (df["oldbalanceOrg"] + 1)
    )

    return df