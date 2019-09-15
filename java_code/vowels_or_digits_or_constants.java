import java.util.*;
public class checkchar {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		char a = sc.next().charAt(0);
		if(Character.isDigit(a)){
			System.out.print(a+" is a number");
		}
		else if(a=='a' || a=='e' || a=='i' || a=='o' || a=='u'){
			System.out.print(a+" is Vowels");
		}
		else{
			System.out.print(a+" is constant");
		}
	}
}
