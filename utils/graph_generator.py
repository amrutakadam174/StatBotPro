import matplotlib.pyplot as plt
import os
import time

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_graph(df, column):
    plt.figure(figsize=(8, 4))

    data = df[column].dropna()

    # ✅ Numeric → Line graph
    if data.dtype != 'object':
        plt.plot(data)
        plt.title(f"{column} Trend")
        plt.xlabel("Index")
        plt.ylabel(column)

    # ✅ Categorical → Bar graph
    else:
        counts = data.value_counts().head(10)
        counts.plot(kind='bar')
        plt.title(f"{column} Distribution")
        plt.xlabel(column)
        plt.ylabel("Count")

    plt.grid(True)

    path = os.path.join(OUTPUT_DIR, f"{column}_{int(time.time())}.png")

    plt.tight_layout()
    plt.savefig(path)
    plt.close()

    return path