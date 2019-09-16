import java.util.*;
public class stringrev {
	public static void main(String[] args){
	Scanner sc = new Scanner (System.in);
	String x = sc.next();
	StringBuilder sb =new StringBuilder(x);
	sb.reverse();
	System.out.print((sb));
   }
}
