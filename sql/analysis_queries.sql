-- Query 1: Top 10 drugs by total Medicare spending

SELECT
    Brnd_Name,
    CAST(Tot_Drug_Cst AS REAL) AS Total_Drug_Cost
FROM drug_summary
ORDER BY Total_Drug_Cost DESC
LIMIT 10;

-- Query 2: Top 10 drugs by total number of claims

SELECT
    Brnd_Name,
    CAST(Tot_Clms AS INTEGER) AS Total_Claims
FROM drug_summary
ORDER BY Total_Claims DESC
LIMIT 10;

-- Query 3: Drugs with a cost per claim greater than $10,000

SELECT
    Brnd_Name,
    ROUND(CAST(Cost_Per_Claim AS REAL), 2) AS Cost_Per_Claim
FROM drug_summary
WHERE CAST(Cost_Per_Claim AS REAL) > 10000
ORDER BY Cost_Per_Claim DESC;

-- Query 4: Rank drugs by cost per claim using a window function

SELECT
    Brnd_Name,
    ROUND(CAST(Cost_Per_Claim AS REAL), 2) AS Cost_Per_Claim,
    RANK() OVER (
        ORDER BY CAST(Cost_Per_Claim AS REAL) DESC
    ) AS Cost_Rank
FROM drug_summary
LIMIT 10;

-- Query 5: Summarize spending and claims by first letter of drug name

SELECT
    UPPER(SUBSTR(Brnd_Name, 1, 1)) AS Drug_Name_Initial,
    COUNT(*) AS Number_of_Drugs,
    ROUND(SUM(CAST(Tot_Drug_Cst AS REAL)), 2) AS Total_Spending,
    SUM(CAST(Tot_Clms AS INTEGER)) AS Total_Claims
FROM drug_summary
GROUP BY Drug_Name_Initial
ORDER BY Total_Spending DESC;

-- Query 6: Compare each drug's cost per claim to the overall average

SELECT
    Brnd_Name,
    ROUND(CAST(Cost_Per_Claim AS REAL), 2) AS Cost_Per_Claim,
    ROUND(
        (
            SELECT AVG(CAST(Cost_Per_Claim AS REAL))
            FROM drug_summary
        ),
        2
    ) AS Average_Cost_Per_Claim
FROM drug_summary
WHERE CAST(Cost_Per_Claim AS REAL) >
      (
          SELECT AVG(CAST(Cost_Per_Claim AS REAL))
          FROM drug_summary
      )
ORDER BY Cost_Per_Claim DESC
LIMIT 20;