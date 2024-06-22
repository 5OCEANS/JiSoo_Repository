function solution(s) {
  var answer = [];
  for (let c of s) if (s.indexOf(c) === s.lastIndexOf(c)) answer.push(c);
  return answer.sort().join("");
}
