function solution(str1, str2) {
  var answer = "";
  const a1 = str1.split("");
  const a2 = str2.split("");

  for (let i = 0; i < a1.length; i++) {
    answer += a1[i];
    for (let j = 0; j < a2.length; j++) {
      if (j == i) {
        answer += a2[j];
      }
    }
  }
  return answer;
}
