console.log("Answer 1: ", document.documentElement.innerText.trim()
	.split("\n")  
	.map((x) => [x.substring(0, x.length/2), x.substring(x.length/2)])
	.reduce((acc, x) => {
		out = 0;
		cost = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		for (let i = 0; i<cost.length; i++) {
			l = cost.charAt(i);
			if ((x[0]).includes(l) & (x[1]).includes(l)) {
				out = out + i;
			}
		}
		return (acc + out);}, 0));
	
	
console.log("Answer 2: ", document.documentElement.innerText.trim()
	.split("\n")  
	.reduce((acc, x) => {
		if (acc[acc.length - 1].length == 3) {
			acc.push([x])
		} else {
			acc[acc.length -1].push(x)
		}
		return acc;}, [[]])
	.reduce((acc, x) => {
		out = 0;
		cost = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		for (let i = 0; i<cost.length; i++) {
			l = cost.charAt(i);
			if ((x[0]).includes(l) & (x[1]).includes(l) & (x[2]).includes(l)) {
				out = out + i;
			}
		}
		return (acc + out);}, 0))
