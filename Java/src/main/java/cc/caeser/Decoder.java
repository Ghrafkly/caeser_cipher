package cc.caeser;

import java.util.ArrayList;
import java.util.stream.Collectors;

public class Decoder {
	private final String message;
	private ArrayList<String[]> decoded = new ArrayList<>();

	public Decoder(String message) {
		this.message = message;
	}

	public ArrayList<String[]> decode() {
		char[] mArr = message.toCharArray();

		for (int i = 0; i < 95; i++) {
			ArrayList<Character> attempt = new ArrayList<>();
			for (char c : mArr) {
				attempt.add((char) (((int) c - 32 + i) % 95 + 32));
			}

			String decodedAttempt = attempt.stream()
					.map(String::valueOf)
					.collect(Collectors.joining());
			decoded.add(new String[]{decodedAttempt, String.valueOf(i+1)});
		}

		return decoded;
	}

	public static void main(String[] args) {
		Decoder decoder = new Decoder("ifmmp!xpsme");
		ArrayList<String[]> attempts = decoder.decode();

		attempts.forEach(System.out::println);
	}
}
