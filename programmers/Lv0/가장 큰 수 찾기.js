function solution(array) {
  var answer = [];
  var max = 0
  for(let i=0;i<array.length;i++){
    if(max < array[i])
    max = array[i];
  }


  answer.push(max)
  answer.push(array.indexOf(max))
  return answer;
}