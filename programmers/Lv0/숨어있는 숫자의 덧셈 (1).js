function solution(my_string) {
  var answer = 0;
  let a = my_string.split("");
  for (let i = 0; i < a.length; i++) {
    if (Number(a[i])) {
      answer += parseInt(a[i]);
    }
  }

  return answer;
}
