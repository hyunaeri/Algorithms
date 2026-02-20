import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        BigInteger fac = new BigInteger("1");
        for (int i = 2; i <= n; i++) {
            fac = fac.multiply(new BigInteger(Integer.toString(i)));
        }
        int count = 0;
        while (true) {
            BigInteger num = fac.remainder(new BigInteger("10"));
            if (num.equals(new BigInteger("0"))) {
                count++;
            } else {
                break;
            }
            fac = fac.divide(new BigInteger("10"));
        }
        System.out.print(count);
    }
}