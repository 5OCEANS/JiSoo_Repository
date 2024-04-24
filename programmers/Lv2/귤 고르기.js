function solution(k, tangerine) {
  var answer = 0;
  let c = []; // 귤 개수 저장
  tangerine.forEach((a) => (c[a] = (c[a] ?? 0) + 1)); // 크기에 따른 개수 저장
  c.sort((a, b) => b - a); // 내림차순 정렬

  while (k > 0) {
    k -= c[answer]; // 과일 개수만큼 빼주기
    answer += 1;
  }
  return answer;
}
