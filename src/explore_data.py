import pandas as pd
file_path="../data/MUP_DPR_RY26_P04_V10_DY24_NPIBN.csv"
df=pd.read_csv(file_path, nrows=1000)
print(df.head())
print(df.shape)
print("\nCOLUMN NAMES:")
for col in df.columns:
    print(col)

print("\nTOP 10 DRUGS BY TOTAL COST:")
top_drugs=(
    df.groupby("Brnd_Name")["Tot_Drug_Cst"]
    .sum()
    .sort_values(ascending=False)
    .head(10))
print(top_drugs)

print("\nTOP 10 DRUGS BY TOTAL COST PER BENEFICIARY:")
print([col for col in df.columns if "Bene" in col])
valid_bene_df=df[df["Tot_Benes"]>0]
drug_summary=(
    valid_bene_df.groupby("Brnd_Name")
    .agg({
        "Tot_Drug_Cst":"sum",
        "Tot_Benes":"sum"
    })
)
drug_summary["Cost_per_Beneficiary"]=(
    drug_summary["Tot_Drug_Cst"] / drug_summary["Tot_Benes"]
)
top_cost_per_bene=(
    drug_summary
    .sort_values("Cost_per_Beneficiary", ascending=False)
    .head(10)
)
print(top_cost_per_bene)




