fn readfile(file: &str) -> String {
	return std::fs::read_to_string(file).expect("Couldn't read input");
}

fn funk(input: &str) -> (usize, usize) {
	let stream = input
		.lines()
		.map(|val| -> Vec<i32> {
				val.split(&[',', '-'])
					.filter_map(|value| value.parse::<i32>().ok())
					.collect::<Vec<i32>>()
			})
		.map(|x| {	(x[0]..=x[1], x[2]..=x[3]) });
	return (
		stream.clone().filter(|(elf_a, elf_b)| -> bool {
			return (elf_b.contains(elf_a.start()) && elf_b.contains(elf_a.end())) ||
				(elf_a.contains(elf_b.start()) && elf_a.contains(elf_b.end()));
		}).count(),
		stream.clone().filter(|(elf_a, elf_b)| -> bool {
			return (elf_b.contains(elf_a.start()) || elf_b.contains(elf_a.end())) ||
				(elf_a.contains(elf_b.start()) || elf_a.contains(elf_b.end()));
		}).count()
	);
}

fn main() {
	let answers: (usize, usize) = funk(&readfile("input4.txt"));
	println!("Answers: {:?}", answers);
}
