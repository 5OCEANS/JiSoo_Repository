function solution(n) {
  a = String(n).split("");

  var answer = [];
  for (let i = a.length - 1; i >= 0; i--) {
    answer.push(Number(a[i]));
  }
  return answer;
}
