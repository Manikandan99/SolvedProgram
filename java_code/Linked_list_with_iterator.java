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
        Iterator a = l1.iterator();
        System.out.println();
        while(a.hasNext()){
            System.out.println(a.next());           
        }   
    }   
}
input:
3
on
in
to
output:
on
in
to
