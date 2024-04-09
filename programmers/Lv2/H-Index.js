function solution(citations) {
  var answer = 0;
  citations = citations.sort((a, b) => b - a);
  let ar = [];
  for (let i = 0; i < citations.length; i++) {
    ar.push(citations[i]);
    if (citations[i] < ar.length) {
      break;
    }
    answer += 1;
  }
  return answer;
}
