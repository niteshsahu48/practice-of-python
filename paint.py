lenth=int(input("Enter Lenth:-"))
breadth=int(input("Enter Breadth:-"))
hight=int(input("Enter Hight:-"))
coast_of_1_ltr=int(input("Enter Coast,One Litre Paint:-"))
coverd_area=int(input("Enter Coverd Area Of Litre:-"))
area_of_room=(lenth*breadth)+(lenth*hight)*2+(breadth*hight)*2
paint_of_need=area_of_room/coverd_area
coast_of_paint=paint_of_need*coast_of_1_ltr
print(area_of_room,"sq area")
print(paint_of_need,"ltr")
print(coast_of_paint,"rs")


