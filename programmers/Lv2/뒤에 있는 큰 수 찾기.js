function solution(numbers) {
  var answer = new Array(numbers.length).fill(-1);
  var stack = [];
  for (let i = 0; i < numbers.length; i++) {
    // 스택이 비어있지 않고 스택 맨 위의 숫자가 현재 숫자보다 작을 때까지
    while (stack && numbers[stack.at(-1)] < numbers[i]) {
      answer[stack.pop()] = numbers[i];
    }
    stack.push(i);
  }

  return answer;
}
