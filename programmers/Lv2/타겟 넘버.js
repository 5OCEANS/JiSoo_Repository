function solution(numbers, target) {
  var answer = 0;
  function solv(i, sum) {
    if (i == numbers.length) {
      // numbers의 인덱스를 모두 탐색하면
      if (sum == target) answer++; // 합이 target이 되면 +1
      return;
    }
    solv(i + 1, sum + numbers[i]); // 해당 숫자 더하거나
    solv(i + 1, sum - numbers[i]); // 빼거나
  }
  solv(0, 0);
  return answer;
}
// 배열의 각 숫자는 더하거나 빼거나 두 가지
