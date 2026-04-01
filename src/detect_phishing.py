import pandas as pd

PHISHING_KEYWORDS = [
 "urgent",
 "verify",
 "reset password",
 "click here",
 "suspension",
 "security alert",
 "unusual activity",
 ]

SUSPICIOUS_DOMAINS = [
 "secure-login-alert.com",
 "verify-now-mail.com",
 "pwc-security-check.net",
 ]

def calculate_risk(subject: str, body: str, sender_domain: str, has_attachment: bool) -> tuple[str, int]:
 score = 0
 text = f"{subject} {body}".lower()

 for keyword in PHISHING_KEYWORDS:
 if keyword in text:
 score += 2

 if sender_domain.lower() in SUSPICIOUS_DOMAINS:
 score += 3

 if has_attachment:
 score += 1

 if score >= 6:
 return "High", score
 if score >= 3:
 return "Medium", score
 return "Low", score

def main() -> None:
 df = pd.read_csv("sample_data/phishing_emails.csv")

 results = df.apply(
 lambda row: calculate_risk(
 row["subject"],
 row["body"],
 row["sender_domain"],
 bool(row["has_attachment"]),
 ),
 axis=1,
 )

 df["risk_level"] = results.apply(lambda x: x[0])
 df["risk_score"] = results.apply(lambda x: x[1])

 df.to_csv("output/phishing_report.csv", index=False)
 print("Phishing detection complete. Report saved to output/phishing_report.csv")

if _name_ == "_main_":
 main()
