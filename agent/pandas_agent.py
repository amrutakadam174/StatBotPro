import pandas as pd
import re

def extract_column_name(query, columns):
    query = query.lower()

    # 1. Check for column inside quotes ('Revenue' or "Revenue")
    match = re.search(r"'(.*?)'|\"(.*?)\"", query)
    if match:
        col = match.group(1) if match.group(1) else match.group(2)
        for c in columns:
            if c.lower() == col.lower():
                return c

    # 2. Match column names directly in query
    for col in columns:
        if col.lower() in query:
            return col

    return None


def analyze_data(df, query):

    query = query.lower()

    # 1. Row count
    if "how many rows" in query or "number of rows" in query:
        return f"Total rows: {df.shape[0]}"

    # 2. Column count
    if "how many columns" in query:
        return f"Total columns: {df.shape[1]}"

    # Extract column name
    column = extract_column_name(query, df.columns)

    # 3. Mean / Average
    if "mean" in query or "average" in query:
        if column:
            return f"Mean of {column}: {df[column].mean()}"
        else:
            return "Please specify a valid column name."

    # 4. Maximum
    if "max" in query or "maximum" in query or "highest" in query:
        if column:
            return f"Max of {column}: {df[column].max()}"
        else:
            return "Please specify a valid column name."

    # 5. Minimum
    if "min" in query or "minimum" in query or "lowest" in query:
        if column:
            return f"Min of {column}: {df[column].min()}"
        else:
            return "Please specify a valid column name."

    return "Sorry, I can answer questions about rows, columns, mean, max, and min."