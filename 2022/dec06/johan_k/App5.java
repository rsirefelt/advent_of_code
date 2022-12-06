import java.util.*;

public class App5 {
	static int getAns(String input, int l) {
		HashSet<String> bucket = new HashSet<String>();
		String[] tmp;
		for (int n = 0; n < input.length()-l+1; n++) {
			bucket.clear();
			tmp = input.substring(n, n + l).split("");
			if (Arrays.stream(tmp).allMatch(bucket::add)) {
				return n+l;
			}
		}
		return -1;
	}

	public static void main(String args[]){
		System.out.println(getAns(args[0], 4));
		System.out.println(getAns(args[0], 14));
	}
}
