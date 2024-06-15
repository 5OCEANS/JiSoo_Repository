function solution(l, r) {
  var answer = [];
  for (let i = l; i <= r; i++) {
    let s = String(i);
    if ([...s].every((e) => e === "5" || e === "0")) {
      answer.push(i);
    }
  }
  return answer.length !== 0 ? answer : [-1];
}
