function solution(myString, pat) {
  const m = myString.toLowerCase();
  const a = pat.toLowerCase();
  if (m.includes(a)) {
    return 1;
  }
  return 0;
}
