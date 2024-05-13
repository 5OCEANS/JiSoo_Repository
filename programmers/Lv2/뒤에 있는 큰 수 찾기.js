function solution(numbers) {
  var answer = [];
  for (let i = 0; i < numbers.length; i++) {
    var num = -1;
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] < numbers[j]) {
        num = numbers[j];
        break;
      }
    }
    answer.push(num);
  }
  return answer;
}
