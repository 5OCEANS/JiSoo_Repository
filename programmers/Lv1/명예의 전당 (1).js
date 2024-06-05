function solution(k, score) {
  const answer = [];
  const s = [];

  for (let i = 0; i < score.length; i++) {
    s.push(score[i]);
    s.sort((a, b) => b - a);

    if (s.length >= k) answer.push(s[k - 1]);
    else answer.push(s[s.length - 1]);
  }

  return answer;
}
