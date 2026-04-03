# Mail-Shield: AI-Powered Phishing Detection and Reporting System

## Overview
Mail-Shield is a simplified public demonstration of an AI-assisted phishing detection and reporting workflow.

The original project concept was developed in an enterprise environment using Microsoft Power Automate, Copilot, and the Microsoft 365 ecosystem. This repository presents a safe portfolio version that demonstrates the underlying workflow logic without exposing confidential information.

## Problem
Manual phishing reporting is time-consuming and depends on individual users identifying suspicious emails correctly. This can delay response time and increase organizational security risk.

## Solution
This project simulates a workflow that:
- processes incoming email data for suspicious patterns
- checks for phishing indicators
- assigns a risk level
- generates a simple report for review

## Workflow

1. Email is received in mailbox
2. Power Automate checks predefined phishing conditions
3. If triggered, email is marked as suspicious
4. Alert is sent to Microsoft Teams
5. Copilot agent assigns risk score
6. Final alert is shared with cybersecurity team
   
Email Input -> Phishing Detection -> Risk Analysis -> AI Insight -> Alert System -> Dashboard Reporting

![Workflow Diagram](assets/workflow_diagram.PNG) 

## Sample Output

The system generates structured outputs that help identify and monitor phishing risk over time.


### Risk Score Trend

![Risk Score Trend](assets/risk_score_chart.PNG)

This chart shows how phishing risk scores vary over time, helping identify unusual spikes in suspicious activity.

---

### Sample Risk Classification Table

![Risk Table](assets/risk_table.png)

This table demonstrates how emails are assigned risk scores and categorized into risk levels (Low, Medium, High) based on detection logic.
These outputs simulate how the Mail-Shield system supports real-time monitoring and decision-making.

## Technologies
- Python
- pandas
- Microsoft Power Automate (enterprise implementation)
- Microsoft Copilot (enterprise implementation)
- Microsoft 365 ecosystem
- Basic data analysis and visualization for risk trends
## Detection Logic

Basic detection logic is implemented using Python for feature analysis and classification.

This is used to understand phishing patterns and supports the rule-based automation workflow.

## Features
- rule-based phishing detection
- suspicious keyword matching
- suspicious domain detection
- risk classification
- report generation

## Business Impact
- Reduced reporting time from approximately 5 minutes to near-instant execution
- Saved approximately 42 business hours per team
- Recognized among the Top 100 solutions in a PwC internal innovation competition

## Limitations

- Detection is mostly rule-based
- May generate false positives in some cases

## Note
This repository contains a sanitized demonstration version created for portfolio purposes. It does not include confidential enterprise data, internal workflows, or proprietary configurations. 
