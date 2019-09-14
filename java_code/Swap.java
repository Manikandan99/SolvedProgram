import java.util.*;
public class swapping {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		System.out.println("Before swap: "+a+" "+b);
		String t="";
		t=a;
		a=b;
		b=t;
		System.out.print("After swap: "+a+" "+b);	
	}
}

Input:
10 20
Output:
Before swap: 10 20
After swap: 20 10
