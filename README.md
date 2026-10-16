# ESG Cloud Automation – Assessment 3 evidence (Rohan Shah, 22648552)

Evidence repository for the Cloud Assessment 3 report.

| Folder | Contents |
|---|---|
| `q1/` | `GreenDesk_Dialogflow_ES_agent.zip` – exported Dialogflow ES agent (import via Settings > Export and Import > Restore from ZIP) |
| `q3/` | `revised_prompt.txt` – triage prompt; `llm_outputs.json` – LLM outputs for 8 messages (Claude, 16 Oct 2026) plus original-prompt comparison; `rule_baseline.py` – keyword baseline; `baseline_results.csv`, `comparison.csv` – results |
| `q4/` | `test_log.md` – NotebookLM test log and screenshots |
| `diagrams/` | Report figures |

## Q3 summary
LLM and rule-based baseline agreed on category for 8/8 messages and urgency for 6/8. Both disagreements were edge cases where the keyword baseline erred (over-rating a brief tap left running; under-rating a lift outage blocking wheelchair access).

Reproduce the baseline: `python rule_baseline.py`
