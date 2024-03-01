function solution(n) {
  //약수의 개수
  let a = [];
  for (let i = 1; i <= n; i++) {
    if (n % i == 0) {
      a.push(i);
    }
  }

  return a.length;
}
