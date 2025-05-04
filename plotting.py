import matplotlib.pyplot as plt

def plot_payment_breakdown(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.stackplot(df["Month"], df["Principal"], df["Interest"],
                 labels=["Principal", "Interest"], colors=["#4CAF50", "#FF9800"])
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (₪)")
    ax.legend(loc="upper right")
    ax.set_title("Principal vs. Interest Over Time")
    return fig
