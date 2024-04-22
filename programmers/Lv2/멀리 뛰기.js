function solution(n) {
  // 피보나치
  const a = new Array(n + 1).fill(0);
  a[0] = 1;
  a[1] = 1;

  for (let i = 2; i < a.length; i++) {
    a[i] = (a[i - 1] + a[i - 2]) % 1234567;
  }

  return a[a.length - 1];
}
