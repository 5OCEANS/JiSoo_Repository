function solution(s) {
  var answer = [0, 0];
  let l = 0;
  while (s.length > 1) {
    l = s.length;
    s = s.split("0").join("");
    answer[0]++;
    answer[1] += l - s.length;
    s = s.length.toString(2);
  }

  return answer;
}
