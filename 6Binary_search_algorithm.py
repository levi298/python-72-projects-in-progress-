# sortedlist = [1,2,5,6,7,9,10,11,16,19,20]
# selected=int(input("give me give me : "))
# middle=(len(sortedlist))
# left=0
# right=0
# middle=middle//2
# print(middle)

# if sortedlist[middle]==selected:
#     print("found it it was in number:",sortedlist[middle])
# elif selected > sortedlist[middle]:
#     print("serching right ")
#     right=((sortedlist[middle+1::]))
#     print(right)
#     middle2 = (len(right))
#     middle2 = middle2//2
#     print(middle2)
#     if right[middle2]==selected:
#         print("yoo u found it was :",right[middle2])
#     elif selected > right[middle2]:
#         print("searching right")
#         left2=right2=((right[middle2+1::]))
#         print(right2)
#         middle3=(len(right2))
#         middle3= middle3//2
#     elif selected < left2[middle2]:
#         print("serching left ---")
#         left=((right[:middle:]))
#         print(left)
#         middle2 = (len(left))
#         middle2 = middle2//2
#         print(middle2)
#     elif left[middle2] == selected:
#         print("yoo u found it was :",left[middle2])
#     if right2[middle3]==selected:
#             print("yes finally u found it ",right2[middle3])
#     elif right2[middle3]<selected:
#             print("searching right ")
#             right3=((right2[middle3+1::]))
#             print(right3)
#             middle4 = (len(right3))
#             middle4 = middle4//2
#     elif selected <= right2[middle]:
#             print("serching left ---")
#             left=((sortedlist[:middle:]))
#             print(left)
#             middle2 = (len(left))
#             middle2 = middle2//2
#             print(middle2)
#     elif left[middle2] == selected:
#                 print("yoo u found it was :",left[middle2])
#     if right3[middle4]==selected:
#                 print("yoo nice u find it finally meow")
#     else:
#                 print("list finished")
# elif selected <= sortedlist[middle]:
#     print("serching left ---")
#     left=((sortedlist[:middle:]))
#     print(left)
#     middle2 = (len(left))
#     middle2 = middle2//2
#     print(middle2)
#     if left[middle2] == selected:
#         print("yoo u found it was :",left[middle2])
#     elif selected < left[middle2]:
#         print("searching left")
#         left2=((left[:middle2:]))
#         print(left2)
#         middle3=(len(left2))
#         middle3= middle3//2
#         if left2[middle3]==selected:
#             print("yes finally u found it ",left2[middle3])
#         elif left2[middle3] > selected:
#             print("searching left ")
#             left3=((left2[:middle3:]))
#             print(left3)
#             middle4 = (len(left3))
#             print(middle,middle2,middle3,middle4)
#             middle4 = middle4//2
#             if left3[middle4]==selected:
#                 print("yoo nice u find it finally meow")
#             else:
#                 print("list finished")




#----------------------------------------------------------------------------------------#
#second attempt#
# sortedlist=[1,3,5,6,7,9,10,15,16,19,20] 
# select=int(input("give me give me : "))

# middle=len(sortedlist)

# middle=middle//2
# # now we have middle value 

# found= False
# if not found:
#     if select == sortedlist[middle]:                          # sorted list (1)
#             print("GOOD U FOUND IT :",sortedlist[middle])
#             found=True

#     elif select > sortedlist[middle]:                         # sortedlist (2)
#         print("serching right")
#         list=sortedlist[middle+1::]
#         middle2=len(list)
#         middle3=middle2//2
#         found= False

#         if not found:
#             if select == list[middle3]:                                # list (1)
#                 print("GOOD U FOUND IT :",list[middle3])
#                 found = True
#             elif select > list[middle3]:                               # list  (2)
#                 print("SERCHING RIGHT")
#                 list2=list[middle3+1::]
#                 middle3=len(list2)
#                 middle4=middle3//2

        

#             elif select < list[middle3]:                             # list (3)
#                 print("SERCHING LEFT")
#                 list2=list[:middle3:]                       # new list formed list 2
#                 middle3=len(list2)
#                 middle4=middle3//2
#                 found= False
#                 if not found:
            
#                     if select == list2[middle4]:                      # list2 (1)
#                         print("GOOD U FOUND IT :",list2[middle4])
#                         found=True

#                     elif select > list2[middle4]:                         # list2 (2)
#                         print("serching right")
#                         list3=list2[middle4+1::]                       # new list formed list 3
#                         middle4=len(list3)
#                         middle5=middle4//2
            
