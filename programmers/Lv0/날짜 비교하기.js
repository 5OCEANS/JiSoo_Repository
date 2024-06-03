function solution(date1, date2) {
  var answer = 0;
  let [a1, b1, c1] = date1;
  let [a2, b2, c2] = date2;

  if (a1 !== a2) return a1 < a2 ? 1 : 0;
  if (b1 !== b2) return b1 < b2 ? 1 : 0;
  if (c1 !== c2) return c1 < c2 ? 1 : 0;

  return answer;
}
