const factorial = (n) => (n === 0 ? 1 : n * factorial(n - 1));
// 재귀적으로 팩토리얼 계산 (n이 0이 될 때까지 곱함)

function solution(balls, share) {
  var answer = Math.round(
    factorial(balls) / factorial(balls - share) / factorial(share)
  );
  return answer;
}
