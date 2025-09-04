#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for patient record
struct Patient {
    char patient_id[10];
    char first_name[30];
    char last_name[30];
    char gender[10];
    char date_of_birth[15];
    char contact_number[15];
    char address[100];
    char registration_date[15];
    char insurance_provider[50];
    char insurance_number[20];
    char email[50];
};

// Function prototypes
void viewPatients();
void searchPatient();
void addPatient();

int main() {
    int choice;

    while (1) {
        printf("\n--- Hospital Management System ---\n");
        printf("1. View All Patients\n");
        printf("2. Search Patient by ID\n");
        printf("3. Add New Patient\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: viewPatients(); break;
            case 2: searchPatient(); break;
            case 3: addPatient(); break;
            case 4: printf("Exiting...\n"); exit(0);
            default: printf("Invalid choice! Try again.\n");
        }
    }
    return 0;
}

// Function to view all patients
void viewPatients() {
    struct Patient p;
    FILE *fp = fopen("patients.csv", "r");
    char line[500];

    if (!fp) {
        printf("Error opening file.\n");
        return;
    }

    printf("\n--- Patient Records ---\n");

    // Print CSV header first
    if (fgets(line, sizeof(line), fp)) {
        printf("%s", line);
    }

    // Print all lines
    while (fgets(line, sizeof(line), fp)) {
        printf("%s", line);
    }

    fclose(fp);
}

// Function to search patient by ID
void searchPatient() {
    struct Patient p;
    FILE *fp = fopen("patients.csv", "r");
    char line[500], id[10];
    int found = 0;

    if (!fp) {
        printf("Error opening file.\n");
        return;
    }

    printf("Enter Patient ID to search: ");
    scanf("%s", id);

    // Skip header
    fgets(line, sizeof(line), fp);

    while (fgets(line, sizeof(line), fp)) {
        char *token = strtok(line, ",");
        if (token && strcmp(token, id) == 0) {
            printf("? Patient Found: %s,%s\n", id, strtok(NULL, "\n"));
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("? Patient ID %s not found.\n", id);
    }

    fclose(fp);
}

// Function to add new patient
void addPatient() {
    struct Patient p;
    FILE *fp = fopen("patients.csv", "a");

    if (!fp) {
        printf("Error opening file.\n");
        return;
    }

    printf("Enter Patient ID: ");
    scanf("%s", p.patient_id);
    printf("Enter First Name: ");
    scanf("%s", p.first_name);
    printf("Enter Last Name: ");
    scanf("%s", p.last_name);
    printf("Enter Gender: ");
    scanf("%s", p.gender);
    printf("Enter Date of Birth (YYYY-MM-DD): ");
    scanf("%s", p.date_of_birth);
    printf("Enter Contact Number: ");
    scanf("%s", p.contact_number);
    printf("Enter Address: ");
    scanf(" %[^\n]s", p.address);  // reads full line with spaces
    printf("Enter Registration Date (YYYY-MM-DD): ");
    scanf("%s", p.registration_date);
    printf("Enter Insurance Provider: ");
    scanf("%s", p.insurance_provider);
    printf("Enter Insurance Number: ");
    scanf("%s", p.insurance_number);
    printf("Enter Email: ");
    scanf("%s", p.email);

    fprintf(fp, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",
            p.patient_id, p.first_name, p.last_name, p.gender,
            p.date_of_birth, p.contact_number, p.address,
            p.registration_date, p.insurance_provider,
            p.insurance_number, p.email);

    fclose(fp);
    printf("? New patient added successfully!\n");
}
