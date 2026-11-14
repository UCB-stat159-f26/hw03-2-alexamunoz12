import matplotlib.pyplot as plt


def plot_player_career(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    colors = {"W": "blue", "L": "red"}

    for result in ["W", "L"]:
        matches = df[df["W/L"] == result]
        ax.scatter(
            matches["PLAYER_AGE"],
            matches["AGE_DIFF"],
            c=colors[result],
            label="Win" if result == "W" else "Loss",
            alpha=0.5,
            s=15
        )

    ax.axhline(0, color="gray", linestyle="--")
    ax.set_xlabel("Player Age")
    ax.set_ylabel("Age Difference (Player - Opponent)")
    ax.legend()

    return fig