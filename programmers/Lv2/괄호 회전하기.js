function solution(s) {
  if (s.length % 2 === 1) return 0;
  const len = s.length;
  let answer = 0;

  for (let i = 0; i < len; i++) {
    const stack = [];
    const str = i === 0 ? s : s.slice(i) + s.slice(0, i);
    
    let check = true;
    for (let n of str) {
      if (n === "(" || n === "{" || n === "[") stack.push(n);
      else {
        const bracket = stack.pop();
        if (n === ")" && bracket === "(") continue;
        if (n === "}" && bracket === "{") continue;
        if (n === "]" && bracket === "[") continue;
        check = false;
        break;
      }
    }
    if (check) answer++;
  }
  return answer;
}