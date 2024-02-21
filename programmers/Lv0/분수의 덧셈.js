// 첫번째 방법
function solution(numer1, denom1, numer2, denom2) {
  var answer = [];

  //분자
  let num = numer1 * denom2 + numer2 * denom1;
  //분모
  let denom = denom1 * denom2;

  let a = num;
  let b = denom;

  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));

  answer[0] = a / gcd(a, b);
  answer[1] = b / gcd(a, b);

  return answer;
}

// 두번째 방법
function gcd(a, b) {
  return a % b === 0 ? b : gcd(b, a % b);
}

function solution(numer1, denom1, numer2, denom2) {
  let num = numer1 * denom2 + numer2 * denom1;
  let denom = denom1 * denom2;
  let gcdan = gcd(num, denom);

  return [num / gcdan, denom / gcdan];
}
