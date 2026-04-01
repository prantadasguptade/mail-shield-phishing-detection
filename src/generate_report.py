import pandas as pd

def main() -> None:
 df = pd.read_csv("output/phishing_report.csv")

 print("Mail-Shield Summary Report")
 print("--------------------------")
 print(f"Total emails analyzed: {len(df)}")
 print()

 risk_counts = df["risk_level"].value_counts()

 for level in ["High", "Medium", "Low"]:
 print(f"{level} Risk Emails: {risk_counts.get(level, 0)}")

 high_risk = df[df["risk_level"] == "High"]

 if not high_risk.empty:
 print("\nHigh Risk Alerts")
 print("----------------")
 for _, row in high_risk.iterrows():
 print(f"Subject: {row['subject']}")
 print(f"Sender Domain: {row['sender_domain']}")
 print(f"Risk Score: {row['risk_score']}")
 print("-" * 20)

if _name_ == "_main_":
 main()
