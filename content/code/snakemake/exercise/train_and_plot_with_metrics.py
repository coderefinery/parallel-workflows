from pathlib import Path
import pickle
import argparse
import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ## Fit pipelines and plot decision boundaries
#
# Loop over the `n_neighbors` parameter
#
# - Fit a standard scaler + knn classifier pipeline
# - Plot decision boundaries and save the image to disk

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--n_neighbors",
    type=int,
    help="The number of neighbors to use for calculation.",
)
parser.add_argument(
    "--metric",
    type=str,
    help="The metric to use",
)
args = parser.parse_args()
n_neighbors = args.n_neighbors
metric = args.metric

# Load preprocessed data from disk
with open("data/preprocessed/Iris.pkl", "rb") as f:
    data = pickle.loads(f)
    X, X_train, X_test, y, y_train, y_test, features, classes = data


# Parameters
# Metrics: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics

# Loop over n_neighbors
# Fit
clf = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric)),
    ]
)
clf.fit(X_train, y_train)

# Plot
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X_test,
    response_method="predict",
    plot_method="pcolormesh",
    xlabel=features[0],
    ylabel=features[1],
    shading="auto",
    alpha=0.5,
)
scatter = disp.ax_.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, edgecolors="k")
disp.ax_.legend(
    scatter.legend_elements()[0],
    classes,
    loc="lower left",
    title="Classes",
)
_ = disp.ax_.set_title(
    f"3-Class classification\n(k={n_neighbors!r}, metric={metric!r})"
)
plt.show()

# Save image to disk
Path("results/").mkdir(parents=True, exist_ok=True)
plt.savefig(f"results/n_neighbors={n_neighbors}___metric={metric}.png")