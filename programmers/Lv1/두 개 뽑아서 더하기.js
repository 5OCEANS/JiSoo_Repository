function solution(numbers) {
  var answer = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let k = i + 1; k < numbers.length; k++) {
      answer.push(numbers[i] + numbers[k]);
    }
    answer.sort((a, b) => {
      return a - b;
    });
  }
  let re = [...new Set(answer)]; // 중복값 제거

  return re;
}
