function solution(box, n) {
  return box.reduce((result, curr, index) => {
    result *= Math.floor(curr / n);
    return result;
  }, 1);
}
