function solution(my_string, index_list) {
  return index_list.reduce((a, k) => a + my_string[k], "");
}
