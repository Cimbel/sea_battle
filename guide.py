from colors import Colors
from time import sleep
import colorama

# need for see color in console
colorama.init()


def guide():
    print(f"""
    
    
    
<- ========================================== ->
   <- =================== GUIDE ================ ->
      <- ========================================== ->
      |     
      |
      |                                                                                   
      |  ------------------------------------- {Colors.CYAN}General information{Colors.END} --------------------
      |      
      |
      |                                                                         
      |  Welcome to the guide, fighter.
      |                      
      |  The instructions will help you much better understand the next things:
      |      1. How many errors game has, their meaning etc.
      |      2. How to play in game, what to do, and what do in case of error or rare case.
      |      3. Meaning about what each different char represents on the play field.                                        
      |      ...  
      |                                                                                
      |  Let's start from the chars which will appear in the game.                             
      |                                                                                        
      |  {Colors.GREEN}@{Colors.END} -- marks available positions for set up ships and shooting                         
      |  {Colors.RED}#{Colors.END} -- marks for ships                                                                  
      |  {Colors.RED}-{Colors.END} -- marks for position, you can't choose for shooting or for set upping ships on     
      |  {Colors.RED}X{Colors.END} -- marks for dead deck
      |
      |
      |  When you type 'start' it will ask you which type of set upping ships do you wanna choose.                      
      |      1. Manually -- you have to set up all ships by your own 
      |      2. Random   -- system will randomly set up all ships instead of you
      |
      |
      |  There are must be 10 ships to start playing.
      | 
      |     one deck ship   - 4
      |     two deck ship   - 3
      |     three deck ship - 2
      |     four deck ship  - 1
      |
      |
      |
      |  ------------------------------------- {Colors.CYAN}Set upping ships randomly{Colors.END} --------------------
      |
      |
      |
      |  When you chose the "randomly" type of set upping ships, it will show a play field which system
      |  generated for you, then asks does it okay for you or not. Type yes if it's okay, and then battle
      |  starts. If you indicate no, then it will recreate field and ask again, you can choose another
      |  type of set upping ships, just follow messages.
      |
      |
      |
      |  ------------------------------------- {Colors.CYAN}Set upping ships manually{Colors.END} -------------------- 
      |
      |
      |
      |     After you chose the "manually" type of set upping ships, it will ask you first about "one-deck ships",
      |     then about "two-deck ships", "three-deck ships", and finally "four-deck ship". The order of set upping
      |     ships in another way you won't be able to change.
      |
      |     If you want change type of set upping ships from the manually to the random, indicate "menu",
      |     follow messages, and then start again a battle.
      |
      |     All ships must be close to each other except one deck ship. 
      |     The example of the right placed ships represented below.
      |
      |
      |            A  B  C  D  E  F  G  H  I  J 
      |         1  {Colors.RED}-  -  -  -  {Colors.GREEN}@  @  @  @  @  @{Colors.END} 
      |         2  {Colors.RED}-  #  #  -  -  -  -  -  -  -{Colors.END} 
      |         3  {Colors.RED}-  -  -  -  -  #  #  -  #  -{Colors.END}
      |         4  {Colors.GREEN}@  @  {Colors.RED}-  -  -  -  -  -  -  -{Colors.END} 
      |         5  {Colors.RED}-  -  -  #  -  -  -  -  #  -{Colors.END}
      |         6  {Colors.RED}-  #  -  -  -  -  #  -  -  -{Colors.END} 
      |         7  {Colors.RED}-  -  -  -  -  -  #  -  #  -{Colors.END} 
      |         8  {Colors.RED}#  -  {Colors.GREEN}@  {Colors.RED}-  #  -  #  -  #  - {Colors.END}
      |         9  {Colors.RED}#  -  {Colors.GREEN}@  {Colors.RED}-  #  -  #  -  #  - {Colors.END}
      |         10 {Colors.RED}#  -  {Colors.GREEN}@  {Colors.RED}-  -  -  -  -  -  - {Colors.END}
      |
      |
      |  1. One-deck ship
      |     
      |     You have to specify one available position on play field wih {Colors.GREEN}"@"{Colors.END} char.
      |     The 'template' for doing that is the next "a1", "1j", "J9", and "6H".
      |
      |  2. Two-deck ship
      |
      |     The template if following "h1:h2", "1h:2h", "J3:4g" ...
      |     Specify between position ":", if you won't specify it, or specify another separator,
      |     it will print out you an error.
      |
      |  3. Three-deck ship
      |
      |     The template is following "h1:h2:h3", "1h:2h:3h, "1a:2a:3a" ...
      |     The separator between positions is the same as with two-deck ships and with four-deck ships -- ":"
      |
      |  4. Four-deck ship
      |
      |     The template is the next -- "3a:4a:5a:6a", "1h:2h:3h:h4" ...
      |     The separator the same as with two deck ship and three deck ship -- ":"
      |
      |  {Colors.RED}!NOTE!{Colors.END} -- You are not able to change the separator ":"
      |
      |
      |
      |  ------------------------------------- {Colors.CYAN}Battle{Colors.END} -------------------- 
      |
      |
      |
      |  In the battle there is no any specific moments to discuss. You have two field, the first one -
      |  where your ships are placed, and the second one shooting field - where you shoot. If you hit
      |  the target, then you keep going shooting until you miss, then computer shoot in the same
      |  way as you, if it shot, then keep going, if missed then your turn. You just have to specify
      |  shoot's position on field where is {Colors.GREEN}"@"{Colors.END} char. When you hit the target, on your field
      |  will appear {Colors.RED}"X"{Colors.END} char, if you missed, then will appear {Colors.RED}"-"{Colors.END} char, 
      |  and you won't be able to shoot in this position anymore. When you killed ship, then will appear around ship
      |  {Colors.RED}"-"{Colors.END} chars. When computer or you kill 10 ships game is over, and will
      |  print out a message who is win, you or computer.
      |  
      |
      |
      |  ------------------------------------- {Colors.RED}Errors meaning{Colors.END} -------------------- 
      |                     
      |            
      |                                      
      |  1. {Colors.RED}[Error]: Not existing position{Colors.END}
      |         
      |     You trying to set up ships or choose position for shooting which
      |     not exists on play field. You have to choose position which is
      |     exists on play field.
      |
      |  2. {Colors.RED}[Error]: Unknown command!{Colors.END}
      |
      |     You type command which not exists in the game, type "help"
      |     to see all available command in the game.
      |
      |  3. {Colors.RED}[Error]: Unknown answer!{Colors.END}
      |
      |     You specified not right answer which given for you to choose.
      |     Specify instead the right answer from the given message. 
      |
      |  4. {Colors.RED}[Error]: Duplication positions{Colors.END}
      |
      |     You trying set up two or more deck on the same position.
      |     Avoid such case and watch out in next time.
      |
      |  5. {Colors.RED}[Error]: One of the position you've tried to set up is busy!{Colors.END}
      |
      |     You tying set up position which in the moment busy.
      |     Specify position only with {Colors.GREEN}"@"{Colors.END} char
      |
      |  6. {Colors.RED}[Error]: The pos you trying attack has already shot!{Colors.END}
      |     
      |     You trying to shoot a position which has already shot. 
      |     Try shoot position wih {Colors.GREEN}"@"{Colors.END} char
      |
      |
      |
      |  ------------------------------------- {Colors.CYAN}Rare cases{Colors.END} -------------------- 
      |
      |
      |
      |  1. There is could be a case, when you end up set up your ships on play field as below.
      |
      |        A  B  C  D  E  F  G  H  I  J 
      |     1  {Colors.RED}-  -  -  -  -  -  -  -  -  {Colors.GREEN}@{Colors.END} 
      |     2  {Colors.RED}-  #  -  -  #  -  -  #  -  {Colors.GREEN}@{Colors.END}
      |     3  {Colors.RED}-  -  -  -  -  -  -  -  -  - {Colors.END}
      |     4  {Colors.RED}-  -  -  -  -  -  -  -  #  - {Colors.END}
      |     5  {Colors.RED}-  #  -  -  #  #  -  -  #  - {Colors.END}
      |     6  {Colors.RED}-  -  -  -  -  -  -  -  #  - {Colors.END}
      |     7  {Colors.RED}-  -  -  -  -  -  -  -  -  - {Colors.END}
      |     8  {Colors.RED}-  #  #  -  -  #  -  {Colors.GREEN}@  @  @ {Colors.END}
      |     9  {Colors.RED}-  -  -  -  -  #  -  {Colors.GREEN}@  @  @ {Colors.END}
      |     10 {Colors.RED}-  #  #  #  -  -  -  {Colors.GREEN}@  @  @ {Colors.END}
      |
      |     And you need to set up somewhere 'four-deck ship', but as you saw, the field doesn't
      |     have any available space for 'four-deck ship'. Then you have to type "reset" and follow
      |     an instructions. This will delete all your deck which you set upped before, and you will be doing
      |     all set upping ships one more time, but in the next time, avoid such case to happen.
      |
      |  2. If you are waiting more then 10-15 seconds for getting answer from the system, 
      |     then type 'Enter' a few times and this must helps.
      |
      |  3. If you noticed that you specified the right position but you still getting an error,
      |     then just try one more time specify the same position, if that not gonna help, then 
      |     try to change order of positions, for instance, "10f:10e:10d" --> "f10:f10:f10" or
      |     "h1:h2:h3:h4" --> "h2:h1:3h:4h" etc.
      |
      |
      |
      <- ========================================== ->
   <- =================== GUIDE ================ ->
<- ========================================== ->



    """)
    sleep(7)
