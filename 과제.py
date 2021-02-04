# name = "터틀봇 A"
# linear velocity = 0
# angular velocity = 0

# for calculation in range(1,4):

#1) __init__ 함수 (객체 선언시 name, linear velocity, angular velocity을 입력으로 받음)

class robot :
    def __init__(self, name, linear_velocity, angular_velocity) :
    self.name = name
    self.linear_velocity = linear_velocity
    self.angular_velocity = angular_velocity

    turtle = robot ("터틀봇A" , 0, 0)

#2) 자신의 현재상태 (name, linear velocity, angular velocity) 를 출력하는 함수

def now():
print ("이름 : {0} \tlinear velocity 값 : {1} \tangular velocity : {2}".format(self.name, self.linear_velocity, self.angular_velocity))

#3) linear velocity 를 랜덤으로 0.1씩 증가시키거나 감소시키는 함수

def no():
  no =randint(0,2)
if no == 0: 
    self.linear_velocity -= 0.1 
elif no ==1:
    self.linear_velocity += 0.1 

#4) angular velocity 를 랜덤으로 0.1씩 증가시키거나 감소시키는 함수
def nom():
  nom =randint(0,2)
if nom == 0: 
    self.angular_velocity -= 0.1 
elif nom ==1:
    self.angular_velocity += 0.1 

# 5) linear velocity와 angluar velocity가 0이 아닐경우 0으로 초기화 하는 함수가 존재한다

def reset():
if self.inear_velocity != 0 & self.angluar_velocity != 0
    linear_velocity = 0
    angular_velocity = 0

#===============================================================================
#1
turtle1 = robot ("터틀봇A" , 0, 0)
turtle2 = robot ("터틀봇B" , 0, 0)
turtle3 = robot ("터틀봇C" , 0, 0)
turtle4 = robot ("터틀봇D" , 0, 0)
turtle5 = robot ("터틀봇E" , 0, 0)

turtle = ['turtle1', 'turtle2', 'turtle3', 'turtle4', 'turtle5']  #turtle4는  turtle[3]임

#2
for calculation in range(1,6):
    turtle[0].no()  #터틀봇A의 no라는 함수를 실행하는 코드

#3
for calculation in range(1,4):
    turtle[2].nom()

#4

# turtle[0].reset()
# turtle[1].reset()
# turtle[2].reset()
# turtle[3].reset()
# turtle[4].reset()

for i in range(0,5) :
    turtle[i].reset()