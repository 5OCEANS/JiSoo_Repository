function solution(x) {
  var answer = true;
  var sum = 0;
  a = x.toString().split("");
  for (let i = 0; i < a.length; i++) {
    sum += Number(a[i]);
  }
  if (x % sum === 0) {
    answer = true;
  } else {
    answer = false;
  }
  return answer;
}
