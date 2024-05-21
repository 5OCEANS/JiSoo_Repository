function solution(order) {
  var answer = 0;
  var ns = order.toString();
  for (let i = 0; i < ns.length; i++) {
    if (ns[i] === "3" || ns[i] === "6" || ns[i] === "9") {
      answer += 1;
    }
  }
  return answer;
}
