# Variables 
swimming_time = float(input("Enter the swimming time"))
cycling_time = float(input("Enter the cycling time"))
running_time = float(input("Enter the running time"))
total_triatholon_time = swimming_time + cycling_time + running_time
#Award allocation
if total_triatholon_time <= 100 :
    print( "Award provincial colours")
elif total_triatholon_time >100 or total_triatholon_time <=105 :
    print("Award provincial half colours")
elif total_triatholon_time >= 106 or total_triatholon_time <=110:
    print(" Award provincial scroll")
else:
    print( "No award")



    