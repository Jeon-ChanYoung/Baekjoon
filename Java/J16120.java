package Java;
import java.util.Scanner;

public class J16120 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringBuilder stack = new StringBuilder();
        
        for(int i=0; i<input.length(); i++) {
            stack.append(input.charAt(i));
            if (stack.length() >= 4 && stack.substring(stack.length() - 4).equals("PPAP")) {
                stack.delete(stack.length() - 4, stack.length() - 1);
            }
        }

        if (stack.toString().equals("P")) {
            System.out.println("PPAP");
        } else {
            System.out.println("NP");
        }
    }
}