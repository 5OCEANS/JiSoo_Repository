function solution(s) {
  var answer = 0;
  let st = [];
  for (let i = 0; i < s.length; i++) {
    st.push(s[i]);

    const same = st.filter((i) => i === st[0]);
    const nsame = st.filter((i) => i !== st[0]);

    if (same.length === nsame.length) {
      answer += 1;
      st = [];
    }
  }
  if (st.length !== 0) {
    answer += 1;
  }
  return answer;
}
