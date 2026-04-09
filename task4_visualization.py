# task4_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1. Load data
data = pd.read_csv("data/trends_analysed.csv")

# 2. Make folder for outputs if not exist
if not os.path.exists("outputs"):
    os.mkdir("outputs")

# -------------------------------
# 3. Chart 1: Top 10 stories by score
top10 = data.sort_values("score", ascending=False).head(10)

# shorten title if long
top10['short_title'] = top10['title'].apply(lambda x: x if len(x)<=50 else x[:47]+"...")

plt.figure(figsize=(10,6))
plt.barh(top10['short_title'], top10['score'], color="lightblue")
plt.xlabel("Score")
plt.ylabel("Story")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # highest on top
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------
# 4. Chart 2: Number of stories per category
cat_count = data['category'].value_counts()

plt.figure(figsize=(10,6))
colors = ["red","green","blue","orange","purple","brown","pink","gray","cyan","yellow"]
plt.bar(cat_count.index, cat_count.values, color=colors[:len(cat_count)])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------------------------------
# 5. Chart 3: Score vs Comments
popular = data[data['is_popular']==True]
non_popular = data[data['is_popular']==False]

plt.figure(figsize=(10,6))
plt.scatter(popular['score'], popular['num_comments'], color="green", label="Popular")
plt.scatter(non_popular['score'], non_popular['num_comments'], color="red", label="Non-Popular")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------------------------------
# 6. Bonus: Dashboard combine all 3
fig, ax = plt.subplots(1,3, figsize=(24,6))

# chart1
ax[0].barh(top10['short_title'], top10['score'], color="lightblue")
ax[0].invert_yaxis()
ax[0].set_title("Top 10 Stories")

# chart2
ax[1].bar(cat_count.index, cat_count.values, color=colors[:len(cat_count)])
ax[1].set_title("Stories per Category")
ax[1].tick_params(axis='x', rotation=45)

# chart3
ax[2].scatter(popular['score'], popular['num_comments'], color="green", label="Popular")
ax[2].scatter(non_popular['score'], non_popular['num_comments'], color="red", label="Non-Popular")
ax[2].set_title("Score vs Comments")
ax[2].legend()

fig.suptitle("TrendPulse Dashboard")
plt.tight_layout(rect=[0,0,1,0.95])
plt.savefig("outputs/dashboard.png")
plt.close()
print("Chart1 saved")
print("Chart2 saved")
print("Chart3 saved")
print("Dashboard saved")