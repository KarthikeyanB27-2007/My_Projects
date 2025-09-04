#include <stdio.h>
#include <string.h>
#include <ctype.h>

void checkStrength(const char *password) {
    int hasLower = 0, hasUpper = 0, hasDigit = 0, hasSpecial = 0;
    int length = strlen(password);

    for (int i = 0; i < length; i++) {
        if (islower(password[i])) hasLower = 1;
        else if (isupper(password[i])) hasUpper = 1;
        else if (isdigit(password[i])) hasDigit = 1;
        else hasSpecial = 1;
    }

    int score = hasLower + hasUpper + hasDigit + hasSpecial;

    printf("\nPassword Entered: %s\n", password);

    if (length < 6 || score <= 1)
        printf("Password Strength: LOW\n");
    else if (length < 10 || score == 2)
        printf("Password Strength: MEDIUM\n");
    else
        printf("Password Strength: HIGH\n");
}

int main() {
    char password[100];

    printf("Enter your password: ");
    scanf("%s", password);  

    checkStrength(password);

    return 0;
}

