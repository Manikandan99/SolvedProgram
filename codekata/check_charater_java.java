import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner sc =new Scanner(System.in);
    String a= sc.next();
    int i;
    String c=" ",d=" ";
    for(i=0;i<a.length();i++){
      if(Character.isDigit(a.charAt(i))){
        c+=a.charAt(i);
      }
      else if(Character.isLetter(a.charAt(i))){
        d+=a.charAt(i);
      }
    }
    System.out.println(c+"\n"+d);   
  }
}


Input:
m1n2o3
output:
 123
 mno
