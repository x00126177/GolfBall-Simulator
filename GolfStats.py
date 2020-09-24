# IMPORTS
import math
# pip install matplotlib
import matplotlib.pyplot as plt

# INPUTS ---
print("Enter in format e.g. Driver, 8 Iron, PW etc.")
club = input("Club used: ")
while club!= "PW" and club != "9 Iron" and club != '8 Iron' and club != '7 Iron' and club != '6 Iron' and club != '5 Iron' and club != '4 Iron' and club != '3 Iron' and club != 'Driver':
    print("Club not supported")
    print("Enter in format e.g. Driver, 8 Iron, PW etc.")
    club = input("Club used: ")
pointX1 = float(input("Please enter X1: "))
pointY1 = float(input("Please enter Y1: "))
pointX2 = float(input("Please enter X2: "))
pointY2 = float(input("Please enter Y2: "))
time = float(input("Time between points: "))
launch_angle = float(input("Launch angle: "))
temperature = float(input("Temperature: "))

# PRESUMPTIONS ---
t = .001    # the increment of time, being used to create a number of heights at certain t's
ballRadius = .021335 #m
ballMass = .04593 #kg
g = 9.8   # GRAVITY

# LIFT AND DRAG COEFFICIENTS FOR CERTAIN CLUBS ---
if club == "Driver":
    Cd = .210
    Cl = .14
elif club == "3 Iron":
    Cd = .2235
    Cl = .155
elif club == "4 Iron":
    Cd = .228
    Cl = .14
elif club == "5 Iron":
    Cd = .2325
    Cl = .165
elif club == "6 Iron":
    Cd = .237
    Cl = .17
elif club == "7 Iron":
    Cd = .2415
    Cl = .175
elif club == "8 Iron":
    Cd = .246
    Cl = .18
elif club == "9 Iron":
    Cd = .2505
    Cl = .18
elif club == "PW":
    Cd = .255
    Cl = .19

# 9. DENSITY OF AIR DEPENDING ON TEMPERATURES ---
if temperature >=0 and temperature < 5:
    densityAir = 1.2922 # kg/m**3
elif temperature >=5 and temperature < 10:
    densityAir = 1.2690 # kg/m**3
elif temperature >=10 and temperature <15:
    densityAir = 1.2466 # kg/m**3
elif temperature >= 15 and temperature < 20:
    densityAir = 1.2250 # kg/m**3
elif temperature >= 20 and temperature < 25:
    densityAir = 1.2041 # kg/m**3
elif temperature >= 25 and temperature < 30:
    densityAir = 1.1839 # kg/m**3
elif temperature >= 30 and temperature < 35:
    densityAir = 1.1644 # kg/m**3
elif temperature >= 35 and temperature <= 40:
    densityAir = 1.1455 # kg/m**3

# FINDING THE LAUNCH ANGLE


# 1. DISTANCE FORMULA FOR POINTS ---
distance = math.sqrt(((pointX2-pointX1)**2.)+((pointY2-pointY1)**2.))

# 2. VELOCITY FOUND BETWEEN BOTH POINTS ---
ballSpeed = distance/time
ballSpeed_mph = ballSpeed*2.23694

# 10. CROSS SECTIONAL AREA
crossArea = math.pi * (ballRadius**2.)

# 13. LAUNCH ANGLE TO RADIANS
launch_angle_radians = (float(launch_angle)/180)*math.pi

# LIST CREATION AND CALCULATIONS ---
X=[]    # x dist
Y=[]    # y dist
Theta=[]    # angle
Theta.insert(0, launch_angle_radians)
Vx=[]
Vx.insert(0, ballSpeed * math.cos(launch_angle_radians))
Vy=[]
Vy.insert(0, ballSpeed * math.sin(launch_angle_radians))
Vel=[]
Vel.insert(0, math.sqrt(Vx[0] ** 2. + Vy[0] ** 2.))
aX=[]
aX.insert(0, 0)
aY=[]
aY.insert(0, 0)
xDist=[]
xDist.insert(0, 0)
yDist=[]
yDist.insert(0, 0)
aLift=[]
aLift.insert(0, 0)
aDrag=[]
aDrag.insert(0, 0)

