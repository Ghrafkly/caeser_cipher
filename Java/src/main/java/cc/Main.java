package cc;

import cc.caeser.Decoder;
import cc.caeser.Encoder;
import cc.output.Output;

import java.util.ArrayList;

public class Main {
	public Trie trie = new Trie();
	public Encoder encoder;
	public Decoder decoder;
	public Weighted weighted;
	public Ranker ranker = new Ranker();
	public Output output = new Output();

	public String encode(int shift, String message) {
		encoder = new Encoder(shift, message);
		return encoder.encode();
	}

	public ArrayList<String[]> decode(String message) {
		decoder = new Decoder(message);
		return decoder.decode();
	}

	public ArrayList<Info> rank(ArrayList<String[]> decoded) {
		weighted = new Weighted(trie, decoded);
		return ranker.ranking(weighted.weight());
	}



	public void loadDictionary() {
		ReadFile rf = new ReadFile();
		rf.readFile("Java/src/main/resources/wordList.txt");
		ArrayList<String> dictionary = rf.getDictionary();
		dictionary.forEach(trie::insert);
	}

	public static void main(String[] args) {
		Main main = new Main();
		main.loadDictionary();
		String encoded = main.encode(1, "the quick brown fox jumps over the lazy dog!?");
		ArrayList<String[]> decoded = main.decode(encoded);
		ArrayList<Info> ranked = main.rank(decoded);

		main.output.final_output(ranked, encoded);

//		System.out.println(encoded);
//		System.out.println(decoded);
//		System.out.println(weighted);
	}
}