function solution(numbers) {
  var sum = 0;
  for(var i=0;i<numbers.length;i++){
    sum += numbers[i];
  }

  var answer = Math.round(sum / numbers.length * 10) / 10;
  return answer;
}
