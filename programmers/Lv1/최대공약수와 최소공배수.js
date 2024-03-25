function solution(n, m) {
  var answer = [];

  const g = (a, b) => (a % b === 0 ? b : g(b, a % b));
  const l = (a, b) => (a * b) / g(a, b);
  answer = [g(n, m), l(n, m)];

  return answer;
}
