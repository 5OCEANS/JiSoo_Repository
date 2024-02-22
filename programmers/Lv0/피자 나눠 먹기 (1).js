function solution(n) {
  var answer;
  if (n%7 == 0)
    answer = Math.round(n / 7);
  else
  answer = Math.floor(n / 7 + 1);
  
  return answer;
}