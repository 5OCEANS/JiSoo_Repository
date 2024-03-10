// function solution(n) {
//   var answer = 0;
//   for (let i = 2; i <= n; i++) {
//     let isp = true;
//     for (let j = 2; j < i; j++) {
//       if (i % j == 0) {
//         isp = false;
//       }
//     }
//     if (isp) {
//       answer += 1;
//     }
//   }
//   return answer;
// }

function solution(n) {
  let a = [];
  for (let i = 2; i <= n; i++) {
    a[i] = i;
  }
  for (let i = 2; i <= n; i++) {
    for (let j = i+i; j <= n; j += i) {
      a[j] = 0;
    }
  }
  return a.filter((e) => e != 0).length;
}
