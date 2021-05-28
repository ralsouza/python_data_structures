# Calculate Average Temperature

num_days = int(input("How many day's temperature? "))
temp_total = 0
temps_list = []

for i in range(num_days):
    temp_day = int(input(f"Day {i+1}'s high temp:"))
    temps_list.append(temp_day)
    temp_total += temps_list[i] # Sums total temps

avg_temp = round(temp_total / num_days, 2)
print(f"\nAverage {avg_temp}")

days_above_avg = 0

for i in temps_list:
    if i > avg_temp:
        days_above_avg += 1

print(f"{days_above_avg} day(s) above the average.")