a=int(input())
i=0
profitPerClick=list(map(int, input().split()))
avgNumClicks=list(map(int, input().split()))
maxPPerIndex=profitPerClick.index(max(profitPerClick))
maxAvgClicksIndex=avgNumClicks.index(max(avgNumClicks))
record=0
while i<int(a):
  if max(profitPerClick)!=0 and max(avgNumClicks)!=0:
    record=record+ max(profitPerClick)*max(avgNumClicks)
    profitPerClick[maxPPerIndex]=0
    avgNumClicks[maxAvgClicksIndex]=0
    maxPPerIndex=profitPerClick.index(max(profitPerClick))
    maxAvgClicksIndex=avgNumClicks.index(max(avgNumClicks))
    i+=1
  else:
    record=record+ min(profitPerClick)*min(avgNumClicks)
    profitPerClick[maxPPerIndex]=0
    avgNumClicks[maxAvgClicksIndex]=0
    maxPPerIndex=profitPerClick.index(min(profitPerClick))
    maxAvgClicksIndex=avgNumClicks.index(min(avgNumClicks))
    i+=1
print(record)

