function solution(arr) {
  var answer = [];

  if (arr.length == 1) {
    answer.push(-1);
  }
  let min = Math.min(...arr);
  arr.map((e) => {
    if (e != min) {
      answer.push(e);
    }
  });
  return answer;
}