#                     elif select < list2[middle4]:                         # list2 (3)
#                         print("serching left")
#                         list3=list2[:middle4:]                       
#                         middle4=len(list3)
#                         middle5=middle4//2
                        
                        
#                 if not found:
                   
#                     if select == list3[middle5]:                      # list3 (1)
#                                 print("GOOD U FOUND IT :",list3[middle5])
#                                 found = True
                                   
#                     elif select > list3[middle5]:                         # list3 (2)
#                                 print("serching right")
#                                 list4=list3[middle5+1::]                       # new list formed list 4
#                                 middle6=len(list4)
#                                 middle7=middle6//2
#                                 found= False
#                                 if list4[middle7]==select:
#                                      print("ur selected vule : ",list4[middle7])
#                                      found=True
#                                 else:
#                                     print("list finished")
            
#                     elif select < list3[middle5]:                         # list3 (3)
#                                     print("serching left")
#                                     list4=list3[:middle5:]                       
#                                     middle6=len(list4)
#                                     middle7=middle6//2
#                                     found= False
#                                     if list4[middle7]==select:
#                                         print("ur selected vule : ",list4[middle7])
#                                         found=True
#                                     else:
#                                         print("list finished")


#     elif select < sortedlist[middle]:                         # sortedlist (3)
#         print("serching left")
#         list=sortedlist[:middle:]
#         middle2=len(list)
#         middle3=middle2//2
#         found= False
        
#         if not found:


#             if select == list[middle3]:
#                 print("GOOD U FOUND IT :",list[middle3])
#                 found =True
#             elif select > list[middle3]:
#                 print("SERCHING RIGHT")
#                 list2=list[middle3+1::]
#                 middle4=len(list2)
#                 middle5=middle4//2

#             elif select < list[middle3]:                             # list (3)
#                 print("SERCHING LEFT")
#                 list2=list[:middle3:]                       # new list formed list 2
#                 middle4=len(list2)
#                 middle5=middle4//2
#                 found= False
#                 if not found:
            
               


#                             if select == list2[middle5]:                      # list2 (1)
#                                 print("GOOD U FOUND IT :",list2[middle5])
#                                 found=True
#                             elif select > list2[middle5]:                         # list2 (2)
#                                 print("serching right")
#                                 list3=list2[middle5+1::]                       # new list formed list 3
#                                 middle6=len(list3)
#                                 middle7=middle6//2
            
#                             elif select < list2[middle5]:                         # list2 (3)
#                                 print("serching left")
#                                 list3=list2[:middle5:]                       
#                                 middle6=len(list3)
#                                 middle7=middle6//2
#                                 found=False
                       
                
#                 if not found:
                   
#                             if  select == list3[middle7]:                      # list3 (1)
#                                         print("GOOD U FOUND IT :",list3[middle7])
#                                         found = True

#                             elif select > list3[middle7]:                         # list3 (2)
#                                         print("serching right")
#                                         list4=list3[middle7+1::]                       # new list formed list 4
#                                         middle7=len(list4)
#                                         middle8=middle7//2
#                                         found= False
#                                         if list4[middle8]==select:
#                                             print("ur selected vule : ",list4[middle8])
#                                             found=True
#                                         else:
#                                             print("list finished")
            
#                             elif select < list3[middle7]:                         # list3 (3)
#                                         print("serching left")
#                                         list4=list3[:middle7:]                       
#                                         middle7=len(list4)
#                                         middle8=middle7//2
#                                         found= False
#                                         if list4[middle8]==select:
#                                             print("ur selected vule : ",list4[middle8])
#                                             found=True
#                                         else:
#                                             print("list finished")    
                    


# ################################################################################################## #

# third attepmpt /  with while loop i know we can do that from start but i was just building things so 

sortedlist=[1,3,6,7,8,9,10,15,16,19,20]

select=int(input("gimme gimee give: "))
middle=len(sortedlist)
current=sortedlist
while True:
        middle=middle//2
        
        if len(current) == 0:
            print("list finished")
            break
        if select == current[middle]:
            print("goood boy u gound it : ",current[middle])
            break
        elif select > current[middle]:
            print("SEARCHING RIGHT")
            current=current[middle+1:]
            middle=len(current)
           
        
        elif select < current[middle]:
            print("SEARCHING LEFT")
            current=current[:middle]
            middle=len(current)
        
            
    
          