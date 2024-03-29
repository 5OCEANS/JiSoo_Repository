function solution(s, n) {
  var c =
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY                          ";
  return s
    .split("")
    .map((e) => c[c.indexOf(e) + n])
    .join("");
}
