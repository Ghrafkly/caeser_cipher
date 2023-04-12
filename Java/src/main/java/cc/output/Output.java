package cc.output;

import cc.Info;
import org.apache.commons.lang.StringUtils;

import java.util.ArrayList;

public class Output {
	public void final_output(ArrayList<Info> decoded, String encoded) {
		String header1 = StringUtils.center("Encoded Text", encoded.length());
		String row1 = StringUtils.center(encoded, encoded.length());

		System.out.println(header1);
		System.out.println("-".repeat(header1.length()));
		System.out.println(row1);
		System.out.println("-".repeat(header1.length()));

		String header2 = StringUtils.center("#", 3) + " | " + StringUtils.center("Decoded", encoded.length()) + " | " + StringUtils.center("Weight", 6) + " | " + StringUtils.center("Rank", 4);

		String row2 = "%3d | %20s | %6d | %4d%n";

		System.out.println(header2);
		System.out.println("-".repeat(header2.length()));
		for (Info dec : decoded) {
			System.out.format(row2, dec.getShift(), dec.getDecoded(), dec.getWeight(), dec.getRank());
		}
		System.out.println("-".repeat(header2.length()));
	}
}
