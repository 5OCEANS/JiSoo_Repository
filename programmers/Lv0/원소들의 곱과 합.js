function solution(num_list) {
  s1 = 1;
  s2 = 0;
  for (let i = 0; i < num_list.length; i++) {
    s1 *= num_list[i];
    s2 += num_list[i];
  }
  if (s1 < s2 ** 2) {
    return 1;
  } else {
    return 0;
  }
}
