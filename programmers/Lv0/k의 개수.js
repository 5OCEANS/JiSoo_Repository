function solution(i, j, k) {
  var answer = 0;
  for(let s = i;s<=j;s++){
    String(s).split("").forEach(e=>e.includes(k)&& answer++);
  }
  return answer;
}