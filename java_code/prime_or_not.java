import java.util.*;
public class prime {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int i,f=0;
		for(i = 2 ; i <a/2;i++){
			if(a%i==0){
				f=1;
			}
		}
		if(f==1){
			System.out.print(a+" is not prime");
		}
		else{
			System.out.print(a+" is prime");
		}
	}
}
