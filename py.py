#make_bricks(3, 1, 8) → True
#make_bricks(3, 1, 9) → False
#make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  #small 1'
  #big 5'
	if(goal > big*5 +small):
		return False
	if(goal%5 > small):
		return False
	return True
    
print (make_bricks(3,1,8)	)
print (make_bricks(3,1,9)  )
print (make_bricks(3,2,10))