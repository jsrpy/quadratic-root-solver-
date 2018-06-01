import cmath 
print("Welcome to My Quadratic Root Solver!")

def QuadraticRoort(a,b,c):
  d = b**2-4*a*c
  x1 = (-b+cmath.sqrt(d))/(2*a)
  x2 = (-b-cmath.sqrt(d))/(2*a)
  return d,x1,x2

def beautify (a,b,c):
  if a==0 and b!=0 and c!=0:
    s = "%sx + %s = 0" %(b,c)
  elif a!=0 and b==0 and c!=0:
    s = "%sx^2 + %s = 0" %(a,c)
  elif a!=0 and b!=0 and c==0:
    s = "%sx^2 + %sx = 0" %(a,b)
  elif a==0 and b==0 and c!=0:
    s = "%s = 0" %(c)
  elif a==0 and b!=0 and c==0:
    s = "%sx = 0" %(b)
  elif a!=0 and b==0 and c==0:
    s = "%sx^2 = 0" %(a)
  elif a==0 and b==0 and c==0:
    s = "0 = 0"
  elif a!=0 and b!=0 and c!=0:
    s = "%sx^2 + %sx + %s = 0" %(a,b,c)
  return s
  
  def QuadraticRootSolver(a,b,c):
  #d = b**2-4*a*c
  #data=(a,b,c) # use tuple not list!
  #x1 = (-b+cmath.sqrt(d))/(2*a)
  #x2 = (-b-cmath.sqrt(d))/(2*a)
  #equation = "%gx^2 + %gx + %g = 0"
  #equation = "%sx^2 + %sx + %s = 0"
  ss = beautify (a,b,c)
  print("The equation you enterted is \n", ss) 
  #print("The equation you enterted is", beautify() %data) #HOW?
  #print("%.2g" %x1) #How can I covert x to float? (Solved.)
  d,x1,x2 = QuadraticRoort(a,b,c)
  x11 = "{0.real:.2f}".format(x1)
  x22 = "{0.real:.2f}".format(x2) #%g is for exponent..
  #print(d)
  if d > 0:
    print("x =", x11, "or", x22)
  elif d == 0:
    print("x =", x11)
  elif d < 0:
    ai = "{0.imag:.2f}i".format(x1)
    bi = "{0.imag:.2f}i".format(x2)
    print("x =", x11, "+" ,ai, "or", x22, "+", bi)
  #print("x =", x11, "or", x22) 
  #ans = '({0.real:.2f}, {0.imag:.2f}i)'.format(x1,x2)
  #print(ans)
  #print("%s" %ans.split(","))
  #print("x =", x1, "or", x2)

QuadraticRootSolver(1,4,-21) #2 roots (x=3 or -7)
QuadraticRootSolver(12,-4,-5) #decimal (x=5/6 or -1/2) 
QuadraticRootSolver(3,12,12) #1 roots (x= -2)
QuadraticRootSolver(4,-12,9) #1 root (x= 1.5)
QuadraticRootSolver(5,2,1) #complex (x=-0.2+-0.4i)
QuadraticRootSolver(3,6,10) #complex (x= [-6+-sqrt(-84)] /6)
