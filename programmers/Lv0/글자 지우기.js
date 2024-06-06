function solution(my_string, indices) {
  var answer = '';
  indices.sort((a, b) => b - a);

  for (let index of indices) {
    my_string = my_string.slice(0, index) + my_string.slice(index + 1);
}

  return my_string;
}