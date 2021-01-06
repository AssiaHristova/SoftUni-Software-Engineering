days = int(input())

patients_done = 0
patients_left = 0
doctors = 7

for day in range(1, days + 1):
    patients = int(input())
    if day % 3 == 0:
        if patients_left > patients_done:
            doctors += 1
    if patients <= doctors:
        patients_done += patients
    else:
        patients_done += doctors
        patients_left += patients - doctors

print(f"Treated patients: {patients_done}.")
print(f"Untreated patients: {patients_left}.")


