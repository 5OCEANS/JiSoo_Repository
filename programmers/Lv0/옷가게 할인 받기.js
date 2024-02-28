function solution(price) {
  var d;
  var answer;
  if(price >= 500000){
    d = 0.2;
  }
  else if(price >= 300000){
    d = 0.1;
  }
  else if(price >=100000){
    d = 0.05;
  }
  answer = Math.floor(price - price*d);
  return answer;
}