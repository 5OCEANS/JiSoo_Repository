function solution(my_string) {
  
  let newarr=[...new Set(my_string)];
  
  return newarr.join('');
}