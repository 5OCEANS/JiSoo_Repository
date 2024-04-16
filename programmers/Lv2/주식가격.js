function solution(prices) {
  var answer = [];
  for (let i = 0; i < prices.length; i++) {
    let n = prices[i]; // 현재 가격
    let j = i + 1;
    let t = 0;

    while (j < prices.length + 1) {
      if (n <= prices[j]) {
        // 내 가격이 다음 가격보다 작거나 같다면
        t += 1;
        j += 1;
        continue;
      } else if (t == 0 && n > prices[j]) {
        // 내 가격이 다음 가격보다 크면
        t = 1;
        answer.push(t);
        t = 0;
        break;
      } else if (t == 0 && j == n.length) {
        // 마지막 주식이면 0
        answer.push(t);
        break;
      }
      answer.push(t);
      t = 0;
      break;
    }
  }
  return answer;
}
