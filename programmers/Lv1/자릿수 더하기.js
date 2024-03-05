function solution(n) {
  var answer = 0;
  m = String(n);
  m.split("");
  for (let i = 0; i < m.length; i++) {
    answer += Number(m[i]);
  }

  return answer;
}
