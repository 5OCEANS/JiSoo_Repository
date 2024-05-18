function solution(num_list) {
  let o = 0;
  let e = 0;
  for (let i of num_list) {
    if (i % 2 === 1) {
      o += i.toString();
    } else {
      e += i.toString();
    }
  }
  return parseInt(o) + parseInt(e);
}
