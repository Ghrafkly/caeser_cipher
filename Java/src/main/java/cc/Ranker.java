package cc;

import java.util.ArrayList;

public class Ranker {
	public ArrayList<Info> ranking(ArrayList<Info> decoded) {
		decoded.sort((o1, o2) -> o2.getWeight() - o1.getWeight());
		int rank = 1;
		int sameWeight = 0;
		int prevWeight = decoded.get(0).getWeight();

		for (Info dec : decoded) {
			if (dec.getWeight() < prevWeight) {
				rank += sameWeight;
				sameWeight = 0;
			}
			dec.setRank(rank);
			prevWeight = dec.getWeight();
			sameWeight++;
		}

		return decoded;
	}
}
