function solution(d, budget) {
  var c = 0;
  d.sort((a, b) => a - b);

  for (let i = 0; i < d.length; i++) {
    if (budget < d[i]) {
      break;
    }
    budget -= d[i];
    c += 1;
  }
  return c;
}
