function solution(price) {
  var d;
  var answer;
  if (price >= 500000) {
    return parseInt(price - price * 0.2);
  } else if (price >= 300000) {
    return parseInt(price - price * 0.1);
  } else if (price >= 100000) {
    return parseInt(price - price * 0.05);
  } else return parseInt(price);
}
