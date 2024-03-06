function solution(n) {
  var answer = 0;
  a = Math.sqrt(n);
  if (a == parseInt(a)) {
    answer = (a + 1) * (a + 1);
  } else {
    answer = -1;
  }
  return answer;
}
