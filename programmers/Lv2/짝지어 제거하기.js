function solution(s) {
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    if (answer.length === 0 || answer[answer.lenth - 1] !== s[i]) {
      answer.push(s[i]);
    } else {
      answer.pop();
    }
  }
  if (answer.length === 0) {
    return 1;
  }

  return 0;
}
