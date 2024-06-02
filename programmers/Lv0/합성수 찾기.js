function solution(n) {
  var answer = 0;
  for (let i = 1; i <= n; i++) {
    let c = 0;
    for (let j = 1; j <= n; j++) {
      if (i % j === 0) {
        c += 1;
      }
    }
    if (c > 2) {
      answer++;
    }
  }
  return answer;
}
