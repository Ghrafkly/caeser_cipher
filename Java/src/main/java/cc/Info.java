package cc;

import lombok.Data;

@Data
public class Info {
	private final int shift;
	private final String decoded;
	private final int weight;
	private int rank;

	public Info(
			int shift,
			String decoded,
			int weight
	) {
		this.shift = shift;
		this.decoded = decoded;
		this.weight = weight;
	}
}
