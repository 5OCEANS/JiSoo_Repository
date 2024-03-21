function solution(s) {
  const sn = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  sn.forEach((e, i) => {
    s = s.split(e).join(i);
  });

  return Number(s);
}