# LOOP TO CALCULATE THE BALL IN FLIGHT FOR EVERY .001 OF A SECOND TO CALCULATE THE CHANGES IN FLIGHT OF THE BALL---
i=1
for i in range(1111111):
    # NEW ACCEL DRAG
    aDrag.insert(i, ((.5*densityAir*crossArea*Cd)/ballMass) * (Vel[i-1]**2.))
    # NEW ACCEL LIFT
    aLift.insert(i, ((.5*densityAir*crossArea*Cl)/ballMass) * (Vel[i-1]**2.))
    # NEW X ACCELERATION
    aX.insert(i, (aDrag[i]*(-math.cos(Theta[i])) + aLift[i]*(-math.sin(Theta[i-1]))))
    # NEW X VELOCITY
    Vx.insert(i, Vx[i-1] + aX[i]*t)
    # NEW X DISTANCE
    xDist.insert(i, xDist[i-1] + Vx[i]*t)
    # NEW X DISTANCE IN YARDS
    X.insert(i, xDist[i] * (1.09361))
    # NEW Y ACCEL
    aY.insert(i, -g + aDrag[i] * (-math.sin(Theta[i])) + aLift[i] * (math.cos(Theta[i-1])))
    # NEW Y VEL
    Vy.insert(i, Vy[i-1] + aY[i] * t)
    # NEW Y DISTANCE METERS
    yDist.insert(i, yDist[i-1] + Vy[i] * t)
    # NEW Y DIST IN YARDS
    Y.insert(i, yDist[i]*(1.09361))
    # NEW VELOCITY
    Vel.insert(i, math.sqrt(Vx[i] ** 2 + Vy[i] ** 2))
    # NEW THETA
    Theta.insert(i, math.atan(Vy[i] / Vx[i]))

    # BREAK FROM LOOP WHEN BALL HAS HIT GROUND
    if yDist[i] <= 0:
        maxDist_meters = xDist[i]
        break

# CHANGING DISTANCES TO YARDS ---
maxDist_yards = maxDist_meters*(1.09361)
maxDist_yards = int(maxDist_yards)
maxHeight_yards = int(max(Y))

# OUTPUTS ---
print("Statistics Feedback---")
print("Maximum height of ball: ", maxHeight_yards,"yards")
print("Maximum height of ball: ", int(max(yDist)),"meters")
print("Carry Distance: ", maxDist_yards,"yards")
print("Carry Distance: ", int(maxDist_meters),"meters")



# LAUNCH ANGLE FEEDBACK ---
print("Launch Angle Feedback---")
if club == "Driver":
    if launch_angle < 9:
        print("Optimal Launch: 9-11 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too LOW for a typical Driver")
        print("Tip: This can be achieved by placing the ball inline with the inside of your heel in your stance while striking up on the ball while its tee'd")
        print("(Left handed players: Inside of right heel. Right handed players: Inside of left heel")
    elif launch_angle > 11:
        print("Optimal Launch: 10-12 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too HIGH for a typical Driver")
        print("Tip: The ball may be too far in front of your stance")
        print("(Left handed players: Between your sternum and right heel. Right handed players: Between your sternum and left heel")
    else:
        print("You are launching the ball with a driver at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 10-12 degrees")
elif club == "3 Iron":
    if launch_angle < 8:
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 8-10 degrees")
        print("This Launch is too low for a typical 3 Iron")
        print("Tip: This can be achieved by placing the ball an inch forward in your stance while having the club face connect with the ball ahead of your hands")
        print("(Left handed players: An inch to the right. Right handed players: An inch to the left")
    elif launch_angle > 10:
        print("Optimal Launch: 10-12 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 3 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is an inch in front of your stance")
        print("(Left handed players: An inch to the right. Right handed players: An inch to the left")
        print("Tip: You could be striking the ball with the club too far ahead of your hands. This creates added launch")
    else:
        print("You are launching the ball with a 3 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 10-12 degrees")
elif club == "4 Iron":
    if launch_angle < 10:
        print("Optimal Launch: 10-12 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 4 Iron")
        print("Tip: This can be achieved by placing the ball an inch forward in your stance while having the club face connect with the ball ahead of your hands")
        print("(Left handed players: An inch to the right. Right handed players: An inch to the left")
    elif launch_angle > 12:
        print("Optimal Launch: 10-12 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 4 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is an inch in front of your stance")
        print("(Left handed players: An inch to the right. Right handed players: An inch to the left")
        print("Tip: You could be striking the ball with the club too far ahead of your hands. This creates added launch")
    else:
        print("You are launching the ball with a 4 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 10-12 degrees")
