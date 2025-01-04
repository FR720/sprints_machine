from datetime import datetime, timedelta

def formatCurrentDateTime():
    now = datetime.now()
    formattedDate = now.strftime("%Y-%m-%d")
    formattedTime = now.strftime("%H:%M:%S")
    print(f"Current Date: {formattedDate}, Current Time: {formattedTime}")

def calculateDateArithmetic():
    today = datetime.now()
    dateInFuture = today + timedelta(days=10)
    dateInPast = today - timedelta(days=10)
    print(f"Date 10 days from today: {dateInFuture.strftime('%Y-%m-%d')}")
    print(f"Date 10 days ago: {dateInPast.strftime('%Y-%m-%d')}")

def extractDateTimeComponents():
    now = datetime.now()
    print(f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Day: {now.day}")
    print(f"Hour: {now.hour}")
    print(f"Minute: {now.minute}")
    print(f"Second: {now.second}")

# Example usage
formatCurrentDateTime()
calculateDateArithmetic()
extractDateTimeComponents()
