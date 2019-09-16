import java.util.*;
public class maxmin {
	public static void main(String[] args){
		Scanner sc = new Scanner (System.in);
		int n = sc.nextInt();
		int i =0;
		int []a=new int[n];
		while(i<n){
			a[i]=sc.nextInt();
			i++;
		}
		for(int j:a){
		System.out.print(j+" ");
		}
		System.out.println();
		Arrays.sort(a);
		System.out.println(a[0]+" "+a[n-1]);
	}
}
