import java.util.*;
import java.lang.*;
public class strsplit {
	public static void main(String[] args){
		Scanner sc = new Scanner (System.in);
		String st = sc.nextLine();
		String []a=st.split(" ");
		for(String i : a){
			System.out.println(i);			
		}
	}
}
