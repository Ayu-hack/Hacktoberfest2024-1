//Perfect number: number which is equal to the sum of its factors other than the number itself
//Example:6, as 6=1+2+3
import java.util.*;
class PerfectNumber
{
    public static void main(String[] args) 
    {
        System.out.println("Enter a number");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum=0;
        for(int i=1;i<n;i++)
        {
            if((n%i)==0)
            sum=sum+i;
        }
        if(sum==n)
        System.out.println("It is a perfect number");
        else
        System.out.println("Not a perfect number");
    }
}
