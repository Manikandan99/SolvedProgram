import java.util.*;
class Main {
  public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);
   int a =sc.nextInt();
   int i,j=0,k;
   for(i=1;i<=a;i++){
     k=i;
     while(k<a)
     {
       System.out.print("  ");
       k++;
     }
     for(j=1;j<=i;j++){
       System.out.print(i+"\t");
     }
     System.out.print("\n");
   }
  }
}




input:
4
output:
   1
  2  2
 3  3  3
4  4  4   4
