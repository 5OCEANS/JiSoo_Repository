function solution(price, money, count) {
  var answer = -1;
  s = 0;
  for (let i = 1; i <= count; i++) {
    s += price * i;
  }
  if (s > money) {
    answer = s - money;
  } else {
    answer = 0;
  }

  return answer;
}
