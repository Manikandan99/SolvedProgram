import java.util.*;
public class stringrev {
	public static void main(String[] args){
	Scanner sc = new Scanner (System.in);
	String x = sc.next();
	String y ="";
	int i;
	for(i=x.length()-1;i>=0;i--){
		y+=x.charAt(i);
	}
	System.out.print(y);
   }
}
