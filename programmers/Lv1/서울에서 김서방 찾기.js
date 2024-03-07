function solution(seoul) {
  let answer = '';
  for (let i = 0; i < seoul.length; i++) {
    if (seoul[i] == "Kim") {
      k = i;
    }
  }
  answer = `김서방은 ${k}에 있다`;
  return answer;
}
