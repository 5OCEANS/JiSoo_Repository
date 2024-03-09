function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i++) {
    var c = [];
    for (let j = 1; j <= i; j++) {
      if (i % j == 0) {
        c.push(j);
      }
    }
    if (c.length % 2 == 0) {
      answer += i;
    } else {
      answer -= i;
    }
  }
  return answer;
}
