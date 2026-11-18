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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

# Left table: How common each tune is
ax1.bar(top10, counts.values)
ax1.set_title("Number of tunes per type")
ax1.set_xlabel("Tune type")
ax1.set_ylabel("Number of tunes")
ax1.tick_params(axis="x", rotation=45)

# Right table: average downloads
ax2.bar(avg_downloads.index, avg_downloads.values, color="orange")
ax2.set_title("Average downloads per type")
ax2.set_xlabel("Tune type")
ax2.set_ylabel("Average downloads") # Q7. Reel is most downloads, Least is Strathspey
ax2.tick_params(axis="x", rotation=45) 
# Q8. Slide - tells you despite the low amount of slide tunes it's still one of the most downloaded

plt.tight_layout()
plt.savefig("top10.png")
plt.show()


# Time signatures
tune_types = ["reel", "jig", "polka", "waltz"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, tune in zip(axes.flat, tune_types):
    subset = df[df["tune_type"] == tune]
    times = subset["time_sig"].value_counts().head(3)
    ax.bar(times.index, times.values)
    ax.set_title(tune.title() + "s")
    ax.set_xlabel("Time signature") # Q9. Jigs=6/8, Polkas=2/4, Waltzes=3/4
    ax.set_ylabel("Number of tunes") 

plt.tight_layout()
plt.savefig("timesigs.png")
plt.show()


# Old/New Tunes
session = df[df["source"] == 1]
session_reels = session[session["tune_type"] == "reel"]
session_jigs = session[session["tune_type"] == "jig"]

plt.figure(figsize=(10,5))
plt.scatter(session_reels["x"], session_reels["downloaded"], s=5, alpha=0.3)
plt.scatter(session_jigs["x"], session_jigs["downloaded"], s=5, alpha=0.3)
plt.xlabel("x") 
plt.ylabel("Number of downloads")
plt.legend()
plt.tight_layout()

plt.savefig("oldnewtunes.png")

plt.show()
