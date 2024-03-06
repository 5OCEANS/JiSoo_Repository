function solution(x, n) {
  var answer = [];
  j = x;
  for (let i = 1; i <= n; i++) {
    answer.push(x);
    x += j;
  }
  return answer;
}
