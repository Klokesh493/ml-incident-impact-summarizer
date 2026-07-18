import csv
import sys


def summarize(rows):
    endpoints = {row["endpoint"] for row in rows}
    models = {row["model"] for row in rows}
    users = sum(int(row["affected_users"]) for row in rows)
    severity = "sev1" if users >= 10000 or len(endpoints) >= 3 else "sev2" if users >= 1000 else "sev3"
    return {"models": len(models), "endpoints": len(endpoints), "affected_users": users, "severity": severity}


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        print(summarize(list(csv.DictReader(handle))))


if __name__ == "__main__":
    main(sys.argv[1])
