function solution(players, callings) {
  let temp=0;
  for(let i=0;i<callings.length;i++){
      for(let j=1;j<players.length;j++){
          if(players[j]===callings[i]){
              temp = players[j-1]
              players[j-1]=players[j]
              players[j]=temp 
          }
      }
  }
  return players;
}