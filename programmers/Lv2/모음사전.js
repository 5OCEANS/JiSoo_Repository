function solution(word) {
  const v = ["A", "E", "I", "O", "U"];
  const w = [];

  function everyWord(cw, d) {
    if (d >5) return;
    w.push(cw); // 현재까지 만들어진 단어 추가
    for (let vo of v) {
      everyWord(cw + vo, d + 1);
    }
  }
  everyWord("", 0);

  const i = w.indexOf(word);
  return i + 1;

}
