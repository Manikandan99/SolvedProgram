package javaapplication1;
import java.util.*;
public class JavaApplication1 {
    public static void main(String[] args) {
         LinkedList<String> l1 = new  LinkedList<String>();         
         Scanner sc = new Scanner(System.in);         
         int n = sc.nextInt();
         while(n!=0){
             String t = sc.next();
             l1.add(t);
             n--;    
         }
        for(String i : l1){
            System.out.println(i);
        }
       
    }   
}


input:
3
mk
op
io


mk
op
io
