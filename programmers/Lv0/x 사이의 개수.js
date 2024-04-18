function solution(myString) {
  const answer = [];
  const x = myString.split("x");
  for (let i = 0; i < x.length; i++) {
      answer.push(x[i].length);
  }
  return answer;
}