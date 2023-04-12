package cc.caeser;

public class Encoder {
	private final int shift;
	private final String message;

	public Encoder(int shift, String message) {
		this.shift = shift;
		this.message = message;
	}

	public String encode() {
		char[] mArr = message.toCharArray();

		for (char c : mArr) {
			if ((int) c < 32 || (int) c > 126) {
				System.out.printf("Incorrect symbol %c:%d for encoding", c, (int) c);
				System.exit(0);
			}
		}

		for (int i = 0; i < mArr.length; i++) {
			int hold = (int) mArr[i] + shift;
			if (hold > 126) hold -= 95;
			mArr[i] = (char) hold;
		}

		return new String(mArr);
	}

	public static void main(String[] args) {
		Encoder encoder = new Encoder(1, "hello world");
		String encoded = encoder.encode();
		System.out.println(encoded);
	}

//	public String encode() {
//		StringBuilder encodedMessage = new StringBuilder();
//		for (int i = 0; i < message.length(); i++) {
//			char c = message.charAt(i);
//			if (c >= 32 && c <= 126) {
//				c += shift;
//				if (c > 126) {
//					c -= 95;
//				}
//			}
//			encodedMessage.append(c);
//		}
//		return encodedMessage.toString();
//	}
}
