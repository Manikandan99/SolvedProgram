package javaapplication1;
import java.util.*;
public class JavaApplication1{

    public static void main(String[] args) {
        
    ArrayList<String> a=new ArrayList<String>();  
    Scanner sc =new Scanner(System.in);
    int n = sc.nextInt();
    int i;
    for(i=0;i<n;i++){
      String b= sc.next();
      a.add(b);
    }
    System.out.println(a);
  } 
}


input:
4
mk sk gr ar
output:
mk sk gr ar
