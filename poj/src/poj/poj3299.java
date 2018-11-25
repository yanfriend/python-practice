package poj;

import java.util.Scanner;

public class poj3299 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		while (sc.hasNext()) {
			char ch1=sc.next().charAt(0);
			if (ch1=='E') break;
			
			double n1=sc.nextDouble();
			char ch2=sc.next().charAt(0);
			double n2=sc.nextDouble();
			
			double H,T,D;
			
			if (ch1>ch2) {
				char tmp=ch1;
				ch1=ch2;
				ch2=tmp;
				double tmpd=n1;
				n1=n2;
				n2=tmpd;
			}
			
			if (ch1=='D' && ch2=='T') {
				H=n2+0.555*(6.11*Math.pow(Math.E, 5417.7530*((1/273.16)-(1/(n1+273.16))))-10.0);
				System.out.printf("T %.1f D %.1f H %.1f",n2,n1,H);
				System.out.println();
			}
					
		}
		

	}

}
