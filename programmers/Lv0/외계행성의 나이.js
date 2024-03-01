function solution(age) {
  let a = "";
  let m = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
  let ag = age.toString();
  for (let i = 0; i < ag.length; i++) {
    a += m[ag[i]];
  }

  return a;
}
