import random


def printer(iteration,states, Values, policy):
  if iteration <= 10 or iteration == 100:
    print("iter %2d:"%iteration)
    for s in states:
      string = str(s)
      if s in policy:
        print("State " + string + "  V = %.3f    Best Action: %d" % (Values[s], policy[s]))
      else:
        print("State " + string + "  V = %.3f  " % Values[s])
  


print("hello, please type the letter of the following options aka: a")
print("a)  gamma = 1")
print("b)  gama = .8")
print("c)  gamma = .2")
print("d)  gamma = .9 and noise = .2  Don't have this")


GAMMA = 1 
NOISE = 0.0 
inputs = str(input())
# state = '123456789'


if inputs == 'a':
  GAMMA = 1
if inputs == 'b':
  GAMMA = .8
if inputs == 'c':
  GAMMA = .2
if inputs == 'd':
  GAMMA = .9
  NOISE = .2
#Parameters

# change this to see if values change after iteration
      


#Define all states
states=[]
for i in range(1,6):
    for j in range(1,6):
      if i == 2 and j == 2:
        GAMMA = GAMMA
      elif i == 2 and j == 3:
        GAMMA = GAMMA
      elif i == 3 and j == 2:
        GAMMA = GAMMA
      else:
        for d in range(1,5):
          states.append((i, j, d))



actions = {}
# (1: up, 2: down, 3: left, and 4: right).
#1 forward  2 forward2  3 turn right  4 turn left
actions = {
    (1, 1, 1):(1, 2, 3, 4), 
    (1, 1, 2):(3, 4),
    (1, 1, 3):(3, 4),
    (1, 1, 4):(1, 2, 3, 4),

    (2, 1, 1):(3, 4), 
    (2, 1, 2):(3, 4),
    (2, 1, 3):(1, 3, 4),
    (2, 1, 4):(1, 2, 3, 4),

    (3, 1, 1):(3, 4), 
    (3, 1, 2):(3, 4),
    (3, 1, 3):(1, 2, 3, 4),
    (3, 1, 4):(1, 2, 3, 4),

    (4, 1, 1):(1, 2, 3, 4), 
    (4, 1, 2):(3, 4),
    (4, 1, 3):(1, 2, 3, 4),
    (4, 1, 4):(1, 3, 4),

    (5, 1, 1):(1, 2, 3, 4), 
    (5, 1, 2):(3, 4),
    (5, 1, 3):(1, 2, 3, 4),
    (5, 1, 4):(3, 4),
    #################################################

    (1, 2, 1):(1, 2, 3, 4), 
    (1, 2, 2):(1, 3, 4),
    (1, 2, 3):(3, 4),
    (1, 2, 4):(3, 4),

    (4, 2, 1):(1, 2, 3, 4), 
    (4, 2, 2):(1, 3, 4),
    (4, 2, 3):(3, 4),
    (4, 2, 4):(1, 3, 4),

    (5, 2, 1):(1, 3, 4), 
    (5, 2, 2):(1, 3, 4),
    (5, 2, 3):(1, 3, 4),
    (5, 2, 4):(3, 4),

    #################################################

    #################################################

    (1, 3, 1):(1, 2, 3, 4), 
    (1, 3, 2):(1, 2, 3, 4),
    (1, 3, 3):(3, 4),
    (1, 3, 4):(3, 4),
  
    (3, 3, 1):(1, 2, 3, 4), 
    (3, 3, 2):(3, 4),
    (3, 3, 3):(3, 4),
    (3, 3, 4):(1, 2, 3, 4),

    (4, 3, 1):(2, 3, 4), 
    (4, 3, 2):(1, 2, 3, 4),
    (4, 3, 3):(1, 3, 4),
    (4, 3, 4):(1, 3, 4),

    (5, 3, 1):(3, 4), 
    (5, 3, 2):(1, 2, 3, 4),
    (5, 3, 3):(1, 2, 3, 4),
    (5, 3, 4):(3, 4),

    #################################################

    (1, 4, 1):(1, 3, 4), 
    (1, 4, 2):(1, 2, 3, 4),
    (1, 4, 3):(3, 4),
    (1, 4, 4):(1, 2, 3, 4),

    (2, 4, 1):(1, 3, 4), 
    (2, 4, 2):(3, 4),
    (2, 4, 3):(1, 3, 4),
    (2, 4, 4):(1, 2, 3, 4),

    (3, 4, 1):(1, 3, 4), 
    (3, 4, 2):(1, 3, 4),
    (3, 4, 3):(1, 2, 3, 4),
    (3, 4, 4):(1, 2, 3, 4),

    (5, 4, 1):(1, 3, 4), 
    (5, 4, 2):(3, 4),
    (5, 4, 3):(1, 2, 3, 4),
    (5, 4, 4):(3, 4),

    #################################################

    (1, 5, 1):(3, 4), 
    (1, 5, 2):(1, 2, 3, 4),
    (1, 5, 3):(3, 4),
    (1, 5, 4):(1, 3, 4),

    (2, 5, 1):(3, 4), 
    (2, 5, 2):(1, 3, 4),
    (2, 5, 3):(1, 3, 4),
    (2, 5, 4):(3, 4),

    (3, 5, 1):(3, 4), 
    (3, 5, 2):(1, 2, 3, 4),
    (3, 5, 3):(3, 4),
    (3, 5, 4):(1, 2, 3, 4),

    (4, 5, 1):(3, 4), 
    (4, 5, 2):(1, 2, 3, 4),
    (4, 5, 3):(1, 3, 4),
    (4, 5, 4):(1, 3, 4),

}

