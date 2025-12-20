"""
******************************
Healthcare Wait Time Optimizer
******************************
This file is used to prompt users for key information and calculate wait times at three hospitals.
It must compare the wait time at the specialty hospital for the given symptom to the hospital with
the shortest wait time. The final function prints out all the results in a structured summary.
"""

# Asking for the user's name, while removing extra spaces and capitalizing their name.
patient_name = input("Enter your name: ").strip().title()

# Checking to make sure that name is not empty, and asking user for input again if so.
while patient_name == "":
    print("Name cannot be empty. ")
    patient_name = input("Enter your name: ").strip().title()

# Asking for the user's symptom, while removing extra spaces and turning it into all lower case so it is case-insensitive.
symptoms = input("Enter your most severe symptom (fever, cough, heart, other): ").strip().lower()
symptoms_list = ["fever", "cough", "heart", "other"]

# Checking to make sure that symptom is in the list, and asking user for input again if not.
while symptoms not in symptoms_list:
    print("Invalid symptom. Valid options: fever, cough, heart, other. ")
    symptoms = input("Enter your most severe symptom (fever, cough, heart, other): ").strip().lower()

# Asking for the user's urgency level, while removing extra spaces
urgency_level = input("Enter your urgency level (1 = mild, 2 = moderate, 3 = severe): ").strip()
urgency_list = ["1","2","3"]

# Checking to make sure that urgency level is in the list, and asking user for input again if not.
while urgency_level not in urgency_list:
    print("Invalid urgency level. Enter 1, 2, or 3. ")
    urgency_level = input("Enter your urgency level (1 = mild, 2 = moderate, 3 = severe): ").strip()

# Calculating wait time for each hospital, based on inputted urgency level.
VH_wait_time = (15 * 10)/int(urgency_level)
SJ_wait_time = (10 * 12)/int(urgency_level)
LHSC_wait_time = (20 * 8)/int(urgency_level)

# Creating lists for hospital name and their wait times.
hospitals = ["Victoria Hospital", "St. Joseph's Hospital", "London Health Sciences Centre"]
wait_times = [VH_wait_time, SJ_wait_time, LHSC_wait_time]

# Finding the min wait time from the list of wait times and the name of the hospital that is the fastest.
fastest_hospital_wait_time = min(wait_times)
fastest_index = wait_times.index(fastest_hospital_wait_time)
fastest_hospital = hospitals[fastest_index]

# Printing the results.
print("\n--- Results ---")
print("Patient Name:", patient_name)
print("Symptoms:", symptoms.capitalize())
print("Urgency Level:", urgency_level)
print(f"Victoria Hospital Wait Time: {VH_wait_time:.1f} minutes")
print(f"St. Joseph's Hospital Wait Time: {SJ_wait_time:.1f} minutes")
print(f"London Health Sciences Centre Wait Time: {LHSC_wait_time:.1f} minutes")

# Printing the comparison result when symptom is not other.
if symptoms != "other":
    if symptoms in symptoms_list:
        i = symptoms_list.index(symptoms)
        specialty_hospital_wait_time = wait_times[i]
        difference = specialty_hospital_wait_time - fastest_hospital_wait_time
        print(f"Specialty hospital wait time: {specialty_hospital_wait_time} minutes. "
              f"Fastest hospital: {fastest_hospital} with {fastest_hospital_wait_time} minutes. "
              f"Difference: {difference} minutes. "
        )

# Printing the comparison result when symptom is other.
if symptoms == "other":
    print(f"Fastest hospital: {fastest_hospital} with {fastest_hospital_wait_time} minutes. "
          "No specialty hospital for your symptom. "
          )
