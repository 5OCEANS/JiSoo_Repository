function solution(n) {
  let arr = n.toString(2).split("");
  let c = arr.filter((one) => one === "1").length;
  let c2;
  while (c !== c2) {
    ++n;
    c2 = n
      .toString(2)
      .split("")
      .filter((one) => one === "1").length;
  }
  return n;
}
