function solution(s) {
  var answer = "";
  let w = s.split(" ");
  for (let i = 0; i < w.length; i++) {
    for (let j = 0; j < w[i].length; j++) {
      if (j % 2 == 0) {
        answer += w[i][j].toUpperCase();
      } else {
        answer += w[i][j].toLowerCase();
      }
    }
    if (i < w.length - 1) {
      answer += " ";
    }
  }

  return answer;
}
