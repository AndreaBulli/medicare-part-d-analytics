import pandas as pd

file_path = "../data/MUP_DPR_RY26_P04_V10_DY24_NPIBN.csv"

chunk_size = 100_000

drug_totals = {}
claim_totals = {}

print("Starting full Medicare Part D analysis...")

for chunk_number, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size), start=1):
    cost_summary = chunk.groupby("Brnd_Name")["Tot_Drug_Cst"].sum()
    claim_summary = chunk.groupby("Brnd_Name")["Tot_Clms"].sum()

    for drug, cost in cost_summary.items():
        drug_totals[drug] = drug_totals.get(drug, 0) + cost

    for drug, claims in claim_summary.items():
        claim_totals[drug] = claim_totals.get(drug, 0) + claims

    print(f"Finished chunk {chunk_number}")

print("\nFinished processing dataset!")
top_10_drugs = sorted(drug_totals.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 DRUGS BY TOTAL COST:")
for drug, cost in top_10_drugs:
    print(f"{drug}: ${cost:,.2f}")

claim_totals = {}

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    summary = chunk.groupby("Brnd_Name")["Tot_Clms"].sum()
    for drug, claims in summary.items():
        claim_totals[drug] = claim_totals.get(drug, 0) + claims

top_10_claims = sorted(claim_totals.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 DRUGS BY TOTAL CLAIMS:")
for drug, claims in top_10_claims:
    print(f"{drug}: {claims:,.0f}")

cost_per_claim = {drug: drug_totals[drug] / claims for drug, claims in claim_totals.items() if drug in drug_totals and claims > 0}

top_10_cost_per_claim = sorted(cost_per_claim.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 DRUGS BY COST PER CLAIM:")
for drug, cost in top_10_cost_per_claim:
    print(f"{drug}: ${cost:,.2f}")

results = pd.DataFrame({
    "Brnd_Name": list(drug_totals.keys()),
    "Tot_Drug_Cst": list(drug_totals.values()),
    "Tot_Clms": [claim_totals.get(drug, 0) for drug in drug_totals]
})

results["Cost_Per_Claim"] = results["Tot_Drug_Cst"] / results["Tot_Clms"]

results.to_csv("../data/drug_summary.csv", index=False)

print("\nSaved summarized results to drug_summary.csv")