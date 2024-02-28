function solution(n) {
  var answer = 0;
  var s = String(n);
  for (let i = 0; i < s.length; i++) {
    answer += parseInt(s[i]);
  }
  return answer;
}
