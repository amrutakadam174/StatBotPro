import pandas as pd

def analyze_data(df, query):
    
    query = query.lower()

    # Mean
    if "mean" in query or "average" in query:
        result = df.mean(numeric_only=True)
        return result

    # Maximum
    elif "max" in query or "highest" in query:
        result = df.max(numeric_only=True)
        return result

    # Minimum
    elif "min" in query or "lowest" in query:
        result = df.min(numeric_only=True)
        return result

    else:
        return "Sorry, I can only find mean, max, or min for now."