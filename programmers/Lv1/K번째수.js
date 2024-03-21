function solution(array, commands) {
  var answer = [];
  for (let i = 0; i < commands.length; i++) {
    var l = array.slice(commands[i][0] - 1, commands[i][1] );
    l.sort((a, b) => {
      return a - b;
    });
    answer.push(l[commands[i][2] - 1]);
  }

  return answer;
}
