function solution(my_string, num1, num2) {
  const stringArr = my_string.split("");

  const n1 = my_string[num1];
  const n2 = my_string[num2];

  stringArr.splice(num1, 1, n2);
  stringArr.splice(num2, 1, n1);

  return stringArr.join("");
}

// function solution(my_string, num1, num2) {
//   my_string = my_string.split('');
//   [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
//   return my_string.join('');
// }
