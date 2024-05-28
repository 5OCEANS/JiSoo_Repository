function solution(number) {
  var answer = 0;
  const s = number
    .split("")
    .map(Number)
    .reduce((a, b) => a + b);
  answer = s % 9;
  return answer;
}
