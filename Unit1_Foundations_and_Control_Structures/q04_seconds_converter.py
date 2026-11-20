"""Q4: Convert seconds into hours, minutes and seconds."""

total = int(input("Enter duration in seconds: "))

hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60

print(f"{total} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
print(f"Formatted: {hours:02d}:{minutes:02d}:{seconds:02d}")
