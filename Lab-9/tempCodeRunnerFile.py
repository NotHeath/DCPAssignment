import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tuneindex.csv")

print(len(df))
df.info # Columns & values

# Q2. Reel is there twice, once as a upper-case onces with all lowercase
df["tune_type"] = df["tune_type"].str.strip().str.lower()

counts = df["tune_type"].value_counts().head(10)
print(counts) # Q3. 7726 reels now

"""
plt.bar(counts.index, counts.values)
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 most common tune types")
plt.xlabel("Tune Types")
plt.ylabel("Popularity")
plt.tight_layout() # stops the labels getting cut off

# Histogram for downloads
plt.hist(df["downloaded"], bins=50, edgecolor="black")
plt.title("Distribution of downloaded tune types")
plt.xlabel("Number of downloads") # Q5. Roughly 9500
plt.ylabel("Number of tunes") # Q4. Only a few
plt.tight_layout()
plt.subplot(1,2)
"""

top10 = counts.index

avg_downloads = (
    df[df["tune_type"].isin(top10)]
    .groupby("tune_type")["downloaded"].mean()
    .sort_values(ascending=False)
)

fig, (ax1, ax2) = plt.subplot(1, 2, figsize=(12,6))

# Left table: How common each tune is
ax1.bar(top10, counts.values)
ax1.set_title("Number of tunes per type")
ax1.set_xlabel("Tune type")
ax1.set_ylabel("Number of tunes")
ax1.tick_params(axis="x", rotation=45)

# Right table: average downloads
ax2.bar(avg_downloads.index, avg_downloads.values)
ax2.set_title("Average downloads per type")
ax2.set_xlabel("Tune type")
ax2.set_ylabel("Average downloads")
ax2.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()