#Eureka! - Archimedes and King Hiero's Crown - www.101computing.net/eureka-and-king-hieros-crown/

mass = float(input("Input the mass of the crown in kg"))
volume = float(input("Input the volume of the crown in cubic meter"))

#Complete the code here to calculate the density and compare it with the density of a range of differen metals
density = mass / volume
if density > 2400.0 and density < 2700.0:
  print('Aluminum')
elif density > 8100.0 and density < 8300.0:
  print('Bronze')
elif density > 10400.0 and density < 10600.0:
  print('Silver')
elif density > 11200.0 and density < 11400.0:
  print('Lead')
elif density > 17100.0 and density < 17500.0:
  print('Gold')
elif density > 21000.0 and density < 21500.0:
  print('Platinum')
else:
  print('Unknown Element')