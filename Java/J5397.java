package Java;

import java.util.Scanner;
import java.util.Stack;

public class J5397 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = Integer.parseInt(sc.nextLine());
        for(int i=0; i<L; i++) {
            String string = sc.nextLine();
            Stack<Character> left = new Stack<>();
            Stack<Character> right = new Stack<>();
    
            for(int j=0; j<string.length(); j++) {
                char record = string.charAt(j);
                if (record == '<' && !left.isEmpty()) {
                    right.add(left.pop());
                } 
    
                else if (record == '>' && !right.isEmpty()) {
                    left.add(right.pop());
                }
    
                else if (record == '-' && !left.isEmpty()) {
                    left.pop();
                }
    
                if ("<>-".indexOf(record) == -1) {
                    left.add(record);
                }
            }
    
            StringBuilder result = new StringBuilder();
            for(char c : left) {
                result.append(c);
            }
            while (!right.isEmpty()) {
                result.append(right.pop());
            }
            System.out.println(result);
        }
    }
}
