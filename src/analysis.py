import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pathlib import Path

# Set up paths
BASE_DIR = Path(__file__).parent.parent
DATA_FILE = BASE_DIR / "Data" / "ab_data.csv" / "ab_data.csv"

# Load dataset
df = pd.read_csv(DATA_FILE).copy()

print("Dataset preview:")
print(df.head())

# A/B TESTING ANALYSIS

control = df[df["group"] == "control"].copy()
treatment = df[df["group"] == "treatment"].copy()

control_rate = control["converted"].mean()
treatment_rate = treatment["converted"].mean()

print("\nControl Conversion Rate:", control_rate)
print("Treatment Conversion Rate:", treatment_rate)

# Statistical test
t_stat, p_value = ttest_ind(control["converted"], treatment["converted"])

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

# Uplift calculation
uplift = treatment_rate - control_rate

print("\nConversion Uplift:", uplift)

# VISUALIZATIONS

plt.figure(figsize=(10,6))
sns.barplot(x="group", y="converted", data=df)
plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.savefig(BASE_DIR / "results" / "conversion_rate_plot.png")

# MACHINE LEARNING MODEL

# Convert group to numeric
df.loc[:, "group_encoded"] = df["group"].map({"control":0, "treatment":1})

X = df[["group_encoded"]].copy()
y = df["converted"].copy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nLogistic Regression Model Accuracy:", accuracy)

# SAVE REPORT

with open(BASE_DIR / "results" / "analysis_report.txt", "w") as f:
    f.write("A/B Testing Conversion Analysis\n")
    f.write("-----------------------------\n")
    f.write(f"Control Conversion Rate: {control_rate}\n")
    f.write(f"Treatment Conversion Rate: {treatment_rate}\n")
    f.write(f"Conversion Uplift: {uplift}\n")
    f.write(f"P-value: {p_value}\n")
    f.write(f"Model Accuracy: {accuracy}\n")

print("\nReport saved to results/analysis_report.txt")
