import java.util.Scanner;

public class ATM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000.00; // Initial balance
        int choice;

        System.out.println("=== Welcome to the ATM ===");

        do {
            System.out.println("\n1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Your Balance: $" + balance);
                    break;

                case 2:
                    System.out.print("Enter deposit amount: $");
                    double deposit = sc.nextDouble();
                    if (deposit > 0) {
                        balance += deposit;
                        System.out.println("Deposited: $" + deposit);
                    } else {
                        System.out.println("Invalid amount!");
                    }
                    break;

                case 3:
                    System.out.print("Enter withdrawal amount: $");
                    double withdraw = sc.nextDouble();
                    if (withdraw > 0 && withdraw <= balance) {
                        balance -= withdraw;
                        System.out.println("Withdrawn: $" + withdraw);
                    } else {
                        System.out.println("Invalid amount or insufficient funds!");
                    }
                    break;

                case 4:
                    System.out.println("Thank you for using the ATM!");
                    break;

                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        } while (choice != 4);

        sc.close();
    }
}
