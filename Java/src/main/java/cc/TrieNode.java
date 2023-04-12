package cc;

import java.util.HashMap;

public class TrieNode {
	private HashMap<Character, TrieNode> children = new HashMap<>();
	private boolean endOfWord;

	public HashMap<Character, TrieNode> getChildren() {
		return children;
	}

	public boolean isEndOfWord() {
		return endOfWord;
	}

	public void setEndOfWord(boolean endOfWord) {
		this.endOfWord = endOfWord;
	}
}
