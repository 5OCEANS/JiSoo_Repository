function solution(num_list) {
  var answer = 0;
  while (!num_list.every((i) => i === 1)) {
    num_list.map((v, j) => {
      if (v === 1) return;
      answer++;
      num_list[j] = v % 2 ? (v - 1) / 2 : v / 2;
    });
  }
  return answer;
}
