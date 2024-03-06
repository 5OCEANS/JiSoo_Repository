function solution(s) {
  s = s.toLowerCase();
  a = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "p") {
      a++;
    }
    if (s[i] === "y") {
      a--;
    }
  }
  if (a === 0) {
    answer = true;
  } else {
    answer = false;
  }

  return answer;
}
