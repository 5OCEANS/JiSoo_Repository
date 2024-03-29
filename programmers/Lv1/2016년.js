function solution(a, b) {
  const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let d = b + 4;
  // 1월 1일이 FRI, b가 1일 때 인덱스 5
  for (let i = 0; i < a - 1; ++i) {
    d += mon[i];
  }

  return day[d % 7];
}
