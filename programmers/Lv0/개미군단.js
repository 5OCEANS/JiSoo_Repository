function solution(hp) {
  var answer = 0;

  let n1 = Math.floor(hp / 5);
  let x = hp % 5;
  let n2 = Math.floor(x / 3);
  let n3 = x % 3;

  answer = n1 + n2 + n3;
  return answer;
}
