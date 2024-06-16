function solution(intStrs, k, s, l) {
  let result = [];

  for (let str of intStrs) {
      let subStr = str.substring(s, s + l);
      let num = parseInt(subStr, 10);
      if (num > k) {
          result.push(num);
      }
  }

  return result;
}