elif club == "5 Iron":
    if launch_angle < 11:
        print("Optimal Launch: 11-13 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 5 Iron")
        print("Tip: This can be achieved by placing the ball a half inch forward in your stance while having the club face connect with the ball ahead of your hands")
        print("(Left handed players: A half inch to the right. Right handed players: A half inch to the left")
    elif launch_angle > 13:
        print("Optimal Launch: 11-13 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 5 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is a half inch in front of your stance")
        print("(Left handed players: A half inch to the right. Right handed players: A half inch to the left")
        print("Tip: You could be striking the ball with the club too far ahead of your hands. This creates added launch")
    else:
        print("You are launching the ball with a 5 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 11-13 degrees")
elif club == "6 Iron":
    if launch_angle < 13:
        print("Optimal Launch: 13-15 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 6 Iron")
        print("Tip: This can be achieved by placing the ball in the center of your stance while having the club face connect with the ball in-line with your hands")
    elif launch_angle > 15:
        print("Optimal Launch: 13-15 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 6 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is at the center of your sternum")
        print("Tip: You could be striking the ball with the club face too far ahead of your hands. This creates added launch")
        print("Tip: Ensure that your hands are inline with the club head on impact")
    else:
        print("You are launching the ball with a 6 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 13-15 degrees")
elif club == "7 Iron":
    if launch_angle < 15:
        print("Optimal Launch: 15-17 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 7 Iron")
        print("Tip: This can be achieved by placing the ball in the center of your stance while having the club face connect with the ball in-line with your hands")
    elif launch_angle > 17:
        print("Optimal Launch: 15-17 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 7 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is at the center of your sternum")
        print("Tip: You could be striking the ball with the club face too far ahead of your hands. This creates added launch")
        print("Tip: Ensure that your hands are inline with the club head on impact")
    else:
        print("You are launching the ball with a 7 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 15-17 degrees")
elif club == "8 Iron":
    if launch_angle < 17:
        print("Optimal Launch: 17-19 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 8 Iron")
        print("Tip: This can be achieved by placing the ball in the center of your stance while having the club face connect with the ball in-line with your hands")
    elif launch_angle > 19:
        print("Optimal Launch: 17-19 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 8 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is at the center of your sternum")
        print("Tip: You could be striking the ball with the club face too far ahead of your hands. This creates added launch")
        print("Tip: Ensure that your hands are inline with the club head on impact")
    else:
        print("You are launching the ball with an 8 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 17-19 degrees")
elif club == "9 Iron":
    if launch_angle < 19:
        print("Optimal Launch: 19-21 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical 9 Iron")
        print("Tip: This can be achieved by placing the ball in the center of your stance while having the club face connect with the ball in-line with your hands")
    elif launch_angle > 21:
        print("Optimal Launch: 19-21 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 9 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is at the center of your sternum")
        print("Tip: You could be striking the ball with the club face too far ahead of your hands. This creates added launch")
        print("Tip: Ensure that your hands are either leading the club head by the smallest amount or is inline with the club head on impact")
    else:
        print("You are launching the ball with a 9 iron at the same launch angle as the PGA Tour Average")
        print("Users:", launch_angle, "degrees")
        print("Optimal Launch: 19-21 degrees")
elif club == "PW":
    if launch_angle < 23:
        print("Optimal Launch: 23-25 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too low for a typical PW")
        print("Tip: This can be achieved by placing the ball in the center of your stance while having the club face connect with the ball in-line with your hands")
    elif launch_angle > 25:
        print("Optimal Launch: 23-25 degrees")
        print("Users:", launch_angle, "degrees")
        print("This Launch is too high for a typical 9 Iron")
        print("Tip: The ball may be too far in front of your stance, ensure that the ball is at the center of your sternum")
        print("Tip: You could be striking the ball with the club face too far ahead of your hands. This creates added launch")
        print("Tip: Ensure that your hands are either leading the club head by the smallest amount or is inline with the club head on impact")
    else:
        print("You are launching the ball with a PW at the same launch angle as the PGA Tour Average")
        print("Optimal Launch: 23-25 degrees")
        print("Users:", launch_angle, "degrees")
