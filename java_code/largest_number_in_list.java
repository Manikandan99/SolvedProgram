import java.util.*;
public class secondlarge {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> al = new ArrayList<Integer>();
		int n,i,t,max=0;
		n= sc.nextInt();
		while(n>0){
			t = sc.nextInt();
			al.add(t);
			n--;
		}
		for(i=0;i<al.size();i++){
			System.out.print(al.get(i)+" ");
		}
		System.out.println();
		max=Collections.max(al);
		System.out.print(max);
		
	}
}
