from datetime import datetime

failed_login_ips = {}

with open("security.log", "r") as file:

    failed_login_count = 0

    for line in file:

        if "Failed login" in line:

            failed_login_count = failed_login_count + 1

            # The split() function allows the line to be separated into a list
            parts = line.split()

            # Printing the 8th item of the list gives the IP address
            if parts[7] in failed_login_ips:
                failed_login_ips[parts[7]]["count"] = failed_login_ips[parts[7]]["count"] + 1
                failed_login_ips[parts[7]]["date"] = parts[0]
                failed_login_ips[parts[7]]["time"] = parts[1]
                failed_login_ips[parts[7]]["times"].append(datetime.strptime(parts[1], "%H:%M:%S"))
            else:
                failed_login_ips[parts[7]] = {
                    "count": 1,
                    "date": parts[0],
                    "time": parts[1],
                    "times": [datetime.strptime(parts[1], "%H:%M:%S")]
                }

failed_attempts_threshold = int(input("How many failed attempts should be considered suspicious? "))
print()
print(f"There are {failed_login_count} failed login attempts.")
print()
rapid_login_seconds = int(input("How many seconds should be considered a rapid login attempt? "))
print()
print("Suspicious IP addresses:")

suspicious_found = False
for ip, count in failed_login_ips.items():
    time_differences = []
    # Loops through the times for each IP and compares consecutive attempts
    for i in range(len(count["times"]) - 1):
        time_difference = count["times"][i + 1] - count["times"][i]
        # Converts the time difference into seconds
        time_differences.append(time_difference.total_seconds())
    if any(time <= rapid_login_seconds for time in time_differences):
        suspicious_found = True
        print(f"{ip}: The time difference between login attempts is suspicious - potential brute force attack!")
    if count["count"] >= failed_attempts_threshold:
        suspicious_found = True
        print(f"{ip}: {count['count']} failed attempts - Date: {count['date']} - Time: {count['time']}")
        print(f"Time differences between logins: {time_differences}")
        print()


if not suspicious_found:
    print("None detected.")
