import pandas as pd

def get_average_table(df: pd.DataFrame):
    condition_col = "Mental Health Condition"

    df[condition_col] = df[condition_col].astype(str).str.strip()
    df[condition_col] = df[condition_col].replace(["nan", "NaN", ""], "None")
    df[condition_col] = df[condition_col].fillna("None")

    variables = {
        "Sleep Hours": "Sleep Hours",
        "Exercise Level": "Exercise Level",
        "Stress Level": "Stress Level",
        "Work Hours per Week": "Work Hours per Week",
        "Screen Time": "Screen Time per Day (Hours)",
        "Social Interaction Score": "Social Interaction Score"
    }

    result = pd.DataFrame(index=variables.keys(), columns=df[condition_col].unique())

    for var_label, var_col in variables.items():
        for condition in df[condition_col].unique():
            subset = df[df[condition_col] == condition]

            if pd.api.types.is_numeric_dtype(df[var_col]):
                value = round(subset[var_col].mean(), 2)
            else:
                mode = subset[var_col].mode()
                value = mode.iloc[0] if len(mode) > 0 else None

            result.loc[var_label, condition] = value
    return result
