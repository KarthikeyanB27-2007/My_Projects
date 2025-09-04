import java.util.Scanner;

public class CricketTicketBillGenerator {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Match and ticket details
        System.out.print("Enter Team A Name: ");
        String teamA = sc.nextLine();

        System.out.print("Enter Team B Name: ");
        String teamB = sc.nextLine();

        System.out.print("Enter Venue: ");
        String venue = sc.nextLine();

        System.out.print("Enter Seat Number: ");
        String seatNo = sc.nextLine();

        System.out.print("Enter Ticket Price ($): ");
        double ticketPrice = sc.nextDouble();

        // Snack menu
        System.out.println("\n--- Snack Menu ---");
        System.out.println("1. Popcorn - $100");
        System.out.println("2. Soft Drink - $50");
        System.out.println("3. Sandwich - $120");
        System.out.println("4. No snacks");

        System.out.print("Enter number of snack items you want to order: ");
        int snackCount = sc.nextInt();
        sc.nextLine();  // consume newline

        double snackTotal = 0;

        for (int i = 1; i <= snackCount; i++) {
            System.out.print("Enter snack choice " + i + " (1-4): ");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    snackTotal += 100;
                    break;
                case 2:
                    snackTotal += 50;
                    break;
                case 3:
                    snackTotal += 120;
                    break;
                case 4:
                    break;
                default:
                    System.out.println("Invalid choice. Skipping.");
            }
        }

        double totalAmount = ticketPrice + snackTotal;

        // Display the ticket bill
        System.out.println("\n======= CRICKET MATCH TICKET BILL =======");
        System.out.println("Match         : " + teamA + " VS " + teamB);
        System.out.println("Venue         : " + venue);
        System.out.println("Seat Number   : " + seatNo);
        System.out.println("Ticket Price  : $" + ticketPrice);
        System.out.println("Snacks Amount : $" + snackTotal);
        System.out.println("Total Amount  : $" + totalAmount);
        System.out.println("=========================================");
    }
}
