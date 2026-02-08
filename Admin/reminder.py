from datetime import datetime, timedelta

issued_books = [
    {
        "student": "24261A6644",
        "book": "DBMS",
        "issue_date": "2024-02-01"
    }
]

today = datetime.now()

for record in issued_books:
    issue_date = datetime.strptime(record["issue_date"], "%Y-%m-%d")
    due_date = issue_date + timedelta(days=15)

    days_left = (due_date - today).days

    if days_left < 0:
        print(f"OVERDUE: {record['student']} must return {record['book']}")
    elif days_left <= 2:
        print(f"REMINDER: {record['student']} should return {record['book']} in {days_left} days")