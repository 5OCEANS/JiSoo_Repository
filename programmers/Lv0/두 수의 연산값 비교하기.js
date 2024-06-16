function solution(a, b) {
  const str = a.toString() + b.toString()
  if (str > 2 * a * b) {
      return Number(str)
  } else if (str === 2 * a * b) {
      return Number(str)
  } else {
      return 2 * a * b
  }
}