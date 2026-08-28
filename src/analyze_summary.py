import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../data/drug_summary.csv")

print(df.head())
print("\nNumber of drugs:", len(df))

top_cost = df.sort_values("Tot_Drug_Cst", ascending=False).head(10)

print("\nTOP 10 DRUGS BY TOTAL COST:")
print(top_cost[["Brnd_Name", "Tot_Drug_Cst"]])

top_claims = df.sort_values("Tot_Clms", ascending=False).head(10)

print("\nTOP 10 DRUGS BY TOTAL CLAIMS:")
print(top_claims[["Brnd_Name", "Tot_Clms"]])

top_cost_per_claim = df.sort_values("Cost_Per_Claim", ascending=False).head(10)

print("\nTOP 10 DRUGS BY COST PER CLAIM:")
print(top_cost_per_claim[["Brnd_Name", "Cost_Per_Claim"]])

plt.bar(top_cost["Brnd_Name"], top_cost["Tot_Drug_Cst"])
plt.title("Top 10 Medicare Part D Drugs by Total Cost")
plt.xlabel("Drug")
plt.ylabel("Total Drug Cost ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/top_10_total_cost.png")
plt.show()

plt.bar(top_claims["Brnd_Name"], top_claims["Tot_Clms"])
plt.title("Top 10 Medicare Part D Drugs by Total Claims")
plt.xlabel("Drug")
plt.ylabel("Total Claims")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../images/top_10_total_claims.png")
plt.show()

plt.bar(top_cost_per_claim["Brnd_Name"], top_cost_per_claim["Cost_Per_Claim"])
plt.title("Top 10 Medicare Part D Drugs by Cost Per Claim")
plt.xlabel("Drug")
plt.ylabel("Cost Per Claim ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/top_10_cost_per_claim.png")
plt.show()