import pandas as pd
import re
from difflib import get_close_matches
from utils.graph_generator import generate_graph


# 🔹 Normalize query (handle synonyms)
def normalize_query(query):
    query = query.lower()

    synonyms = {
        "average": "mean",
        "avg": "mean",
        "revenue": "sales",
        "price": "msrp",
        "total": "sum"
    }

    for word, replacement in synonyms.items():
        query = query.replace(word, replacement)

    return query


# 🔹 Smart column matching (fuzzy + flexible)
def smart_column_match(query, columns):
    query = query.lower()

    # ✅ Direct match
    for col in columns:
        if col.lower() in query:
            return col

    # ✅ Fuzzy full query match
    matches = get_close_matches(query, columns, n=1, cutoff=0.5)
    if matches:
        return matches[0]

    # ✅ Word-by-word match
    for word in query.split():
        matches = get_close_matches(word, columns, n=1, cutoff=0.6)
        if matches:
            return matches[0]

    return None


# 🔹 Main function
def analyze_data(df, query):

    # 🔥 Normalize query
    query = normalize_query(query)

    # ------------------ BASIC ------------------

    if "row" in query:
        return f"Total rows: {df.shape[0]}"

    if "column" in query:
        return f"Total columns: {df.shape[1]}"

    # 🔹 Smart column detection
    column = smart_column_match(query, df.columns)

    # ------------------ STATISTICS ------------------

    if "mean" in query:
        if column:
            return f"Mean of {column}: {df[column].mean()}"
        return f"❌ Column not found. Try: {', '.join(df.columns[:5])}"

    if "max" in query:
        if column:
            return f"Max of {column}: {df[column].max()}"
        return f"❌ Column not found. Try: {', '.join(df.columns[:5])}"

    if "min" in query:
        if column:
            return f"Min of {column}: {df[column].min()}"
        return f"❌ Column not found. Try: {', '.join(df.columns[:5])}"

    if "sum" in query:
        if column:
            return f"Sum of {column}: {df[column].sum()}"
        return f"❌ Column not found. Try: {', '.join(df.columns[:5])}"

    # ------------------ GRAPH ------------------

    if any(word in query for word in ["plot", "graph", "chart", "show"]):
        if column:
            path = generate_graph(df, column)
            return {"type": "graph", "path": path}

        return f"❌ Column not found. Try: {', '.join(df.columns[:5])}"

    # ------------------ DEFAULT ------------------

    return "❌ Query not supported. Try: mean sales, plot country, max quantity"