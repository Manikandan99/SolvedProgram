import java.util.*;
public class EVENORODD {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		if(a%2==0){
			System.out.print("EVEN:"+a);
		}
		else{
			System.out.print("ODD:"+a);
		}
	}
}

input:
12
output:
EVEN:12