else:
    print("Club not supported")

# BALL SPEED FEEDBACK ---
print("Ball Speed Feedback---")
if club == "Driver":
    if ballSpeed_mph >= 162 and ballSpeed_mph <= 172:
        print("Optimal Ball Speed: 167.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 2400rpm and 3000rpm when your Drivers launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a Driver")
    elif ballSpeed_mph < 162:
        print("Optimal Ball Speed: 167.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a Driver")
    else:
        print("Optimal Ball Speed: 167.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "3 Iron":
    if ballSpeed_mph >= 137 and ballSpeed_mph <= 147:
        print("Optimal Ball Speed: 142.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 4300rpm and 4900rpm when your 3 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 3 Iron")
    elif ballSpeed_mph < 115:
        print("Optimal Ball Speed: 142.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 3 Iron")
    else:
        print("Optimal Ball Speed: 142.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "4 Iron":
    if ballSpeed_mph >= 132 and ballSpeed_mph <= 142:
        print("Optimal Ball Speed: 137.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 4500rpm and 5100rpm when your 4 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 4 Iron")
    elif ballSpeed_mph < 132:
        print("Optimal Ball Speed: 137.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 4 Iron")
    else:
        print("Optimal Ball Speed: 137.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "5 Iron":
    if ballSpeed_mph >= 127 and ballSpeed_mph <= 137:
        print("Optimal Ball Speed: 132.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 5000rpm and 5600rpm when your 5 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 5 Iron")
    elif ballSpeed_mph < 127:
        print("Optimal Ball Speed: 132.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 5 Iron")
    else:
        print("Optimal Ball Speed: 132.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "6 Iron":
    if ballSpeed_mph >= 122 and ballSpeed_mph <= 132:
        print("Optimal Ball Speed: 127.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 5900rpm and 6500rpm when your 6 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 6 Iron")
    elif ballSpeed_mph < 122:
        print("Optimal Ball Speed: 127.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 6 Iron")
    else:
        print("Optimal Ball Speed: 127.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "7 Iron":
    if ballSpeed_mph >= 115 and ballSpeed_mph <= 125:
        print("Optimal Ball Speed: 120.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 6800rpm and 7400rpm when your 7 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 7 Iron")
    elif ballSpeed_mph < 115:
        print("Optimal Ball Speed: 120.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 7 Iron")
    else:
        print("Optimal Ball Speed: 120.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "8 Iron":
    if ballSpeed_mph >= 110.0 and ballSpeed_mph <= 120.0:
        print("Optimal Ball Speed: 115.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 7700rpm and 8300rpm when your 8 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using an 8 Iron")
    elif ballSpeed_mph < 110:
        print("Optimal Ball Speed: 115.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with an 8 Iron")
    else:
        print("Optimal Ball Speed: 115.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "9 Iron":
    if ballSpeed_mph >= 104 and ballSpeed_mph <= 114:
        print("Optimal Ball Speed: 109.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 8300rpm and 8900rpm when your 9 Irons launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a 9 Iron")
    elif ballSpeed_mph < 104:
        print("Optimal Ball Speed: 109.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This ball speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a 9 Iron")
    else:
        print("Optimal Ball Speed: 109.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
elif club == "PW":
    if ballSpeed_mph >= 97 and ballSpeed_mph <= 107:
        print("Optimal Ball Speed: 102.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("You are generating between 9000rpm and 9600rpm when your PW's launch angle is in its optimised condition")
        print("This is the optimal solution for distance and spin control when using a PW")
    elif ballSpeed_mph < 104:
        print("Optimal Ball Speed: 102.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This ball speed is slower than the PGA Tour Average and is limiting the spin and distance you could achieve with a PW")
    else:
        print("Optimal Ball Speed: 102.0 MPH")
        print("Users: ", ballSpeed_mph, "MPH")
        print("This swing speed is faster than the tour average however it may be increasing the spin thus afftecting the distance and control of your shot")
else:
    print("Club not supported")

# PLOTTING BALL FLIGHT ---
plt.plot(X[1:111111], Y[1:111111])
plt.plot()
plt.xlabel('Carry Distance (Yards)')
plt.ylabel('Height (Yards)')
plt.show()