policy ={}
for s in actions:
  policy[s] = random.randrange(1,5)
  # print(s)
  # print(policy[s])

# print(policy)


Values = {}
for s in states:
  if s in actions.keys():
    Values[s] = 0
  if s == (5, 5, 1) or s == (5, 5, 2) or s == (5, 5, 3) or s == (5, 5, 4):
      Values[s]=100
  if s == (4, 4, 1) or s == (4, 4, 2) or s == (4, 4, 3) or s == (4, 4, 4) :
      Values[s]=-1000
# print(V)
# printer(1,states,Values, policy)

# print(Values[[1,1,1]])

s = states[0]
s = [s[0]+1, s[1], s[2]]
# states[1][0] = 2
# # states = tuple(states)
# # print(states[1])
iteration = 1
# printer(1,states,Values,policy)
while iteration <=1:

  for s in states:

    if s in policy:

      old_V = Values[s]
      new_V = 0

      for a in actions[s]:
        print(len(actions[s]))
        cost = 0
        
##############################
        # If the state is looking up
        if s[2] == 1:
          # looking up, move forward 1 space
          if a == 1:
            x = s[0]
            y = s[1]+1
            d = s[2]
            s_prime = s[0], s[1]+1, s[2]
            cost = 1.5
            
          # looking up, move forward 2 space
          if a == 2:
            x = s[0]
            y = s[1]+2
            d = s[2]
            s_prime = s[0], s[1]+2, s[2]
            cost = 2

          # looking up, turn left
          if a == 3:
            x = s[0]
            y = s[1]
            d = 3
            s_prime = s[0], s[1], 3
            cost = .5

          # looking up, turn right
          if a == 4:
            x = s[0]
            y = s[1]
            d = 4
            s_prime = s[0], s[1], 4
            cost = .5
##############################
        # If the state is looking down
        if s[2] == 2:
          # looking down, move forward 1 space
          if a == 1:
            x = s[0]
            y = s[1]-1
            d = s[2]
            s_prime = s[0], s[1]-1, s[2]
            cost = 1.5
            
          # looking down, move forward 2 space
          if a == 2:
            x = s[0]
            y = s[1]-2
            d = s[2]
            s_prime = [s[0], s[1]-2, s[2]]
            cost = 2

          # looking down, turn left
          if a == 3:
            x = s[0]
            y = s[1]
            d = 4
            s_prime = [s[0], s[1], 4]
            cost = .5

          # looking down, turn right
          if a == 4:
            x = s[0]
            y = s[1]
            d = 3
            s_prime = [s[0], s[1], 3]
            cost = .5
##############################
        # If the state is looking left
        if s[2] == 3:
          # looking left, move forward 1 space
          if a == 1:
            x = s[0]-1
            y = s[1]
            d = s[2]
            s_prime = s[0]-1, s[1], s[2]
            cost = 1.5
            
          # looking left, move forward 2 space
          if a == 2:
            x = s[0]-2
            y = s[1]
            d = s[2]
            s_prime = s[0]-2, s[1], s[2]
            cost = 2

          # looking left, turn left
          if a == 3:
            x = s[0]
            y = s[1]
            d = 2
            s_prime = s[0], s[1], 2
            cost = .5

          # looking left, turn right
          if a == 4:
            x = s[0]
            y = s[1]
            d = 1
            s_prime = s[0], s[1], 1
            cost = .5

##############################
        # If the state is looking right
        if s[2] == 4:
          # looking right, move forward 1 space
          if a == 1:
            x = s[0]+1
            y = s[1]
            d = s[2]
            s_prime = s[0]+1, s[1], s[2]
            cost = 1.5
            
          # looking right, move forward 2 space
          if a == 2:
            x = s[0]+2
            y = s[1]
            d = s[2]
            s_prime = s[0]+2, s[1], s[2]
            cost = 2

          # looking right, turn left
          if a == 3:
            x = s[0]
            y = s[1]
            d = 1
            s_prime = s[0], s[1], 1
            cost = .5

          # looking right, turn right
          if a == 4:
            x = s[0]
            y = s[1]
            d = 2
            s_prime = s[0], s[1], 2
            cost = .5
            

##############################
# For noise and chance

        # if NOISE > 0:
        #   for p in actions[s]:
        #     print()
        #   print()
##############################
# for only Gamma
        # print(Values[s_prime[0],s_prime[1], s_prime[2] ])
        if NOISE ==0:
          v = -cost + (GAMMA * Values[x,y,d])
        if v > new_V:
          new_V = v
          policy[s] = a

      Values[s] = new_V

        
        # print(s_prime)
  printer(iteration,states,Values, policy)

  iteration = iteration + 1
  


