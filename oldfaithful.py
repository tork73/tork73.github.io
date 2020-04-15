import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
url = "https://tork73.github.io/Data_behandling/faithful.csv"
df = pd.read_csv(url)
df.columns = ["nr", "lengde", "ventetid"]

sns.set(color_codes=True)

sns.jointplot(
    x=df["lengde"],
    y=df["ventetid"],
    kind="kde",
# #    marginal_kws=dict(bins=15),
#     xlim=(1, 6.5),
#     ylim=(40, 100)
    )
plt.show()







#print(df["ventetid"].quantile([.25, .5, .75]))

# plt.boxplot(
#     df["ventetid"],
#     vert=False,
#     widths=5,
#     patch_artist=True,
#     boxprops=dict(facecolor="lightsteelblue", color="b")
#             )
# plt.xlabel("Tid (minutt)")
# plt.show()

