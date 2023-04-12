package cc;

import java.util.ArrayList;
import java.util.List;

public class Weighted {
	private final Trie trie;
	private final ArrayList<String[]> decoded;

	public Weighted(Trie trie, ArrayList<String[]> decoded) {
		this.trie = trie;
		this.decoded = decoded;
	}

	public ArrayList<Info> weight() {
		ArrayList<Info> weighted = new ArrayList<>();

		for (String[] s : decoded) {
			String[] words = s[0].split("[^a-zA-Z]");
			String shift = s[1];

			int score = 0;

			for (String word : words) {
				for (int i = 0; i < word.length(); i++) {
					String subWordStart = word.substring(i);
					String subWordEnd = word.substring(0, i);
					String subWordCenter = "";

					if (i < word.length() / 2) {
						subWordCenter = word.substring(i + 1, word.length() - i - 1);
					}

					ArrayList<String> subWords = new ArrayList<>(
							List.of(subWordStart, subWordEnd, subWordCenter)
					);

					for (String subWord : subWords) {
						if (trie.search(subWord.toUpperCase())) {
							score++;
						}
					}
				}
			}
			weighted.add(new Info(Integer.parseInt(shift), s[0], score));
		}
		return weighted;
	}
}
