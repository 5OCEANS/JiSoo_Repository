function solution(n) {
  var answer = [];
  for (let i = 0; i < n; i++) {
    let s = [];
    for (let j = 0; j < n; j++) {
      s.push(i === j ? 1 : 0);
    }
    answer.push(s);
  }
  return answer;
}
