import java.util.*;
public class ASCII {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		char a = sc.next().charAt(0);
		int b = (int)a;
		System.out.print("ASCII:"+b);
	}
}

input:
a
output:
ASCII:97

input:
A
output:
ASCII:65

input:
0
output:
ASCII:48
