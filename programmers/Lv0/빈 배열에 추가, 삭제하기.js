function solution(arr, flag) {
  var answer = [];

  for (let i = 0; i < arr.length; i++) {
    if (flag[i]) {
      answer.push(...Array(arr[i] * 2).fill(arr[i]));
    } else {
      answer = answer.slice(0, answer.length - arr[i]);
    }
  }
  return answer;
}
