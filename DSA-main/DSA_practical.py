class HospitalQueue:
    def __init__(self):
        # Initialize an empty list to store patients
        self.queue = []

    def enqueue(self, patient_id, name, priority):
        # Add the patient to the list as a dictionary
        self.queue.append({'id': patient_id, 'name': name, 'priority': priority})
        # Sort the queue based on priority (1 comes first)
        self.queue.sort(key=lambda x: x['priority'])
        print(f"Patient '{name}' added successfully.")

    def display_next(self):
        if not self.queue:
            print("No patients are currently waiting.")
        else:
            p = self.queue[0]
            print(f"Next patient to be treated: {p['name']} (ID: {p['id']}, Priority: {p['priority']})")

    def dequeue(self):
        if not self.queue:
            print("No patients to treat.")
        else:
            # Remove and return the first patient (highest priority)
            treated_patient = self.queue.pop(0)
            print(f"Patient '{treated_patient['name']}' has been treated and removed.")

    def display_all(self):
        if not self.queue:
            print("Queue is empty. No patients waiting.")
        else:
            print("\n--- All Waiting Patients ---")
            for p in self.queue:
                priority_type = {1: "Critical", 2: "Serious", 3: "Normal"}.get(p['priority'], "Unknown")
                print(f"ID: {p['id']} | Name: {p['name']} | Priority: {p['priority']} ({priority_type})")
            print("----------------------------\n")


# # --- Example Usage ---
# if __name__ == "__main__":
#     hq = HospitalQueue()
    
#     # 1. Add Patients (enqueue)
#     hq.enqueue(101, "Alice", 3)  # Normal
#     hq.enqueue(102, "Bob", 1)    # Critical
#     hq.enqueue(103, "Charlie", 2) # Serious
    
#     # 4. Display all waiting patients in priority order
#     hq.display_all()
    
#     # 2. Display the next patient to be treated
#     hq.display_next()
    
#     # 3. Remove a patient from the queue after treatment (dequeue)
#     hq.dequeue()
    
#     # Display remaining patients
#     hq.display_all()