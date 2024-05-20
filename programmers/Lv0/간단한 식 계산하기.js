function solution(binomial) {
  const n = binomial.split(" ");
  return n[1] === "+"
    ? +n[0] + +n[2]
    : n[1] === "-"
    ? +n[0] - +n[2]
    : +n[0] * +n[2];
}
