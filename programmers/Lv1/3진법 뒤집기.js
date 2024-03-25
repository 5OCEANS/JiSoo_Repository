function solution(n) {
  const t = n.toString(3);
  const k = t.split("").reverse().join("");

  return parseInt(k,3);
}
