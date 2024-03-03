function solution(array) {
  var answer = 0;
  let a = array.join("");
  let b = a.split("").map(Number);
  for (let i = 0; i < b.length; i++) {
    if (b[i] === 7) {
      answer += 1;
    }
  }
  return answer;
}
