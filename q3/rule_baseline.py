"""Rule-based keyword baseline for ESG message triage (Q3b).
Run: python rule_baseline.py  -> prints a table and writes baseline_results.csv"""
import csv, re

CATEGORY_RULES = [
    ("HAZARDOUS_MATERIAL", ["spill", "chemical", "asbestos", "hazardous", "battery leak"]),
    ("WATER", ["water", "leak", "tap", "pipe", "flood"]),
    ("ENERGY", ["air conditioning", "aircon", "lights", "heater", "power", "energy", "overnight"]),
    ("WASTE_RECYCLING", ["recycling", "bin", "waste", "rubbish", "contaminat"]),
    ("ACCESSIBILITY", ["accessible", "ramp", "lift", "wheelchair", "accessibility"]),
    ("SUPPLIER_PROCUREMENT", ["supplier", "vendor", "procurement", "purchas"]),
    ("GOVERNANCE_CONDUCT", ["bribe", "conflict of interest", "misconduct", "fraud"]),
]
TEAM = {"HAZARDOUS_MATERIAL": "FACILITIES", "WATER": "FACILITIES", "ENERGY": "FACILITIES",
        "WASTE_RECYCLING": "SUSTAINABILITY_OFFICE", "ACCESSIBILITY": "ACCESSIBILITY_OFFICE",
        "SUPPLIER_PROCUREMENT": "PROCUREMENT", "GOVERNANCE_CONDUCT": "GOVERNANCE_RISK", "OTHER": "HUMAN_REVIEW"}
CRITICAL_WORDS = ["spill", "chemical", "fire", "injur", "unsafe"]
HIGH_WORDS = ["all morning", "running", "blocked", "for two days", "still", "flooding", "overnight"]
MEDIUM_WORDS = ["again", "may not", "recurring", "keeps"]

def classify(msg):
    m = msg.lower()
    cat = next((c for c, kws in CATEGORY_RULES if any(k in m for k in kws)), "OTHER")
    if any(w in m for w in CRITICAL_WORDS): urg = "CRITICAL"
    elif any(w in m for w in HIGH_WORDS): urg = "HIGH"
    elif any(w in m for w in MEDIUM_WORDS): urg = "MEDIUM"
    else: urg = "LOW"
    return cat, urg, TEAM[cat]

MESSAGES = [
    "There is a water leak in Building C that has been running all morning.",
    "The recycling bins are contaminated again and no one seems to be checking them.",
    "The air conditioning is running overnight in an empty office.",
    "I want to report that one of our suppliers may not meet our sustainability policy.",
    "The accessible entrance near the main building has been blocked for two days.",
    # Harder edge cases added to stress-test the baseline
    "Someone left a tap running in the Building A kitchen for a minute, not a big deal, just wasteful.",
    "The lift to level 3 is out of order today, so wheelchair users can't get to the training room.",
    "There's a strong chemical smell and fumes coming from near the loading dock bins.",
]

if __name__ == "__main__":
    rows = []
    for i, msg in enumerate(MESSAGES, 1):
        cat, urg, team = classify(msg)
        rows.append({"id": i, "message": msg, "category": cat, "urgency": urg, "team": team})
        print(f"{i} | {cat:22} | {urg:8} | {team:20} | {msg}")
    with open("baseline_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
