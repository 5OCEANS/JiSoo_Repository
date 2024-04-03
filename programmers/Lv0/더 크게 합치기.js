function solution(a, b) {
  var answer = 0;
  answer = Math.max(Number(a.toString()+b.toString()),Number(b.toString()+a.toString()))
  
  return answer;
}