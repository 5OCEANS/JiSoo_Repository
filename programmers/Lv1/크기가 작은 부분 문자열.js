function solution(t, p) {
  var count = 0;

  for (let i = 0; i < t.length; i++) {
    var nt = t.substr(i, p.length);
    if (nt.length != p.length) {
      break;
    }
    if (Number(nt) <= Number(p)) {
      count += 1;
    }
  }
  return count;
}
