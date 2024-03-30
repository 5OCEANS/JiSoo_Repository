function solution(answers) {
  var answer = [];
  var a = [1, 2, 3, 4, 5];
  var b = [2, 1, 2, 3, 2, 4, 2, 5];
  var c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;

  answers.map((an, i) => {
    if (a[i % a.length] === an) c1 += 1;
    if (b[i % b.length] === an) c2 += 1;
    if (c[i % c.length] === an) c3 += 1;
  });

  let ms = Math.max(c1, c2, c3);
  if (c1 === ms) {
    answer.push(1);
  }
  if (c2 == ms) {
    answer.push(2);
  }
  if (c3 == ms) {
    answer.push(3);
  }
  return answer;
}
