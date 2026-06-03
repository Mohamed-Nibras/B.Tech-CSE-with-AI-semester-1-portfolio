#car game

help = ("""Start --> To start the car  
Stop --> To stop the car
Exit --> To exit the car""" )

while True :
   begin = input('Enter help to begin ')
   if begin.lower() == "help":
    print(help)
    break

   else :
    print('Enter help correctly')
    

command = ""
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if started :
            print('Car is already started ')

        else :
            started = True
            print('Car has started')
            
    elif command == "stop":
        if not started:
            print('Car is already stopped ')

        else :
            started = False
            print('Car has stopped ')

    elif command == 'quit':
        print('Game ends ')
        break

    else:
       print('I dont understand that command ')

       
      
