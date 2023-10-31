from datetime import datetime
import random


def increment_by_min(time, step):
    hr = time[:3]
    min = int(time[3:6])

    return hr + str(min + step)


def capture_temps(temps, count, start_time):
    print("Started capturing readings at", start_time, "\n")

    current_time = start_time

    for i in range(count):
        random_temp = random.randint(80, 120)
        temps.append(random_temp)

        current_time = increment_by_min(current_time, step=1)

        print("Saved reading", random_temp, "at",
              current_time)

    print("\nStopped capturing readings at", current_time, "\n")


def print_sorted_temps(temps, start_time):
    temps.sort()
    print_temps(temps, start_time)


def print_temps(temps, start_time):
    for i in range(len(temps)):
        print(increment_by_min(start_time, i), ":", temps[i])


temps = []

count = 10

start_time = datetime.now().time().strftime("%H:%M")

# Able to modify the empty list and fill it with temp readings
capture_temps(temps, count, start_time)

end_time = increment_by_min(start_time, count)

print("Sorted Temperature Readings\n")
print_sorted_temps(temps, start_time)

print("Original Temperature Readings")
print_temps(temps, start_time)
