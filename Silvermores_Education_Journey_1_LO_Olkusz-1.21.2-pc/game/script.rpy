# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.








#Komentarz o procesie myślowym przy tworzeniu gry. Polecam dokładnie przeczytać gdyż zawiera pełno informacji dotyczących naszego procesu projektowania gry.




#Ciekawostki z programistą projektu!

# Na początku duża część naszej pracy została wzięta z źródeł do których nie mieliśmy praw autorskich! Dlatego tydzień przed terminem oddania prac musieliśmy stworzyć nasze własne tła do wszystkich lokacjii
# Dzięki ciężkiej pracy naszego grafika (Projektowaniu / rysowaniu modeli postaci i teł) i mnie (przy obróbce kolorystycznej powyższych), 
# mamy pełne prawa do wszystkich rzeczy znajdujących się w grze :)
# Był to ciężki tydzień, lecz było warto




#Role w drużynie:

 #Modele postaci zostały narysowane pięknie przez Tosię, Mateusz zajmował się pomysłami i przebiegiem gry, ja (Piotr) zajmowałem się całym programowaniem, muzyką, doborem kolorystyki postaci, oceną pomysłów,
 #doborem efektów dźwiękowych i przede wszystkim utrzymywaniem całego projektu w ryzach żebyśmy nie wpadli w development hell. Jagoda jest osobą odpowiedzialną za piękny opis gry, backstory postaci, i 
 #jest jedyną osobą z nas która umię ładnie gramatycznie pisać lol.

 #Pani Sandra (Nasz wychowawca i nadzorujący projekt) była dla nas dużym wsparciem, jeśli mieliśmy do czegoś wątpliwości zawsze była dla nas dostępna. Mogliśmy pisać nawet o 20 (w szczególności w sprawach związanych
 #z copyrightem) a Pani pomimo późnej godziny, i tak odpisywała na czas.




#Dlaczego wybraliśmy Visual Novel i Ren'py ponad grę akcji i unity?

# Moim pierwszym planem było zabranie mojego doświadczenia w tworzeniu gier i skryptów z C# i zrobienie doskonałej gry w unity, lecz zauważyliśmy że w pierwszej oraz drugiej edycji konkursu 
# pierwsze miejsca zajmowały już gry platformowa napisane (prawdopodobnie) w C# przy użyciu silnika Unity. Gry te były zapewne bazowane na Templacie platformówki z Unity.
# Unity ma wiele plusów lecz uznałem że jeżeli mamy tylko 2 miesiące na dostarczenie ciekawej, oryginalnej i wciągającej gry edukacyjnej, to musimy zrobić coś co nie zostało jeszcze zrobione w poprzednich
# edycjach konkursu GEEK, coś całkowicie nowego, świeżego.
# W poprzednich edycjach nie zauważyłem żadnej gry napisanej jako Visual Novela. Jest to dość niszowy typ gier komputerowych z bardzo lojajną społecznością. Gry te są zazwyczaj wciągającymi hisoriami
 #miłosnymi z wieloma postaciami, produkowanymi przez lata. Dlatego, podjeliśmy się tego ciężkiego zadania jakim jest stworzenie Pełnej Visual Noveli z wieloma zakończeniami i wątkami. 
 


#Kilka ostatnich słów, zanim wrócę do naprawiania błędów w kodzie.
 #Mam nadzieję, że gra Państwu się spodoba, głównym założeniem było nie rzucanie literaturą czy algebrą w twarz gracza,
 #ale sprawienie, by sam CHCIAŁ grać w tę grę.
 #Gdybym miał wybierać między grą, w której muszę się nauczyć czegoś, czego nie lubię w żmudny powtarzalny sposób, nie grałbym w nią (a gdybym musiał, prawdopodobnie napisałbym do niej cheaty lub coś w tym stylu). 
 #Po rozegraniu naszej gry ponad 100 razy szukając bugów i glitchy, mogę stwierdzić że jest dość dobra. Sam ocenił bym ją bliżej gier jak Doki Doki litterature club (bardzo popularna Visual Novela) niż do jakiś
 #innych niszowych gier napisanych w tydzień. Włożyliśmy w tą grę całe nasze serca, pracowaliśmy w każdym wolnym momęcie często lekko zaniedbując nasze inne pasje, godząc proces tworzenia gry z nauką.
 #Dlatego mamy nadzieję że gra się spodoba :)


#Myślę że cały kod jest czytelny i ładnie zkomentowany
#Miłej gry i sprawdzania kodu!  :) 

# - Piotr (Główny i jedyny programista)






# Characters
define g = Character('Max', color="#0086FC")
define n = Character('Sarah', color="#B20FDE")
define a = Character('Lily', color="#FE3EE1")
define d = Character('Rick')
define t = Character('Jason')
define s = Character('Mrs. Thompson', color="#a6a092")
define l = Character('Lessie', color="#4e92bf")
define b = Character('Headmaster Roberts', color="#804221")
define sm = Character('Mr. Ai')
define c = Character('Mr. Froga')
define bob = Character('Robbert', color="#00B99D")

# Narration characters
# for the tr (translator) character i've used a trick using the history system built into renpy. It saves every dialogue so i've just renamed history to translations and after each and every normal line i make
# the translator say it in a -100 font with a 99999 speed lol.

define tr = Character('<-------->', color="#3D3D3D", what_size=0.1)
define nr = Character('Narrator', color="#838383")


# Sprites ( characters and backgrounds)
# Imiona postaci zostały zmienione przed stworzeniem finalnej wrsji

image Roberts = "Roberts.png"
image Jason = "Jason_Happy.png"
image thompson = "Miss_thompson.png"
image thompson_right = "Miss_thompson_right.png"
image Lesie = "Lesie_disgusted.png"
image Froga = "Froga.png"
image Ai = "Ai.png"
image Lily = "Lily.png"
image Lily_night = "Lily_night.png"
image max_night = "max_happy_night.png"
image Lily_right = "Lily_right.png"
image Robbert_closeup = "Robbert_closeup.png"
image Robbert_far = "Robbert_far.png"
image Lily_Experiment_On_max = "Lily_Experiment_On_max.png"


#max house
image Bedroom_max = "Bedroom_max.jpg"
image Bedroom_max_Night = "Bedroom_max_night.jpg"
image salon = "Salon_max.png"
image max_computer = "max_computer.jpg"
image House_kitchen = "House_Kitchen.jpg"
image max_porch = "max_house.jpg"
image House_Backyard = "House_Backyard.jpg"
image House_Backyard_3 = "House_Backyard_3.jpg"
image max_Joy = "max_happy.png"
image Sarah_Joy = "Sarah_Happy.png"
image max_tv = "max_tv.png"
image bad_ending_screen = "Bad_ending_screen.jpg"
image neutral_ending = "Desert.jpg"



#school
image school_entrance = "school_entrance.png"
image school_staircase = "School_staircase.jpg"
image school_room1 ="school_room1.jpg" 
image school_classroom_hall = "Hallway_classroom_door.jpg"
image school_cafeteria = "Cafeteria.jpg"
image ArrowUp = "ArrowUp.png"
image school_classroom = "school_classroom.jpg"
image School_Roberts_office = "School_Roberts_office.jpg"
image School_Ai_office = "School_Ai_office.jpg"
image School_classroom_geography = "School_classroom_geography.jpg"
image School_classroom_maths = "School_classroom_maths.jpg"
image Turkey_flag = "Test_turkey.jpg"
image forest_test = "psych_test_forest.png" 
image studio_logo = "Studio_logo.png"
image corridor_straight = "School_hall_2.png"
image poolroom = "pool.jpg"
image Spain_flag = "test_spain.jpg"
image white = "white.png"
image new_day = "new_day.png"
image good_ending = "good_ending.jpg"
image map_icon = "map_icon.png"
image map = "map.png"

# city i guess lol
image mall = "mall.png"


# Bus images
image bus1 = "bus1.png"
image bus2 = "bus2.png"
# easter-egg bus
image bus3 = "bus3.png"

#Music innitialization (however you spell it)
init:
    # i think this is the Jason theme one lol, thats what happens when you add something 2 months ago and not touch it for a month
    # tak a propo dlaczego jak komentuje i pisze wszystko po angielsku... ehh lepiej brzmi chyba czy coś
    # jak już robię grę po angielsku to czemu nie programować po angielsku lol
    $ renpy.music.register_channel("type_sound", "music", loop=True)

    #  this is the main schoo music
    $ renpy.music.register_channel("main", "music", loop=True)

    # this is the music for thompsomns classroom and tests
    $ renpy.music.register_channel("test", "music", loop=True)

    # this is the sound effect for white flash screen
    $ renpy.music.register_channel("transformation", "music", loop=False)

    # birds and ambience while you're outside
    $ renpy.music.register_channel("ambience", "music", loop=True)

    # music for stressful situations
    $ renpy.music.register_channel("stress", "music", loop=True)

    # music for new days music
    $ renpy.music.register_channel("day2", "music", loop=True)

    # channel for endings music
    $ renpy.music.register_channel("endings", "music", loop=True)

    # channel for lessies theme ig
    $ renpy.music.register_channel("Lesie", "music", loop=True)

    # cHannel for headmasters office.
    $ renpy.music.register_channel("headmaster", "music", loop=True)




#Some variables used for checking if you've already passed the test :)
# variable for the random bus event
define bus = 5

# variable for escape as default, just in case it doesnt get generated later on. better safe than sorry
define escape = 1

#var for ammount of escape tries
define tries = 0

# variable for bus easteregg
define persistent.bus_easteregg = False

# variable for when you get the bad ending
define persistent.bad_ending = False

#variable for getting the good? ending
define persistent.good_ending = False

#variable for getting the true good ending 
define persistent.true_good_ending = False


define interacted_thompson_1 = False
define history_test_passed = False
define maths_test_passed = False
define geography_test_passed = False
define psychology_test_passed = False
define physics_test_passed = False
define chemistry_test_passed = False
define day = 1
define psych_score = 1
define pen_quest = False
define favors = 0
define interacted_Robbert = False
define Jason_started = False

define Lesie_started = False
define Lesie_completed = False
define favor_Lesie = False
# achievements:




# random for set of question

define seed1 = renpy.random.randint(1,2)

define seed2 = renpy.random.randint(1,2)

define seed3 = renpy.random.randint(1,2)

define seed4 = renpy.random.randint(1,2)



define persistent.tests_done = 0

define persistent.bus_easteregg = False

define persistent.bad_ending = False

define persistent.good_ending = False

define persistent.true_good_ending = False

define persistent.are_you_alright = False

define persistent.achievement_love_birds = False



screen achScreen:
    zorder 99
    image "images/achievement_menu.png":
        size (1280, 720)
        pos (0, 0)
    if persistent.bus_easteregg == True:
      image "images/achievement_bus.png":
         size (1280, 720)
         pos (0, 0)
    if persistent.bad_ending == True:
      image "images/achievement_bad_ending.png":
         size (1280, 720)
         pos (0, 0)
    if persistent.good_ending == True:
      image "images/achievement_good_ending.png":
         size (1280, 720)
         pos (0, 0)
    if persistent.true_good_ending == True:
      image "images/achievement_true_good_ending.png":
         size (1280, 720)
         pos (0, 0)
    if persistent.are_you_alright == True:
      image "images/achievement_are_you_alright.png":
         size (1280, 720)
         pos (0,0)
    if persistent.achievement_love_birds == True:
      image "images/achievement_love_birds.png":
         size (1280, 720)
         pos (0,0)
    if persistent.tests_done >= 2:
      image "images/achievement_2_tests.png":
         size (1280, 720)
         pos (0,0)
    if persistent.true_good_ending == True and persistent.good_ending == True and persistent.bad_ending == True:
      image "images/achievement_fully_done.png":
         size (1280, 720)
         pos (0,0)





screen achButton:
    zorder 100 #hopefully always on top of everything 
    imagebutton:
        pos (1200, 630) # x, y to position it on the screen somewhere
        idle "images/achievement.png"
        hover "images/achievement_hover.png"
        focus_mask True 
        action ToggleScreen("achScreen") #it will toggle the screen from show to hide and hide to show automatically







# map of the school
screen mapScreen:
    zorder 99
    image "images/map.png":
       
        size (1280, 720)
        pos (0, 0)






# the top left button corresponding to opening the map. It calls the mapScreen screen, witch opens  map png file
screen mapButton:
    zorder 100 #hopefully always on top of everything 
    imagebutton:
        pos (10, 10) # x, y to position it on the screen somewhere
        idle "images/map_icon.png"
        hover "images/map_icon_hover.png"
        focus_mask True 
        action ToggleScreen("mapScreen") #it will toggle the screen from show to hide and hide to show automatically

# Fovors vbox
# this was a pain to set up. Never again trying to add some bull cr.. like that...
screen fav_counter:
    vbox:
        style_prefix "favors"
        align (1.0,0.0)
        frame:
            background "#9e9677"
            xalign 0.5
            yalign 0.5
            text "Favors: [favors]"




# The game actually starts here lol      
# making it was a fun journey, learned the whole ren'py syntax in about 2 weeks. Thats why "corridor right" is written in a super messy way. It was my first ever piece of code so its a spaghetti   
label start: 

   #shows all the screens
   show screen mapButton
   hide screen fav_counter
   show screen fav_counter
   show screen achButton

   nr "..."
   tr "{size=-10000}{cps=*1000}...{/cps}{/size}{nw}"
   

   stop music
   play sound "alarm.wav" volume 0.25

   scene Bedroom_max
   show max_Joy at right
   with dissolve

   g "Wait..."
   tr "{size=-10000}{cps=*1000}Czekaj...{/cps}{/size}{nw}"
   g "It's 7 am already...?"
   tr "{size=-10000}{cps=*1000}Jest już 7 rano?{/cps}{/size}{nw}"
   g "Well, gotta make myself something to eat..."
   tr "{size=-10000}{cps=*1000}No cóż, czas zrobiś sobie coś do zjedzenia...{/cps}{/size}{nw}"
  
   scene salon
   with dissolve

   show Sarah_Joy

   n "Good morning, Max!"
   tr "{cps=*100099000000000000}{size=-10000}Dzień dobry, Max!{/cps}{/size}{nw}"
   g "Good morning, mom..."
   tr "{cps=*100099000000000000}{size=-10000}Dzień dobry, mamo...{/cps}{/size}{nw}"
   n "Stop slacking off, go make yourself a breakfast"
   tr "{cps=*100099000000000000}{size=-10000}Przestań się ociągać, lepiej zrób sobie śniadanie.{/cps}{nw}"
   n "Also, you should hurry up. Your bus is leaving in 30 minutes."
   tr "{cps=*100099000000000000}{size=-10000}Powinneś się troche pospieszyć, twój autobus odjrzeżdźa za 30 minut.{/cps}{/size}{nw}"

   nr "You eat breakfast and go to school"
   hide screen fav_counter
   show screen fav_counter
   jump school_entrance

   label school_entrance:

           scene school_entrance
           with dissolve
           play ambience "ambience_birds.mp3" volume 0.55
           
           nr "You are standing in front of your school."
           tr "{cps=*100099000000000000}{size=-10000}Stoisz przed wejściem do swojej szkoły{/cps}{/size}{nw}"
   menu:
        
                               
        "Go inside the school": 
               stop ambience    
               play sound "door_slam.ogg" volume 0.25  
               play main "School_theme.wav" volume 0.45  
               hide screen fav_counter
               show screen fav_counter 
               jump school_room1
               with dissolve
        "Bunk off school":
               $ escape = renpy.random.randint(1,2)
               jump mall
               with dissolve



                       
   label mall:
         if tries <= 1:
            scene mall with dissolve
            if escape == 1:
               # You mother doesnt cath you off of school
               # omg moja gramatyka w tych komentarzach jest niemożliwa. tak się kończy siedzenia nad grą o 1 w nocy.
               show max_Joy at right with dissolve
               g "What a good day to escape school!"
               tr "{cps=*100099000000000000}{size=-10000}Ależ to dobry dzień żeby uciec ze szkoły!{/cps}{/size}{nw}" 
               hide max_Joy with dissolve
               nr "You escape school and wander the city for the rest of the day."
               tr "{cps=*100099000000000000}{size=-10000}Uciekasz ze szkoły i włóczysz się po mieście przez resztę dnia.{/cps}{/size}{nw}"
               $ day += 1
               jump day2
            elif escape == 2:
               #your mother cathes you trying to bunk off of school
               show max_Joy at right with dissolve
               g "What a good day to escape scho-"
               tr "{cps=*100099000000000000}{size=-10000}Ależ to dobry dzień żeby uciec ze szko-{/cps}{/size}{nw}" 
               show Sarah_Joy at left with hpunch
               n "What are you doing here!?"
               tr "{cps=*100099000000000000}{size=-10000}Co ty tutaj robisz!?{/cps}{/size}{nw}"
               n "We are going back to school this instant!"
               tr "{cps=*100099000000000000}{size=-10000}Wracamy do szkoły w tym momencie!{/cps}{/size}{nw}" 
               $ tries += 1
               jump school_entrance 
         elif tries >= 2:
               scene mall with dissolve
               show Sarah_Joy at left with hpunch
               n "You are grounded!"
               tr "{cps=*100099000000000000}{size=-10000}Jesteś uziemiony!{/cps}{/size}{nw}" 
               $ day += 1
               jump day2
             
   label school_room1:
            stop test   
                
            scene school_room1
            show Jason at right 
            with dissolve

   
   if interacted_thompson_1 == True:                 
    menu:
               
               "Talk to Jason":
                 
                 stop main
                 play type_sound "Jason_theme_original.wav" volume 0.45
                 if Jason_started == False:
                  if pen_quest == False:
                    
                    t "Hey, Max"
                    tr "{cps=*100099000000000000}{size=-10000}Hej, Max{/cps}{/size}{nw}"
                    t "Can I ask you for a favor?"
                    tr "{cps=*100099000000000000}{size=-10000}Mógłbym poprosić cię o przysługę?{/cps}{/size}{nw}"
                    g "What do you want me to do?"
                    tr "{cps=*100099000000000000}{size=-10000}{/cps}Co chcesz żebym dla ciebię zrobił?{/size}{nw}"
                    t "I lost my Pen. Can you find it?"
                    tr "{cps=*100099000000000000}{size=-10000}Zgubiłem swój długopis. Mógłbyś go dla mnie znaleść?{/cps}{/size}{nw}"


                    nr "Do you want to help Jason for a favor?"
                    tr "{cps=*100099000000000000}{size=-10000}Czy chcesz pomódz Jasonowi w zamian za przysłógę?{/cps}{/size}{nw}"
                    menu:
                       

                       "Help Jason":
                                $ Jason_started = True
                                g "Sure thing"
                                tr "{cps=*100099000000000000}{size=-10000}Pewnie{/cps}{/size}{nw}"
                                t "I will make this up for you!"
                                tr "{cps=*100099000000000000}{size=-10000}Odwdzięcze ci się!{/cps}{/size}{nw}"
                                stop type_sound
                                play main "School_theme.wav" volume 0.45
                                hide screen fav_counter
                                show screen fav_counter
                                jump school_room1


                       "I don't have time for this.":
                                $ Jason_started = False
                                g " I can't help you. I'm too busy."
                                tr "{cps=*100099000000000000}{size=-10000}Nie mogę ci pomodź, jestem zbyt zajęty{/cps}{/size}{nw}"
                                t "No worries."
                                tr "{cps=*100099000000000000}{size=-10000}Nie ma problemu{/cps}{/size}{nw}"
                                stop type_sound
                                play main "School_theme.wav" volume 0.45
                                jump school_room1

                 elif pen_quest == True and Jason_started == True:
                     t "Thanks for finding my pen. I really appreciate it."
                     tr "{size=-10000}{cps=*1000}Dzięki za znalezienie mojego długopisu. Naprawdę to doceniam.{/cps}{/size}{nw}"
                     stop type_sound
                     play main "School_theme.wav" volume 0.45
                     call school_room1 from _call_school_room1 
                 elif Jason_started == True and pen_quest == False:
                     t "Have you found my pen yet?"
                     tr "{size=-10000}{cps=*1000}Znalazłeś już mój długopis?{/cps}{/size}{nw}"
                     g "I'm still looking for it."
                     tr "{size=-10000}{cps=*1000}Wciąż go szukam.{/cps}{/size}{nw}"
                     play main "School_theme.wav" volume 0.45
                     stop type_sound
                     jump school_room1

               
               "Go left":
               
                  jump Corridor_left
               "Go right":
                  
                  jump Corridor_right

               "Go straight ahead":
                  jump Corridor_straight

               "Go outside of the school":
                  nr "You go outside"
                  tr "{size=-10000}{cps=*1000}Wychodzisz na zewnątrz{/cps}{/size}{nw}"
                  stop main
                  stop type_sound
                  stop test
                  jump school_entrance

   elif interacted_thompson_1 == False:
       menu:
        "You gotta hurry up or you will be late for your class!"
        "Go right":
           jump Corridor_right



    #Label corridor (right and left)

   
   # this label is a total mess, i wrote it in the first week of me learning ren'py so its a total piece of spaghetti. Im 2 months in doing this project at the time of writing this and I AM NOT touching it.
   # if i touch it it would propably break and i dont have the time to fix all this bullcrap

   label Corridor_right:
      scene school_classroom_hall
      with dissolve

   #History test below

   menu: 
      "Go inside the classroom":
        stop main
        play test "Test_theme.wav" volume 0.40
        scene school_classroom
        with dissolve
        while history_test_passed == False:  
          while interacted_thompson_1 == False:
             scene school_classroom
             show thompson at right
             show Lesie at left
             with dissolve
             $ interacted_thompson_1 = True
             s "What was Macedonian formation called?" with hpunch
             tr "{size=-10000}{cps=*1000}Jak nazywała się Macedońska formacja bojowa?{/cps}{/size}{nw}"
             l "I don't know..."
             tr "{size=-10000}{cps=*1000}Nie wiem...{/cps}{/size}{nw}"
             s "Why didn't you learn it?"
             tr "{size=-10000}{cps=*1000}Dlaczego się tego nie nauczyłaś?{/cps}{/size}{nw}"
             s "You should have studied more!"
             tr "{size=-10000}{cps=*1000}Powinnaś się więcej uczyć!{/cps}{/size}{nw}"
             l "I'm sorry..."
             tr "{size=-10000}{cps=*1000}Przepraszam...{/cps}{/size}{nw}"
             s "F, sit down."
             tr "{size=-10000}{cps=*1000}Jedynka, siadaj.{/cps}{/size}{nw}"
             
             s "..."
             tr "{size=-10000}{cps=*1000}...{/cps}{/size}{nw}"
             hide Lesie
             hide thompson
             show thompson
             with dissolve

             s "Would you look at that."
             tr "{size=-10000}{cps=*1000}Czego ja nie widzę.{/cps}{/size}{nw}"
             s "You are late again!"
             tr "{size=-10000}{cps=*1000}Znowu jesteś spóźniony!{/cps}{/size}{nw}"
             g "*Oh no*"
             tr "{size=-10000}{cps=*1000}*O nie*{/cps}{/size}{nw}"
             g "Sorry Miss Thompson, won't happen again."
             tr "{size=-10000}{cps=*1000}Przepraszam Pani Thompson, to już się nie powtórzy.{/cps}{/size}{nw}"
             s "Go to Mr Roberts office! Now!"
             tr "{size=-10000}{cps=*1000}Idź do biura dyrektora Robertsa! Już!{/cps}{/size}{nw}"
             play sound "door_slam.ogg" volume 0.25
             stop test
             jump school_Roberts_office_thompson

          scene school_classroom
          show thompson
          with dissolve
          s "Do you want to pass the history test?"
          tr "{size=-10000}{cps=*1000}Czy chciałbyś podejść do testu z historii?{/cps}{/size}{nw}"
          menu:
            "Yes, i want to pass the test":
               s "The first question is:"
               tr "{size=-10000}{cps=*1000}Pierwsze pytanie to:{/cps}{/size}{nw}"
               s "What year did Julius Caesar get assassinated?"
               tr "{size=-10000}{cps=*1000}Kiedy został zamordowany Juliusz Cezar{/cps}{/size}{nw}"
               menu:
                 "44 BC":
                        s "Correct, next question"
                        tr "{size=-10000}{cps=*1000}Poprawna odpowiedź, następne pytanie{/cps}{/size}{nw}"
                        s "How many years did queen Elizabeth II reign?"
                        tr "{size=-10000}{cps=*1000}Ile lat panowała królowa Elżbieta II?{/cps}{/size}{nw}"
                        menu:
                         "70 years":
                           s "Correct, now for the last question..."
                           tr "{size=-10000}{cps=*1000}Dobrze, teraz ostatnie pytanie... {/cps}{/size}{nw}"
                           s "How old was Mao Zedong when he died?"
                           tr "{size=-10000}{cps=*1000}W jakim wieku zginął Mao Zedong{/cps}{/size}{nw}"
                           menu:
                             "72 year old":
                                s "You fail, try again later! The correct answer was: 82 years old." with hpunch
                                tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: 82 years old{/cps}{/size}{nw}"
                                stop test
                                play main "School_theme.wav" volume 0.45
                                $ day += 1
                                jump day2
                             "82 years old":
                                s "Correct, you pass. Congratulations."
                                tr "{size=-10000}{cps=*1000}Dobra odpowiedź, zaliczasz test. Gratuluję. {/cps}{/size}{nw}"
                                $ history_test_passed = True
                                $ persistent.tests_done += 1
                              
                                stop test
                                s "Come back tommorow to pass your maths test."
                                tr "{size=-10000}{cps=*1000}Wróć jutro aby poprawić test z matematyki{/cps}{/size}{nw}"
                                $ day += 1
                                jump day2
                             "69 years old":
                                s "You fail, try again later! The correct answer was: 82 years old." with hpunch
                                tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: 82 years old{/cps}{/size}{nw}"
                                stop test
                                play main "School_theme.wav" volume 0.45
                                $ day += 1
                                jump day2
                         "49 years":
                          s "Incorrect, try again later! The correct answer was: 70 years." with hpunch
                          tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawna odpowiedź to: 70 years{/cps}{/size}{nw}"
                          stop test
                          play main "School_theme.wav" volume 0.45
                          $ day += 1
                          jump day2
                         "64 years":
                          s "Incorrect, try again later! The correct answer was: 70 years." with hpunch
                          tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawna odpowiedź to: 70 years.{/cps}{/size}{nw}"
                          stop test
                          play main "School_theme.wav" volume 0.45
                          $ day += 1
                          jump day2

                    
                      
                 "34 BC":
                    s "Incorrect, Try again later! The correct answer was: 44 BC"
                    tr "{size=-10000}{cps=*1000}Zła odpowiedź, spróbuj ponownie później! Poprawną odpowiedzią jest: 44 BC{/cps}{/size}{nw}"
                    stop test
                    play main "School_theme.wav" volume 0.45
                    $ day += 1
                    jump day2
                 "46 BC":
                    s "Incorrect, Try again later! The correct answer was: 44 BC"
                    tr "{size=-10000}{cps=*1000}Zła odpowiedź, spróbuj ponownie później! Poprawną odpowiedzią jest: 44 BC{/cps}{/size}{nw}"
                    stop test
                    play main "School_theme.wav" volume 0.45
                    $ day += 1
                    jump day2

            "No, i will come back later":
               stop test
               play main "School_theme.wav" volume 0.45
               jump Corridor_right
          scene school_classroom

          #Maths test after passing the history test (thompson teaches like 99% of the subjects so the only logical thing to do is to make her test your all the time)

        while maths_test_passed == False:

           menu:
             "Go back":
              stop test
              play main "School_theme.wav" volume 0.45
              jump Corridor_right
             "Pass maths test":
               
               show thompson at right
               with dissolve
               s "So you came to pass your mathemathics test?"
               tr "{size=-10000}{cps=*1000}A więc przyszłeś poprawić swój test z matematyki?{/cps}{/size}{nw}"
               s "Fine by me."
               tr "{size=-10000}{cps=*1000}Nie ma dla mnie problemu.{/cps}{/size}{nw}"

               if seed1 == 1:
                  
                  s "The first question is: \n You can never divide by:"
                  tr "{size=-10000}{cps=*1000}Pierwsze pytanie to: \n Nigdy nie możesz dzielić przez:{/cps}{/size}{nw}"
                  s "Enter 'skip' if you want to skip this question and use a favor"
                  tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                  $ answer = renpy.input("")
                  if answer == "skip" and favors >= 1:
                     $ favors -= 1
                     $ maths_test_passed = True
                     $ persistent.tests_done += 1
                     stop test
                     hide screen fav_counter
                     show screen fav_counter
                     s "You have used 1 favor. You now have [favors] favors left."
                     tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                     $ day += 1
                     jump day2
                  elif answer.lower() == "0" or answer.lower() == "zero":
                     s "Correct" 
                     tr "{size=-10000}{cps=*1000}Poprawna odpowiedź{/cps}{/size}{nw}"
                     s "The next question is: The Pythagorean theorem is used for a ____ triangle "
                     tr "{size=-10000}{cps=*1000}Twierdzenie pitagorasa jest używane dla trójkątka _____{/cps}{/size}{nw}"
                     s "Enter 'skip' if you want to skip this question and use a favor"
                     tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors >= 1:
                         $ favors -= 1
                         $ maths_test_passed = True
                         $ persistent.tests_done += 1
                         hide screen fav_counter
                         show screen fav_counter
                         s "You have used 1 favor. You now have [favors] favors left."
                         tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                         $ day += 1
                         jump day2
                     elif answer.lower() == "right":
                         s "Correct"
                         tr "{size=-10000}{cps=*1000}Poprawna odpowiedź{/cps}{/size}{nw}"
                         s "The next question is: "
                         tr "{size=-10000}{cps=*1000}Następne pytanie to:{/cps}{/size}{nw}"
                         s "Write the number: six hundred ninety-two thousand one hundred fifty-five"
                         tr "{size=-10000}{cps=*1000}Napisz w postaci liczby:sześćset dziewięćdziesiąt dwa tysiące sto pięćdziesiąt pięć{/cps}{/size}{nw}"
                         s "Enter 'skip' if you want to skip this question and use a favor"
                         tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                         $ answer = renpy.input("")
                         if answer.lower() == "skip" and favors >= 1:
                           $ favors -= 1
                           $ maths_test_passed = True
                           $ persistent.tests_done += 1
                           hide screen fav_counter
                           show screen fav_counter
                           s "You have used 1 favor. You now have [favors] favors left."
                           tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                           $ day += 1
                           jump day2
                         elif answer.lower() == "692155":
                           s "Correct! You are doing really well!"
                           tr "{size=-10000}{cps=*1000}Poprawna odpowiedź. Bardzo dobrze sobie radzisz!{/cps}{/size}{nw}"
                           s "The final question is: What is the square root of nine?"
                           tr "{size=-10000}{cps=*1000}Ostatnie pytanie: Ile to pierwiastek kwadratowy z dziewięciu{/cps}{/size}{nw}"
                           s "Enter 'skip' if you want to skip this question and use a favor"
                           tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                           $ answer = renpy.input("")
                           if answer.lower() == "skip" and favors >= 1:
                                    $ favors -= 1
                                    $ maths_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    s "You have used 1 favor. You now have [favors] favors left."
                                    tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                                    stop test
                                    $ day += 1
                                    jump day2     
                           elif answer.lower() == "3":
                                    "Correct! You pass your maths test!"
                                    tr "{size=-10000}{cps=*1000}Dobra odpowiedź! Zdajesz swój test z matematyki. {/cps}{/size}{nw}"
                                    $ maths_test_passed = True
                                    $ persistent.tests_done += 1
                                    $ day += 1
                                    stop test
                                    jump day2
                           else:
                                 s "Wrong! Try again later! The correct answer is: 3"
                                 tr "{size=-10000}{cps=*1000}Zła odpowiedź. Spróbuj ponownie później. Poprawną odpowiedzią jest 3 {/cps}{/size}{nw}"
                                 
                                 stop test
                                 play main "School_theme.wav" volume 0.45
                                 $ day += 1
                                 jump day2
                         else:
                           s "Wrong! Try again later! The correct answer was: 692155"
                           tr "{size=-10000}{cps=*1000}Zła odpowiedź. Spróbuj ponownie później. Poprawną odpowiedzią jest: 692155{/cps}{/size}{nw}"
                           stop test
                           play main "School_theme.wav" volume 0.45
                           $ day += 1
                           jump day2
                     else:
                           s "Wrong! Try again later! The correct answer is: right"
                           tr "{size=-10000}{cps=*1000}Zła odpowiedź. Spróbuj ponownie później. Poprawną odpowiedzią jest: right{/cps}{/size}{nw}"
                           stop test
                           play main "School_theme.wav" volume 0.45
                           $ day += 1
                           jump day2
                  else:
                     s "Wrong! Try again later! The correct answers are: 0 and zero"
                     tr "{size=-10000}{cps=*1000}Zła odpowiedź. Spróbuj ponownie później. Poprawnnymi odpowiedziami są: 0 i zero{/cps}{/size}{nw}"
                     stop test
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2


               elif seed1 == 2:
                  
                  s "The first question is: \n The square of the number is always:"
                  tr "{size=-10000}{cps=*1000}Pierwsze pytanie brzmi: \n Kwadrat liczby jest zawsze:{/cps}{/size}{nw}"
                  s "Enter 'skip' if you want to skip this question and use a favor"
                  tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                  $ answer = renpy.input("")
                  if answer.lower() == "skip" and favors >= 1:
                     $ favors -= 1
                     $ maths_test_passed = True
                     $ persistent.tests_done += 1
                     hide screen fav_counter
                     show screen fav_counter
                     s "You have used 1 favor. You now have [favors] favors left."
                     tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                     $ day += 1
                     jump day2
                     stop test
                  elif answer.lower() == "a positive number" or answer.lower() == "positive" or answer.lower() == "positive number" or answer.lower() == "+":
                     s "Correct" 
                     tr "{size=-10000}{cps=*1000}Poprawna odpowiedź{/cps}{/size}{nw}"
                     s "The next question is: The Pythagorean theorem is used for a ____ triangle "
                     tr "{size=-10000}{cps=*1000}Twierdzenie Pitagorasa jest używane dla trójkąta _____{/cps}{/size}{nw}"
                     s "Enter 'skip' if you want to skip this question and use a favor"
                     tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors >= 1:
                       
                         $ favors -= 1
                         $ maths_test_passed = True 
                         $ persistent.tests_done += 1
                         hide screen fav_counter
                         show screen fav_counter
                         s "You have used 1 favor. You now have [favors] favors left."
                         tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                         stop test
                         play main "School_theme.wav" volume 0.45
                         $ day += 1
                         jump day2
                     elif answer.lower() == "right" or answer.lower() == "rectangle":
                         s "Correct"
                         tr "{size=-10000}{cps=*1000}Poprawna odpowiedź{/cps}{/size}{nw}"
                         s "The next question is: "
                         tr "{size=-10000}{cps=*1000}Następne pytanie to: {/cps}{/size}{nw}"
                         s "Write the number: two thousand one hundred thirty-seven"
                         tr "{size=-10000}{cps=*1000}Napisz numer: Dwa tysiące sto trzydzieści siedem{/cps}{/size}{nw}"
                         s "Enter 'skip' if you want to skip this question and use a favor"
                         tr "{size=-10000}{cps=*1000}Napisz 'skip' jeżeli chcesz pominąć to pytanie{/cps}{/size}{nw}"
                         $ answer = renpy.input("")
                         if answer.lower() == "skip" and favors >= 1:
                           
                           $ favors -= 1
                           $ maths_test_passed = True
                           $ persistent.tests_done += 1
                           hide screen fav_counter
                           show screen fav_counter
                           s "You have used 1 favor. You now have [favors] favors left."
                           tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                           stop test
                           play main "School_theme.wav" volume 0.45
                           $ day += 1
                           jump day2
                         elif answer.lower() == "2137":
                           s "Correct! You are doing really well!"
                           s "The final question is: What is the square root of four?"
                           s "Enter 'skip' if you want to skip this question and use a favor"
                           $ answer = renpy.input("")
                           if answer.lower() == "skip" and favors >= 1:
                                    $ favors -= 1
                                    $ maths_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    s "You have used 1 favor. You now have [favors] favors left."
                                    tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                                    stop test
                                    play main "School_theme.wav" volume 0.45
                                    $ day += 1
                                    jump day2
                           elif answer.lower() == "2":
                                    s "Correct! You pass your maths test!"
                                    tr "{size=-10000}{cps=*1000}Poprawna odpowiedź! Zdajesz test z matematyki!{/cps}{/size}{nw}"
                                    $ maths_test_passed = True
                                    $ persistent.tests_done += 1
                                    $ day += 1
                                    stop test
                                    jump day2
                                    
                           else:
                                 s "Wrong! Try again later! The correct answer is: 2" 
                                 tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: 2{/cps}{/size}{nw}"
                                 play main "School_theme.wav" volume 0.45
                                 stop test
                                 $ day += 1
                                 jump day2
                         else:
                           s "Wrong! Try again later! The correct answer was: 2137"
                           tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: 2137{/cps}{/size}{nw}"
                           play main "School_theme.wav" volume 0.45
                           stop test
                           $ day += 1
                           jump day2
                     else:
                           s "Wrong! Try again later! The correct answer is: right"
                           tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: right{/cps}{/size}{nw}"
                           play main "School_theme.wav" volume 0.45
                           stop test
                           $ day += 1
                           jump day2
                  else:
                     s "Wrong! Try again later! The correct answer is: Positive"
                     tr "{size=-10000}{cps=*1000}Zła odpowiedź! Spróbuj ponownie później! Poprawną odpowiedzią jest: Positive{/cps}{/size}{nw}"
                     play main "School_theme.wav" volume 0.45
                     stop test
                     $ day += 1
                     jump day2


            
                   


      "Go back":
         stop test
         call school_room1 from _call_school_room1_1 
         
         


   
   menu:
     "Go back":
         stop test
         play main "School_theme.wav" volume 0.45
         jump Corridor_right
         

   
   label Corridor_left:

      scene school_staircase
      with dissolve
   menu:
      "Go to Mr. Ai's office":
         jump School_Ai_office
      
      "Go inside geography classroom":
         jump School_classroom_geography

      "Go back":
         jump school_room1

   #Ais office

   label School_Ai_office:
        
   while psychology_test_passed == False:
     scene School_Ai_office
     show Ai at right
     with dissolve
     menu:
      "Go back":
         jump Corridor_left
      "Take the psychological evaluation":
         stop main
         sm "So you'd like to pass your psychological evaluation?"
         tr "{size=-10000}{cps=*1000}A więc chciałbyś zaliczyć swoją ewaluacje psychiczną?{/cps}{/size}{nw}"
         sm "Very well then!"
         tr "{size=-10000}{cps=*1000}Dobrze więc!{/cps}{/size}{nw}"
         scene forest_test
         with dissolve
         sm "Imagine this, you are walking alone, through the forest in the middle of the night, you turn around quickly, what do you see?"
         tr "{size=-10000}{cps=*1000}Wyobraź sobie, że idziesz samotnie przez las w środku nocy, szybko się odwracasz, co widzisz?{/cps}{/size}{nw}"
         menu:
                      
            "Nothing":
                $ psych_score = 1
                scene School_Ai_office
                show Ai at right
                with dissolve
                sm "Lets say, you were a robber. You break into someone's house in the middle of the night, but they see you. They quickly hide in a closet, what do you do?"
                tr "{size=-10000}{cps=*1000}Powiedzmy, że byłeś złodziejem. Włamujesz się do czyjegoś domu w środku nocy, ale ktoś cię widzi. Szybko chowają się do szafy, co robisz?{/cps}{/size}{nw}"
                menu:
                 

                 "Wait quietly until they think they're safe, and then when they get out of that closet make sure there is no evidence.":
                     $ psych_score +=1
                     sm "That's a conserning answer."
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "No witnesses...":
                     sm "Most people would say that."
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "Run hoping they didn't see your face.":
                     sm "I expected that answer from you."
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
            "A wild animal":
                $ psych_score = 1
                scene School_Ai_office
                show Ai at right
                with dissolve
                sm "Lets say, you were a robber. You break into someone's house in the middle of the night, but they see you. They quickly hide in a closet, what do you do?"
                tr "{size=-10000}{cps=*1000}Powiedzmy, że byłeś złodziejem. Włamujesz się do czyjegoś domu w środku nocy, ale ktoś cię widzi. Szybko chowają się do szafy, co robisz?{/cps}{/size}{nw}"
                menu:
                 

                 "Wait quietly until they think they're safe, and then when they get out of that closet make sure there is no evidence.":
                     $ psych_score +=1
                     sm "That's a conserning answer."
                     tr "{size=-10000}{cps=*1000}To niepokojąca odpowiedź{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "No witnesses...":
                     sm "Most people would say that."
                     tr "{size=-10000}{cps=*1000}To niepokojąca odpowiedź{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "Run hoping they didn't see your face.":
                     sm "I expected that answer from you."
                     tr "{size=-10000}{cps=*1000}Spodziewałem się tej odpowiedzi po tobie{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
            # A dog is the psychopaths answer, according to psychological studies, psychopaths are more likely to pick a dog in this question (Dunno why)   
            "A dog": 
                $ psych_score += 1
                scene School_Ai_office
                show Ai at right
                with dissolve
                sm "Lets say, you were a robber. You break into someone's house in the middle of the night, but they see you. They quickly hide in a closet, what do you do?"
                tr "{size=-10000}{cps=*1000}Powiedzmy, że byłeś złodziejem. Włamujesz się do czyjegoś domu w środku nocy, ale ktoś cię widzi. Szybko chowają się do szafy, co robisz?{/cps}{/size}{nw}"
                menu:

                 "Wait quietly until they think they're safe, and then when they get out of that closet make sure there is no evidence.":
                     $ psych_score +=1
                     sm "That's a conserning answer."
                     tr "{size=-10000}{cps=*1000}To niepokojąca odpowiedź{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     
                     while persistent.are_you_alright == False:
                        $ persistent.are_you_alright = True
                        call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'Are you alright?' ")
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "No witnesses...":
                     sm "Most people would say that."
                     tr "{size=-10000}{cps=*1000}To niepokojąca odpowiedź{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
                 "Run hoping they didn't see your face.":
                     sm "I expected that answer from you."
                     tr "{size=-10000}{cps=*1000}Spodziewałem się tej odpowiedzi po tobie{/cps}{/size}{nw}"
                     sm "Thats all i wanted from you, your answers were preatty interesting"
                     tr "{size=-10000}{cps=*1000}To wszystko co od ciebię chciałem, twoje odpowiedzi były dość interesujące{/cps}{/size}{nw}"
                     $ psychology_test_passed = True
                     $ persistent.tests_done += 1
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
   nr "The door is locked"
   tr "{size=-10000}{cps=*1000}Drzwi są zamknięte.{/cps}{/size}{nw}"
   
   jump Corridor_left
                     


   #Geography classroom 
   
   label School_classroom_geography:
      stop main
      scene School_classroom_geography
      show Froga
      with dissolve
      if pen_quest == False and Jason_started == True:
       menu: 
            "Go back":
               play main "School_theme.wav" volume 0.45
               jump Corridor_left
   
            "Look for Jason's pen":
               nr "You have found Jason's pen"
               tr "{size=-10000}{cps=*1000}Znalazłeś długopis Jasona{/cps}{/size}{nw}"
               $ pen_quest = True
               $ favors += 1
               nr "Favors let you skip the test of your choice. If you're struggling with passing a test, you can use a favor!"
               tr "{size=-10000}{cps=*1000}Przysługi pozwalają ci pominąć dowolny test twojego wyboru. Jeśli nie radzisz sobie ze zdaniem jednego z testów, możesz użyć przysługi!{/cps}{/size}{nw}"
               hide screen fav_counter
               show screen fav_counter
               play main "School_theme.wav" volume 0.45
               jump Corridor_left
         
      if seed2 == 1:
       while geography_test_passed == False: 
          c "Would you like to pass your geography test?"
          tr "{size=-10000}{cps=*1000}Czy chciałbyś zaliczyć test z geografii?{/cps}{/size}{nw}"
          menu:
            
            "Yes, please":
               c "Good luck!"
               tr "{size=-10000}{cps=*1000}powodzenia!{/cps}{/size}{nw}"
               c "First question: What's the capital of Canada?"
               tr "{size=-10000}{cps=*1000}Pierwsze pytanie to: Jaka jest stolica Kanady?{/cps}{/size}{nw}"
               c "If you want to skip this question write 'skip' as an answer"
               tr "{size=-10000}{cps=*1000}Jeżeli chcesz pominąć ten test napisz 'skip'{/cps}{/size}{nw}"
               $ answer = renpy.input("")
               if answer.lower() == "skip" and favors >= 1:
                     $ favors -= 1
                     $ geography_test_passed = True
                     $ persistent.tests_done += 1
                     $ day += 1
                     hide screen fav_counter
                     show screen fav_counter
                     play main "School_theme.wav" volume 0.45
                     jump day2
                     
               elif answer.lower() == "ottawa":
                     c "Correct!"
                     tr "{size=-10000}{cps=*1000}Dobra odpowiedź!{/cps}{/size}{nw}"
                     c "What flag is this?"
                     tr "{size=-10000}{cps=*1000}Jaka to flaga?{/cps}{/size}{nw}"
                     c "If you want to skip this question write 'skip' as an answer"
                     tr "{size=-10000}{cps=*1000}Jeżeli chcesz pominąć ten test napis 'skip'{/cps}{/size}{nw}"
                     show Turkey_flag at top with dissolve
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors >= 1:
                           $ geography_test_passed = True
                           $ persistent.tests_done += 1
                           $ favors -= 1
                           $ day += 1
                           play main "School_theme.wav" volume 0.45
                           jump day2
                     elif answer.lower() == "turkey":
                              c "Correct!"
                              tr "{size=-10000}{cps=*1000}Poprawna odpowiedź!{/cps}{/size}{nw}"
                              hide Turkey_flag
                              c "Now for the last question"
                              tr "{size=-10000}{cps=*1000}Teraz, ostatnie pytanie to:{/cps}{/size}{nw}"
                              c "What's the longest river in Asia?"
                              tr "{size=-10000}{cps=*1000}Jaka jest najdłuższa rzeka Azjii?{/cps}{/size}{nw}"
                              c "If you want to skip this question write 'skip' as an answer"
                              tr "{size=-10000}{cps=*1000}Jeżeli chcesz pominąć ten test napis 'skip'{/cps}{/size}{nw}"
                              $ answer = renpy.input("")
                              if answer.lower() == "yangtze river" or answer.lower() == "yangze" or answer.lower() == "yangrze river" or answer.lower() == "yangtze":
                                 c "Good job! You pass!"
                                 tr "{size=-10000}{cps=*1000}Dobra robota! Zdajesz! {/cps}{/size}{nw}"
                                 $ geography_test_passed = True
                                 $ persistent.tests_done += 1
                                 $ day += 1
                                
                                 hide screen fav_counter
                                 show screen fav_counter
                                 play main "School_theme.wav" volume 0.45
                                 jump day2
                              
                              elif answer.lower() == "skip" and favors > 0:
                                 if favors > 0:
                                    c "You have skipped the question and lost 1 favor"
                                    tr "{size=-10000}{cps=*1000}Użyłes 1 przysługi. Zostało ci [favors] przysług.{/cps}{/size}{nw}"
                                    $ favors -= 1
                                    $ day += 1
                                    $ geography_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    play main "School_theme.wav" volume 0.45
                                    jump day2

                              else:
                                 c "Incorrect, you were so close to passing! The correct answer was: Yangtze River"
                                 tr "{size=-10000}{cps=*1000}Źle, byłeś tak blisko zdania! Poprawną odpowiedzią była: Yangtze River{/cps}{/size}{nw}"
                                 play main "School_theme.wav" volume 0.45
                                 $ day += 1
                                 jump day2 
                     else:
                              c "Incorrect, how could you not know this one? The correct answer was Turkey."
                              tr "{size=-10000}{cps=*1000}Zła odpowiedź, jak mogłeś tego nie wiedzieć? Poprawną odpowiedzią była: Turkey{/cps}{/size}{nw}"
                              play main "School_theme.wav" volume 0.45
                              $ day += 1
                              jump day2
               else:
                     c "Try again, later. The correct answer was: Ottawa"
                     tr "{size=-10000}{cps=*1000}Spróbuj ponownie później. Poprawną odpowiedzią była: Ottawa{/cps}{/size}{nw}"
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
            "I'm not ready yet":
               play main "School_theme.wav" volume 0.45
               jump Corridor_left
      
      elif seed2 == 2:
         while geography_test_passed == False: 
          c "Would you like to pass your geography test?"
          tr "{size=-10000}{cps=*1000}Czy chciałbyś podejść do testu z geografii?{/cps}{/size}{nw}"
          menu: 
            
            "Yes, please":  
               c "Good luck!"
               tr "{size=-10000}{cps=*1000}Powodzenia!{/cps}{/size}{nw}"
               c "First question: What's the largest ocean in the world?"
               tr "{size=-10000}{cps=*1000}Jaki ocean jest największy na świecie?{/cps}{/size}{nw}"
               c "If you want to skip this question write 'skip' as an answer"
               tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
               $ answer = renpy.input("")
               if answer.lower() == "skip" and favors > 0:
                     
                     $ geography_test_passed = True
                     $ persistent.tests_done += 1
                     $ day += 1
                     $ favors -= 1
                     hide screen fav_counter
                     show screen fav_counter
                     play main "School_theme.wav" volume 0.45
                     jump day2
                     
               elif answer.lower() == "pacific ocean" or answer.lower() == "pacific":
                     c "Correct!"
                     tr "{size=-10000}{cps=*1000}Poprawna odpowiedź!{/cps}{/size}{nw}"
                     c "What flag is this?"
                     tr "{size=-10000}{cps=*1000}Co to za flaga?{/cps}{/size}{nw}"
                     c "If you want to skip this question write 'skip' as an answer"
                     tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                     show Spain_flag at top with dissolve
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors > 0:
                           $ favors -= 1
                           $ geography_test_passed = True
                           $ persistent.tests_done += 1
                           $ day += 1
                           play main "School_theme.wav" volume 0.45
                           jump day2
                     elif answer.lower() == "spain":
                              c "Correct!"
                              tr "{size=-10000}{cps=*1000}Poprawna odpowiedź!{/cps}{/size}{nw}"
                              hide Spain_flag
                              c "Now for the last question:"
                              tr "{size=-10000}{cps=*1000}Ostatnie pytanie to:{/cps}{/size}{nw}"
                              c "What's the highest mountain in the world?"
                              tr "{size=-10000}{cps=*1000}Jaka jest najwyższy szczyt na świecie?{/cps}{/size}{nw}"
                              c "If you want to skip this question write 'skip' as an answer"
                              $ answer = renpy.input("")
                              if answer.lower() == "mount everest" or "everest" or "mt. everest":
                                 c "Correct, you pass!"
                                 tr "{size=-10000}{cps=*1000}Dobrze, zaliczasz!{/cps}{/size}{nw}"
                                 $ geography_test_passed = True
                                 $ persistent.tests_done += 1
                                 $ day += 1
                           
                                 hide screen fav_counter
                                 show screen fav_counter
                                 play main "School_theme.wav" volume 0.45
                                 jump day2
                              
                              elif answer.lower() == "skip" and favors > 0:
                                 if favors > 0:
                                    c "You have skipped the test and lost 1 favor"
                                    tr "{size=-10000}{cps=*1000}Pominąłeś to pytanie i straciłeś 1 przysługę.{/cps}{/size}{nw}"
                                    $ favors -= 1
                                    $ day += 1
                                    $ geography_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    play main "School_theme.wav" volume 0.45
                                    jump day2
                              else:
                                 c "Incorrect, you were so close to passing! The correct answers were: Everest, Mt. Everest, Mount Everest."
                                 tr "{size=-10000}{cps=*1000}Zła odpowiedź, byłeś tak blisko zdania! Poprawnymi odpowiedziami były: Everest, Mt. Everest, Mount Everest.{/cps}{/size}{nw}"
                                 play main "School_theme.wav" volume 0.45
                                 $ day += 1
                                 jump day2
                     else:
                              c "Incorrect, how did you get this one wrong? The correct answer was: Spain"
                              tr "{size=-10000}{cps=*1000}Zła odpowiedź, jak mogłeś odpowiedzieć na to źle? Poprawną odpowiedzią było: Spain{/cps}{/size}{nw}"
                              play main "School_theme.wav" volume 0.45
                              $ day += 1
                              jump day2
               else:
                     c "Try again later. The correct answer was: Pacific Ocean"
                     tr "{size=-10000}{cps=*1000}Spróbuj ponownie później. Poprawną odpowiedzią był: Pacific Ocean{/cps}{/size}{nw}"
                     play main "School_theme.wav" volume 0.45
                     $ day += 1
                     jump day2
            "I'm not ready yet":
                  play main "School_theme.wav" volume 0.45
                  jump Corridor_left

      menu:
       "Go back":
         jump Corridor_left
         play main "School_theme.wav" volume 0.45




   #Label for Robertss office - normal
   label school_Roberts_office:
      scene School_Roberts_office
      show Roberts at right
      with dissolve
      
      stop main
      play headmaster "headmaster.wav" volume 0.45

      b "Would you like to see the progress on your tests?"
      tr "{size=-10000}{cps=*1000}Chciałbyś zobaczyć swój postęp w poprawianiu testów?{/cps}{/size}{nw}"
   menu:
      
      "Yes, please":
       b "What test would you like to check?"
       tr "{size=-10000}{cps=*1000}Jaki przedmiot chciałbyś sprawdzić?{/cps}{/size}{nw}"
       menu:
         
         "History":
           if history_test_passed == True:
            b "You have passed your history test"
            tr "{size=-10000}{cps=*1000}Zdałeś już swój test z historii.{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office
           else:
            b "You still haven't passed your history test"
            tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojego testu z historii.{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_1
         "Maths":
           if maths_test_passed == True:
            b "You have passed your mathematics test"
            tr "{size=-10000}{cps=*1000}Zdałeś już swój test z matematyki.{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_2 
           else:
            b "You still haven't passed your maths test"
            tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojego testu z matematyki{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_3 
         "Geography":
           if geography_test_passed == True:
            b "You have passed your geography test"
            tr "{size=-10000}{cps=*1000}Zdałeś już swój test z geografii.{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_4  
           else:
            b "You still haven't passed your geography test"
            tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojego testu z geografii.{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_5 
         "Psychological Evaluation":
           if psychology_test_passed == True:
            b "You have passed your psychological evaluation"
            tr "{size=-10000}{cps=*1000}Zdałeś już swoją ewaluacje psychiczną{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_6 
           else:
            b "You still haven't passed your psychological evaluation"
            tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojej ewaluacji psychicznej{/cps}{/size}{nw}"
            call school_Roberts_office from _call_school_Roberts_office_7  
         "Chemisty test":
            if chemistry_test_passed == True:
               b "You have passed your chemistry test"
               tr "{size=-10000}{cps=*1000}Zdałeś już swój test z chemii{/cps}{/size}{nw}"
               call school_Roberts_office from _call_school_Roberts_office_8 
            else:
               b "You still haven't passed your chemistry test"
               tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojego testu z chemii{/cps}{/size}{nw}"
               call school_Roberts_office from _call_school_Roberts_office_9    
         "Physics test":
            if physics_test_passed == True:
               b "You have passed your physics test"
               tr "{size=-10000}{cps=*1000}Zdałeś już swój test z fizyki{/cps}{/size}{nw}"
               call school_Roberts_office from _call_school_Roberts_office_10 
            elif physics_test_passed == False:    
               b "You still haven't passed your physics test"
               tr "{size=-10000}{cps=*1000}Jeszcze nie zdałeś swojego testu z fizyki{/cps}{/size}{nw}"
               call school_Roberts_office from _call_school_Roberts_office_11 
       
      "Go back":
         stop headmaster
         play main "School_theme.wav" volume 0.45
         call Corridor_straight from _call_Corridor_straight 
         



   #Corridor straight and right? I think so lol

   label Corridor_straight:
      scene corridor_straight
      with dissolve
      show Robbert_far at right
   if interacted_Robbert == True:

      menu:
          "Talk to Robbert":
           if Lesie_started == True and Lesie_completed == False:
              menu:
                "Give Lesie's letter to Robbert":
                     g "Lesie wanted me to give you this letter."
                     tr "{size=-10000}{cps=*1000}Lesie chciała żebym dał ci ten list.{/cps}{/size}{nw}"
                     bob "I will be sure to read it!"
                     tr "{size=-10000}{cps=*1000}Napewno go przeczytam!{/cps}{/size}{nw}"
                     $ Lesie_completed = True
                     jump Corridor_straight

           if physics_test_passed == False or chemistry_test_passed == False:
            hide Robbert_far
            show Robbert_closeup
            bob "Which subject would you like to pass?"
            tr "{size=-10000}{cps=*1000}Który przedmiot chciałbyś zdać?{/cps}{/size}{nw}"
            menu: 
             "Chemisty exam":
              if chemistry_test_passed == False:
                if seed3 == 1:
                     bob "Good luck!"
                     tr "{size=-10000}{cps=*1000}Powodzenia/cps}{/size}{nw}"
                     bob "First question: What is the chemical formula for sulfuric acid (VI)?"
                     tr "{size=-10000}{cps=*1000}Jaki jest wzór chemiczny kwasu siarkowego (VI)? {/cps}{/size}{nw}"
                     bob "If you want to skip this question write 'skip' as an answer"
                     tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors > 0:
                           $ favors -= 1
                           $ chemistry_test_passed = True
                           $ persistent.tests_done += 1
                           $ day += 1
                           hide screen fav_counter
                           show screen fav_counter
                           play main "School_theme.wav" volume 0.45
                           jump day2
                           
                     elif answer.lower() == "h2so4":
                           bob "Correct!"
                           tr "{size=-10000}{cps=*1000}Dobra odpowiedź{/cps}{/size}{nw}"
                           bob "What is the chemical formula for water?"
                           tr "{size=-10000}{cps=*1000}Jaki jest wzór chemiczny na wodę?{/cps}{/size}{nw}"
                           bob "If you want to skip this question write 'skip' as an answer"
                           tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                           $ answer = renpy.input("")
                           if answer.lower() == "skip" and favors > 0:
                                 $ favors -= 1
                                 $ chemistry_test_passed = True
                                 $ persistent.tests_done += 1
                                 $ day += 1
                                 hide screen fav_counter
                                 show screen fav_counter
                                 play main "School_theme.wav" volume 0.45
                                 jump day2
                           elif answer.lower() == "h2o":
                                    bob "Correct!"
                                    tr "{size=-10000}{cps=*1000}Dobra odpowiedź{/cps}{/size}{nw}"
                                    bob "The last question is:"
                                    tr "{size=-10000}{cps=*1000}Ostatnie pytanie brzmi:{/cps}{/size}{nw}"
                                    bob "What is the chemical formula for chlorine?"
                                    tr "{size=-10000}{cps=*1000}Jaki jest symbol chemiczny chloru?{/cps}{/size}{nw}"
                                    bob "If you want to skip this question write 'skip' as an answer"
                                    tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                                    $ answer = renpy.input("")
                                    if answer.lower() == "cl":
                                       bob "Correct, you pass!"
                                       tr "{size=-10000}{cps=*1000}Dobra odpowiedź, zdajesz!{/cps}{/size}{nw}"
                                       $ chemistry_test_passed = True
                                       $ persistent.tests_done += 1
                                       $ day += 1
                                       
                                       hide screen fav_counter
                                       show screen fav_counter
                                       play main "School_theme.wav" volume 0.45
                                       jump day2
                                    
                                    elif answer.lower() == "skip" and favors > 0:
                                       if favors > 0:
                                          bob "You have skipped the question and lost 1 favor"
                                          tr "{size=-10000}{cps=*1000}Tracisz 1 przysługę.{/cps}{/size}{nw}"
                                          $ favors -= 1
                                          $ day += 1
                                          $ chemistry_test_passed = True
                                          $ persistent.tests_done += 1
                                          hide screen fav_counter
                                          show screen fav_counter
                                          play main "School_theme.wav" volume 0.45
                                          jump day2
                                       else:
                                          bob "You don't have enough favors"
                                          tr "{size=-10000}{cps=*1000}Nie masz wystarczająco przysług.{/cps}{/size}{nw}"
                                          play main "School_theme.wav" volume 0.45
                                          $ day += 1
                                          jump day2
                                    else:
                                       bob "Incorrect! The correct answer was Cl"
                                       tr "{size=-10000}{cps=*1000}Zła odpowiedź! Poprawną odpowiedzią było: Cl{/cps}{/size}{nw}"
                                       play main "School_theme.wav" volume 0.45
                                       $ day += 1
                                       jump day2
                           else:
                                    bob "Incorrect, how did you get this one wrong? The correct answer was H2O"
                                    tr "{size=-10000}{cps=*1000}Zła odpowiedź, jak mogłeś na to źle odpowiedzieć? Poprawną odpowiedzią było: H2O{/cps}{/size}{nw}"
                                    play main "School_theme.wav" volume 0.45
                                    $ day += 1
                                    jump day2
                     else:
                           bob "Try again, later. The correct answer is: H2SO4"
                           tr "{size=-10000}{cps=*1000}Zła odpowiedź. Poprawna odpowiedź to: H2SO4{/cps}{/size}{nw}"
                           play main "School_theme.wav" volume 0.45
                           $ day += 1
                           jump day2

                elif seed3 == 2:
                     b "Good luck!"
                     tr "{size=-10000}{cps=*1000}Powodzenia!{/cps}{/size}{nw}"
                     bob "First question: What is the chemical symbol for gold?"
                     tr "{size=-10000}{cps=*1000}Jaki jest symbol chemiczny złota{/cps}{/size}{nw}"
                     bob "If you want to skip this question write 'skip' as an answer"
                     tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                     $ answer = renpy.input("")
                     if answer.lower() == "skip" and favors > 0:
                           $ favors -= 1
                           $ chemistry_test_passed = True
                           $ persistent.tests_done += 1
                           $ day += 1
                           hide screen fav_counter
                           show screen fav_counter
                           play main "School_theme.wav" volume 0.45
                           jump day2
                           
                     elif answer.lower() == "au":
                           bob "Correct!"
                           tr "{size=-10000}{cps=*1000}Dobra odopowiedź!{/cps}{/size}{nw}"
                           bob "What is the chemical formula for water?"
                           tr "{size=-10000}{cps=*1000}Jaki jest wzór chemiczny wody?{/cps}{/size}{nw}"
                           bob "If you want to skip this question write 'skip' as an answer"
                           tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                           $ answer = renpy.input("")
                           if answer.lower() == "skip" and favors > 0:
                                 $ favors -= 1
                                 $ chemistry_test_passed = True
                                 $ persistent.tests_done += 1
                                 $ day += 1
                                 hide screen fav_counter
                                 show screen fav_counter
                                 play main "School_theme.wav" volume 0.45
                                 jump day2
                           elif answer.lower() == "h2o":
                                    bob "Correct!"
                                    tr "{size=-10000}{cps=*1000}Poprawna odpowiedź{/cps}{/size}{nw}"
                                    bob "Now for the last question"
                                    tr "{size=-10000}{cps=*1000}Ostatnie pytanie to:{/cps}{/size}{nw}"
                                    bob "What is the chemical formula for carbon dioxide?"
                                    tr "{size=-10000}{cps=*1000}Jaki jest wzór chemiczny dwutlenku węgla?{/cps}{/size}{nw}"
                                    bob "If you want to skip this question write 'skip' as an answer"
                                    tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                                    $ answer = renpy.input("")
                                    if answer.lower() == "co2":
                                       bob "Correct, you pass!"
                                       tr "{size=-10000}{cps=*1000}Dobra odpowiedź, zdajesz!{/cps}{/size}{nw}"
                                       $ chemistry_test_passed = True
                                       $ persistent.tests_done += 1
                                       $ day += 1
                                       
                                       hide screen fav_counter
                                       show screen fav_counter
                                       play main "School_theme.wav" volume 0.45
                                       jump day2
                                    
                                    elif answer.lower() == "skip" and favors > 0:
                                       if favors > 0:
                                          bob "You have skipped the question and lost 1 favor"
                                          tr "{size=-10000}{cps=*1000}Pominąłeś to pytanie i straciłeś 1 {/cps}{/size}{nw}"
                                          $ favors -= 1
                                          $ day += 1
                                          $ chemistry_test_passed = True
                                          $ persistent.tests_done += 1
                                          hide screen fav_counter
                                          show screen fav_counter
                                          play main "School_theme.wav" volume 0.45
                                          jump day2
                                       else:
                                          bob "You don't have enough favors"
                                          tr "{size=-10000}{cps=*1000}Nie masz wystarczająco przysług{/cps}{/size}{nw}"
                                          play main "School_theme.wav" volume 0.45
                                          $ day += 1
                                          jump day2
                                    else:
                                       bob "Incorrect, you were so close to passing! The correct answer was CO2"
                                       tr "{size=-10000}{cps=*1000}Nie poprawna odpowiedź, byłeś tak blisko zdania! Poprawną odpowiedzią było CO2{/cps}{/size}{nw}"
                                       play main "School_theme.wav" volume 0.45
                                       $ day += 1
                                       jump day2
                           else:
                                    bob "Incorrect, how did you get this one wrong? The correct answer was: H2O"
                                    tr "{size=-10000}{cps=*1000}Zła odpowiedź, jak mogłeś sobie z tym nie poradzić? Poprawną odpowiedzią było: H2O{/cps}{/size}{nw}"
                                    play main "School_theme.wav" volume 0.45
                                    $ day += 1
                                    jump day2
                     else:
                           bob "Try again later. The correct answer was: Au"
                           tr "{size=-10000}{cps=*1000}Spróbuj ponownie później. Poprawną odpowiedzią było: Au{/cps}{/size}{nw}"
                           play main "School_theme.wav" volume 0.45
                           $ day += 1
                           jump day2
      
              elif chemistry_test_passed == True:
                bob "You have already passed this test!"
                tr "{size=-10000}{cps=*1000}Już zdałeś ten test{/cps}{/size}{nw}"
                $ day +=1
                jump Corridor_straight
                
             "Physics exam":
              if physics_test_passed == False:  
               if seed4 == 1:
                  bob "Good luck!"
                  tr "{size=-10000}{cps=*1000}Powodzenia{/cps}{/size}{nw}"
                  bob "First question: What is the unit of force?"
                  tr "{size=-10000}{cps=*1000}Pierwsze pytanie: Jaka jest jednostka siły?{/cps}{/size}{nw}"
                  bob "If you want to skip this question write 'skip' as an answer"
                  tr "{size=-10000}{cps=*1000}Jeśłi chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                  $ answer = renpy.input("")
                  if answer.lower() == "skip" and favors > 0:
                        $ favors -= 1
                        $ physics_test_passed = True
                        $ persistent.tests_done += 1
                        $ day += 1
                        hide screen fav_counter
                        show screen fav_counter
                        play main "School_theme.wav" volume 0.45
                        jump day2
                        
                  elif answer.lower() == "newton":
                        bob "Correct!"
                        tr "{size=-10000}{cps=*1000}Poprawna odpowiedź!{/cps}{/size}{nw}"
                        bob "What is the unit of work?"
                        tr "{size=-10000}{cps=*1000}Jaka jest jednostka pracy w układzie Si{/cps}{/size}{nw}"
                        bob "If you want to skip this question write 'skip' as an answer"
                        tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                        $ answer = renpy.input("")
                        if answer.lower() == "skip" and favors > 0:
                           $ favors -= 1
                           $ physics_test_passed = True
                           $ persistent.tests_done += 1
                           $ day += 1
                           play main "School_theme.wav" volume 0.45
                           jump day2
                        elif answer.lower() == "joule":
                           bob "Correct!"
                           tr "{size=-10000}{cps=*1000}Poprawna odpowiedź!{/cps}{/size}{nw}"
                           bob "Now for the last question"
                           tr "{size=-10000}{cps=*1000}Teraz, ostatnie pytanie:{/cps}{/size}{nw}"
                           bob "What is the unit of power?"
                           tr "{size=-10000}{cps=*1000}Jaka jest jednostka siły?{/cps}{/size}{nw}"
                           bob "If you want to skip this question write 'skip' as an answer"
                           tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć tą odpowiedź napisz 'skip'{/cps}{/size}{nw}"
                           $ answer = renpy.input("")
                           if answer.lower() == "watt":
                              bob "Correct, you pass!"
                              tr "{size=-10000}{cps=*1000}Poprawna odpowiedź, zdajesz!{/cps}{/size}{nw}"
                              $ physics_test_passed = True
                              $ persistent.tests_done += 1
                              $ day += 1
                              hide screen fav_counter
                              show screen fav_counter
                              play main "School_theme.wav" volume 0.45
                              jump day2
                           elif answer.lower() == "skip" and favors > 0:
                              if favors > 0:
                                    bob "You have skipped the question and lost 1 favor"
                                    tr "{size=-10000}{cps=*1000}Pominąłeś pytanie i straciłeś 1 przysługę{/cps}{/size}{nw}"
                                    $ favors -= 1
                                    $ day += 1
                                    $ physics_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    play main "School_theme.wav" volume 0.45
                                    jump day2
                              else:
                                    bob "You don't have enough favors"
                                    tr "{size=-10000}{cps=*1000}Nie masz wystarczająco przysług{/cps}{/size}{nw}"
                                    play main "School_theme.wav" volume 0.45
                                    $ day += 1
                                    jump day2
                           else:
                              bob "Incorrect, you were so close to passing! The correct answer is: Watt"
                              tr "{size=-10000}{cps=*1000}Byłeś tak blisko zdania! Poprawną odpowiedzią jest: Watt{/cps}{/size}{nw}"
                              play main "School_theme.wav" volume 0.45
                              $ day += 1
                              jump day2
                        else:
                           bob "Wrong answer. The correct answer is: Joule"
                           tr "{size=-1000}{cps=*1000} Zła odpowiedź. Poprawna odpowiedź to: Joule{/cps}{/size}{nw}"
                           $ day += 1
                           jump day2

                  else:
                   bob "Wrong answer. The correct answer is: Newton"
                   tr "{size=-1000}{cps=*1000} Zła odpowiedź. Poprawna odpowiedź to: Newton{/cps}{/size}{nw}"
                   $ day += 1
                   jump day2
               elif seed4 == 2: 
                  bob "Good luck!"
                  tr "{size=-10000}{cps=*1000}Powodzenia{/cps}{/size}{nw}"
                  bob "First question: What is the unit of distance?"
                  tr "{size=-10000}{cps=*1000}Jaka jest jednostka odległości w układzie Si{/cps}{/size}{nw}"
                  bob "If you want to skip this question write 'skip' as an answer"
                  tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                  $ answer = renpy.input("")
                  if answer.lower() == "skip" and favors > 0:
                        $ favors -= 1
                        $ physics_test_passed = True
                        $ persistent.tests_done += 1
                        $ day += 1
                        hide screen fav_counter
                        show screen fav_counter
                        play main "School_theme.wav" volume 0.45
                        jump day2
                        
                  elif answer.lower() == "meter":
                        bob "Correct!"
                        tr "{size=-10000}{cps=*1000}Dobra odpowiedź!{/cps}{/size}{nw}"
                        bob "What is the unit of time?"
                        tr "{size=-10000}{cps=*1000}Jaka jest jednostka czasu{/cps}{/size}{nw}"
                        bob "If you want to skip this question write 'skip' as an answer"
                        tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip' jako odpowiedź{/cps}{/size}{nw}"
                        $ answer = renpy.input("")
                        if answer.lower() == "skip" and favors > 0:
                           $ favors -= 1
                           $ physics_test_passed = True
                           $ persistent.tests_done += 1
                           $ day += 1
                           hide screen fav_counter
                           show screen fav_counter
                           play main "School_theme.wav" volume 0.45
                           jump day2
                        elif answer.lower() == "second":
                           bob "Correct!"
                           tr "{size=-10000}{cps=*1000}Dobra odpowiedź{/cps}{/size}{nw}"
                           bob "Now for the last question"
                           tr "{size=-10000}{cps=*1000}Teraz, ostatnie pytanie to:{/cps}{/size}{nw}"
                           bob "What is the unit of speed?"
                           tr "{size=-10000}{cps=*1000}Jaka jest jednostka prędkości{/cps}{/size}{nw}"
                           bob "If you want to skip this question write 'skip' as an answer"
                           tr "{size=-10000}{cps=*1000}Jeśli chcesz pominąć to pytanie napisz 'skip'{/cps}{/size}{nw}"
                           $ answer = renpy.input("")
                           if answer.lower() == "m/s" or answer.lower() == "mps":
                              bob "Correct, you pass!"
                              tr "{size=-10000}{cps=*1000}Dobra odpowiedź, zdajesz!{/cps}{/size}{nw}"
                              $ physics_test_passed = True
                              $ persistent.tests_done += 1
                              $ day += 1
                              
                              hide screen fav_counter
                              show screen fav_counter
                              play main "School_theme.wav" volume 0.45
                              jump day2
                           elif answer.lower() == "skip" and favors > 0:
                              if favors > 0:
                                    bob "You have skipped the question and lost 1 favor"
                                    tr "{size=-10000}{cps=*1000}Tracisz 1 przysługę{/cps}{/size}{nw}"
                                    $ favors -= 1
                                    $ day += 1
                                    $ physics_test_passed = True
                                    $ persistent.tests_done += 1
                                    hide screen fav_counter
                                    show screen fav_counter
                                    play main "School_theme.wav" volume 0.45
                                    jump day2
                              else:
                                    bob "You don't have enough favors"
                                    tr "{size=-10000}{cps=*1000}Nie masz wystarczająco przysług{/cps}{/size}{nw}"
                                    play main "School_theme.wav" volume 0.45
                                    $ day += 1
                                    jump day2
                           else:
                              bob "Incorrect, you were so close to passing! The correct answer is: m/s or mps"
                              tr "{size=-10000}{cps=*1000}Źle, byłeś tak blisko zdania! Poprawna odpowiedź to m/s albo mps{/cps}{/size}{nw}"
                              play main "School_theme.wav" volume 0.45
                              $ day += 1
                              jump day2
                        else:
                           bob "Wrong. The correct answer was: second"
                           tr "{size=-1000}{cps=*1000} Źle. Poprawną odpowiedzią jest: second{/cps}{/size}{nw}"
                           $ day += 1
                           jump day2
                  else:
                     bob "Wrong answer. The correct answer is: Meter"
                     tr "{size=-1000}{cps=*1000} Zła odpowiedź. Poprawną odpowiedzią jest: Meter{/cps}{/size}{nw}"
                     $ day += 1
                     jump day2



              elif physics_test_passed == True:
                bob "You have already passed this exam!"
                tr "{size=-10000}{cps=*1000}Już poprawiłeś ten sprawdzian!{/cps}{/size}{nw}"
                $ day += 1
                jump Corridor_straight

            
             "Go back":
               jump Corridor_straight

           else:
             bob "You have already passed all the tests i've had for you."
             tr "{size=-10000}{cps=*1000}Już poprawiłeś wszystkie testy które dla ciebię miałem.{/cps}{/size}{nw}"
             call Corridor_straight from _call_Corridor_straight_1 

          
         
          "Go inside Mr. Roberts office":
            jump school_Roberts_office
            
          "Go to the swimming pool":
            jump pool

          "Go to cafeteria":
            jump caffeteria
          "Go back":
            call school_room1 from _call_school_room1_2 
            stop test
          
   elif interacted_Robbert == False:
      hide Robbert_far
      show Robbert_closeup at right
      $ interacted_Robbert = True
      bob "Hello!"
      tr "{size=-10000}{cps=*1000}Hej!{/cps}{/size}{nw}"
      g "Hi?"
      tr "{size=-10000}{cps=*1000}Hej?{/cps}{/size}{nw}"
      bob "Miss Thompson had told me that you have to retake a few exams to pass."
      tr "{size=-10000}{cps=*1000}Panna Thomson powiedziała mi że musisz poprawić kilka testów aby zdać.{/cps}{/size}{nw}"
      bob "I'm suppost to test your physics and chemisty skills to compensate for breaking the head teachers window with a ball."
      tr "{size=-10000}{cps=*1000}Mam za zadanie przetestować twoje umiejętności z fizyki i chemii w zamian za to że rozbiłem okno gabinetu dyrektora piłką.{/cps}{/size}{nw}"
      bob "Come back later to pass your tests!"
      tr "{size=-10000}{cps=*1000}Przyjdź do mnie później żeby zdać swoje testy!{/cps}{/size}{nw}"
      call Corridor_straight from _call_Corridor_straight_2 

      



   #Label for Robertss office - sent by thompson  
   label school_Roberts_office_thompson:
       nr "Miss Thompson takes you to the Head Teachers office"
       tr "{size=-10000}{cps=*1000}Panna Thompson zabiera cię do gabinetu Dyrektora{/cps}{/size}{nw}"
       scene School_Roberts_office
       show thompson_right at left
       show Roberts at right
       with dissolve

       stop test
       stop main
       stop type_sound

       b "What did you do this time, Max?"
       tr "{size=-10000}{cps=*1000}Co zrobiłeś tym razem, Max?{/cps}{/size}{nw}"
       s "He was late to my class AGAIN, and he couldn't even answer the simpliest of questions!"
       tr "{size=-10000}{cps=*1000}ZNOWU spóźnił się na moją lekcję i nie był wstanie odpowiedzieć nawet na najprostrze pytania!{/cps}{/size}{nw}"
       s "He needs to be punished!"
       tr "{size=-10000}{cps=*1000}Musi zostać ukarany!{/cps}{/size}{nw}"
       g "I swear, It won't happen again."
       tr "{size=-10000}{cps=*1000}Obiecuję, już nigdy się to nie zdarzy.{/cps}{/size}{nw}"
       b "That's the 5th time i hear that this month."
       tr "{size=-10000}{cps=*1000}To już piąty raz kiedy to słysze w tym miesiącu.{/cps}{/size}{nw}"
       b "Eighter you improve your grades or i will fail you, and you will get expelled!"
       tr "{size=-10000}{cps=*1000}Albo poprawisz swoję oceny, albo obleję cię i zostaniesz wydalony ze szkoły!{/cps}{/size}{nw}"
       b "You have 14 days. Thats the most i can give you."
       tr "{size=-10000}{cps=*1000}Masz 14 dni. To najwięcej ile mogę ci dać{/cps}{/size}{nw}"
       g "*How am i suppost to fix my grades that quickly?*"
       tr "{size=-10000}{cps=*1000}*Jak niby mam poprawić swoje oceny tak szybko?*{/cps}{/size}{nw}"
       g "Do I have any other choice?"
       tr "{size=-10000}{cps=*1000}Mam jakiś inny wybór?{/cps}{/size}{nw}"
       b "No. Eighter grades or you fail. Good luck!"
       tr "{size=-10000}{cps=*1000}Nie. Albo oceny albo zostajesz wydalony ze szkoły. Powodzeni!{/cps}{/size}{nw}"
       nr "You exit the room and go home."
       tr "{size=-10000}{cps=*1000}Wychodzisz z pokoju i udajesz się do domu{/cps}{/size}{nw}"

       stop headmaster

       jump max_experiment
   




   #label for a simple minigame (RPS)

   label minigame:
      define random_move = renpy.random.randint(1,2)
      scene max_computer
      show max_Joy at right
      show Lily_right at left
      nr "You decide to play rock paper scisors with your sister Lilly"
      nr "You play to two of three."
      menu:
        "Choose rock":
          nr "..."
          tr "{size=-10000}{cps=*1000}...{/cps}{/size}{nw}"
          pause(0.5)
          a "Paper"
          tr "{size=-10000}{cps=*1000}Papier{/cps}{/size}{nw}"
          g "Okay, you got lucky."
          tr "{size=-10000}{cps=*1000}Ok, miałaś szczęście{/cps}{/size}{nw}"
          menu:
            "Choose rock":
              pause(0.5)
              a "Paper"
              tr "{size=-10000}{cps=*1000}Papier{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to bed early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie! {/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose paper":
              pause(0.5)
              a "Scissors"
              tr "{size=-10000}{cps=*1000}Nożyce{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose scissors":
              pause(0.5)
              a "Rock"
              tr "{size=-10000}{cps=*1000}Kamień{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2
                        
        "Choose paper":
          nr "..."
          pause(0.5)
          a "Scissors"
          g "Okay, you got lucky."  
          menu:
            "Choose rock":
              pause(0.5)
              a "Paper"
              tr "{size=-10000}{cps=*1000}Papier{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to bed early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie! {/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose paper":
              pause(0.5)
              a "Scissors"
              tr "{size=-10000}{cps=*1000}Nożyce{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose scissors":
              pause(0.5)
              a "Rock"
              tr "{size=-10000}{cps=*1000}Kamień{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2
        "Choose scissors":
          nr "..."
          pause(0.5)
          a "Rock"
          g "Okay, you got lucky."
          menu:
            "Choose rock":
              pause(0.5)
              a "Paper"
              tr "{size=-10000}{cps=*1000}Papier{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to bed early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie! {/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose paper":
              pause(0.5)
              a "Scissors"
              tr "{size=-10000}{cps=*1000}Nożyce{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2
            "Choose scissors":
              pause(0.5)
              a "Rock"
              tr "{size=-10000}{cps=*1000}Kamień{/cps}{/size}{nw}"
              g "Cheater!"
              tr "{size=-10000}{cps=*1000}Oszust!{/cps}{/size}{nw}"
              g "I'm going to be early!"
              tr "{size=-10000}{cps=*1000}Idę do łóżka wcześnie!{/cps}{/size}{nw}"
              $ day += 1
              jump day2  




   #Label for Day x
   # should've named it dayX instead of day2, but its too late to change it now lol
   label day2:
    $ bus = renpy.random.randint(1,60)
    $ tries = 0
    stop ambience
    if maths_test_passed == False or psychology_test_passed == False or history_test_passed == False or physics_test_passed == False or chemistry_test_passed == False or geography_test_passed == False:
      if day == 7:
         stop main
         stop test
         scene black with dissolve
         pause (0.5)
         show new_day with dissolve
         pause (1)
         hide new_day with dissolve
         show black with dissolve
         pause (0.5)   
         play sound "alarm.wav" volume 0.25
            
         scene Bedroom_max
         show max_Joy at right
         with dissolve
         g "Its day nr [day]"
         tr "{size=-10000}{cps=*1000}Jest dzień nr [day]{/cps}{/size}{nw}"
         g "Finally, a day off."
         tr "{size=-10000}{cps=*1000}Nareszcie, dzień wolnego.{/cps}{/size}{nw}"
         g "What should i do today..."
         tr "{size=-10000}{cps=*1000}Co powinienem dzisiaj zrobić?{/cps}{/size}{nw}"
         nr "What do you want to do today?"
         tr "{size=-10000}{cps=*1000}Co chciałbys dzisiaj zrobić?{/cps}{/size}{nw}"
         menu: 
            
            "Watch TV":
               scene max_tv with dissolve
               nr "You watch the TV all day"
               tr "{size=-10000}{cps=*1000}Oglądasz telewizję cały dzień{/cps}{/size}{nw}"
               $ day += 1
               jump day2
               

            "Play with Lilly":
               scene max_computer with dissolve
               jump minigame
            
            "Go to sleep":
               nr "You sleep all day long after a week of hard work."  
               tr "{size=-10000}{cps=*1000}Przesypiasz cały dzień po ciężkim tygodniu pracy.{/cps}{/size}{nw}"
               $ day+= 1
               jump day2
      elif day < 7 or day > 7 and day != 14:

         stop main
         stop test
         
         scene black with dissolve
         pause (0.5)
         show new_day with dissolve
         pause (1)
         hide new_day with dissolve
         show black with dissolve
         pause (0.5)

         play sound "alarm.wav" volume 0.25
         play day2 "day2.mp3" volume 0.35
         scene Bedroom_max
         show max_Joy at right
         with dissolve
         g "Its day nr [day]"
         tr "{size=-10000}{cps=*1000}Jest dzień nr [day]{/cps}{/size}{nw}"

         menu:
               "Go to the living room.":
                 jump salon_empty

               "Go back to sleep":
                  nr "Are you sure you want to waste time instead of retaking your tests?"
                  tr "{size=-10000}{cps=*1000}Jesteś pewien że chcesz marnować swój czas zamiast poprawiać testów?{/cps}{/size}{nw}"
                  menu:
                     "Yes, i am sure":
                       nr "Alright, you do you."
                       tr "{size=-10000}{cps=*1000}Ok, rób co chcesz{/cps}{/size}{nw}"
                       nr "You waste time laying in bed all day."
                       tr "{size=-10000}{cps=*1000}Marnujesz cały dzień leżąc w łóźku{/cps}{/size}{nw}"
                       $ day += 1
                       stop day2
                       jump day2
                     "No":
                       nr "Good choice"
                       tr "{size=-10000}{cps=*1000}Dobry wybór{/cps}{/size}{nw}"
                       nr "You go downstairs"
                       tr "{size=-10000}{cps=*1000}Schodzisz po schodach{/cps}{/size}{nw}"
                       jump salon_empty
      
      elif day == 14:
         stop main
         stop test
         scene black with dissolve
         pause (0.5)
         show new_day with dissolve
         pause (1)
         hide new_day with dissolve
         show black with dissolve
         pause (0.5)   
         play sound "alarm.wav" volume 0.25
            
         scene Bedroom_max
         show max_Joy at right
         with dissolve
         g "Its day nr [day]"

         play stress "stress.wav" volume 0.65
         n "I got a call from school, you need to go to Mr. Roberts office as soon as possible."
         tr "{size=-10000}{cps=*1000}Dostałam telefon ze szkoły, musisz iść do Pana Robertsa jak szybko jak to tylko możliwe{/cps}{/size}{nw}"
         g "Oh no..."
         tr "{size=-10000}{cps=*1000}O nie...{/cps}{/size}{nw}"
         jump bad_ending
    else:
      stop main
      stop test
      play day2 "day2.mp3" volume 0.35
      scene Bedroom_max
      show Sarah_Joy at left
      show max_Joy at right
      with dissolve

      n "Hey Max!"
      tr "{size=-10000}{cps=*1000}Hej Max!{/cps}{/size}{nw}"
      n "I got a call from Principal Roberts. He want to talk to you, so you should hurry up and go to his office."
      tr "{size=-10000}{cps=*1000}Dostałam telefon on Dyrektora Robertsa. Chcesz z tobą porozmawiać, więc powinieneś się pospieszyć i iść do jego biura.{/cps}{/size}{nw}"
      g "Alright mom!"
      tr "{size=-10000}{cps=*1000}Ok mamo!{/cps}{/size}{nw}"
      jump good_ending
        
   label good_ending:
      scene School_Roberts_office
      show Roberts at right
      with dissolve
      b "Congratulations, Max!"
      tr "{size=-10000}{cps=*1000}Gratulacje Max!{/cps}{/size}{nw}"
      b "You've done it."
      tr "{size=-10000}{cps=*1000}Udało ci się!{/cps}{/size}{nw}"
      b "You will pass to the next grade!"
      tr "{size=-10000}{cps=*1000}Zdajesz do następnej klasy!{/cps}{/size}{nw}"
      g "Thank you so much!"
      tr "{size=-10000}{cps=*1000}Bardzo dziękuję!{/cps}{/size}{nw}"
      b "Good job. Don't make the same mistake next year."
      tr "{size=-10000}{cps=*1000}Dobra robota. Nie popełnij tego samego błędu za rok.{/cps}{/size}{nw}"
      g "You can be sure of that, principal!"
      tr "{size=-10000}{cps=*1000}Możesz być tego pewny, dyrektorze!{/cps}{/size}{nw}"
      g "Goodbye!"
      tr "{size=-10000}{cps=*1000}Do widzenia!{/cps}{/size}{nw}"
      b "Goodbye, Max."
      tr "{size=-10000}{cps=*1000}Do wiedzenia, Max.{/cps}{/size}{nw}"
      hide Roberts
      with dissolve
      stop day2
      play endings "good_ending.mp3"
      scene House_Backyard_3 with dissolve
      nr "Your job here is done."
      tr "{size=-10000}{cps=*1000}Twoja rola jest skończona{/cps}{/size}{nw}"
      nr "You can now go back to your normal life."
      tr "{size=-10000}{cps=*1000}Możesz teraz wrócić do swojego normalnego życia.{/cps}{/size}{nw}"
      nr "Would you like to be removed from Max's brain and continue your normal life?"
      tr "{size=-10000}{cps=*1000}Czy chciałbyś zostać usunięty z mózgu Maxa i wrócić do swojego normalnego życia?{/cps}{/size}{nw}"

      menu:
       
       "Yes, I want to get back to my normal life":
         nr "You will now get removed from Max's body and come to your normal life. Thank you for your help :)"
         tr "{size=-10000}{cps=*1000}Teraz zostaniesz usunięty z mózgu Maxa i wrócisz do swojego normalnego życia :){/cps}{/size}{nw}"
         stop day2
         show good_ending
         with fade
         while persistent.true_good_ending == False:
            $ persistent.true_good_ending = True
            call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'The true good ending' ")
         pause (9999)
         nr "The game will now shutdown, its not a crash."
         $ renpy.quit()

       "No, I want to stay in Max's body":
         stop endings
         nr "His soul is going to wander the world for all eternity without its body because of you..."
         tr "{size=-10000}{cps=*1000}Jego dusz będzię się błąkać po świecie przez całą nieskończonością bez ciała przez ciebię...{cps=*1000}{/cps}{/size}{nw}"
         nr "But who am I to question your decisions?"
         tr "{size=-10000}{cps=*1000}Ale kim ja niby jestem aby kwestjonować twoje decyzję? {/cps}{/size}{nw}"
         nr "You've made a choice, witch you can't take back."
         tr "{size=-10000}{cps=*1000}Podjąłeś decyzję której nie możesz już cofnąć.{/cps}{/size}{nw}"
         stop day2
         scene neutral_ending
         with fade
         while persistent.good_ending == False:
            $ persistent.good_ending = True
            call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'The good ending?' ")
         pause (999)
         g "Have I made the right decision...?"
         tr "{size=-10000}{cps=*1000}Czy napewno podjąłem dobrą decyzję...?{/cps}{/size}{nw}"
         pause (5)
         nr "The game will now shutdown, its not a crash."
         $ renpy.quit()


   label bad_ending:
      
      scene School_Roberts_office
      show Roberts at right
      with dissolve
      b "The 14 days I gave you are up."
      tr "{size=-10000}{cps=*1000}14 dni które odemnie dostałej upłyneły.{/cps}{/size}{nw}"
      b "I'm quite dissapointed. I really didn't think you'd struggle that much with basic tests."
      tr "{size=-10000}{cps=*1000}Jestem dosyć zawiedziony. Naprawdę nie myślałem że będziesz miał taki duży problem z najprostrzymi testami.{/cps}{/size}{nw}"
      b "Well, enought said."
      tr "{size=-10000}{cps=*1000}Wystarczająco dużo już powiedziałem{/cps}{/size}{nw}"
      b "You fail. You are expelled."
      tr "{size=-10000}{cps=*1000}Nie zdajesz. Zostajesz wydalony ze szkoły.{/cps}{/size}{nw}"
      stop stress
      play endings "bad_ending.mp3" volume 0.55
      scene House_Backyard_3 with dissolve
      g "Well, i guess that's it..."
      tr "{size=-10000}{cps=*1000}No więc, to chyba tyle...{/cps}{/size}{nw}"
      nr "Would you like to try again?"
      tr "{size=-10000}{cps=*1000}Chciałbyś spróbować ponownie?{/cps}{/size}{nw}"
      menu:
       "Yes, please!":
            stop endings
            scene white with hpunch
            play transformation "transformation.mp3"
            $ seed1 = renpy.random.randint(1,2)
            $ seed2 = renpy.random.randint(1,2)
            $ seed3 = renpy.random.randint(1,2)
            $ seed4 = renpy.random.randint(1,2)
            jump start

       "No, I'm fine with being expelled.":
            nr "Bad choice but who am I to decide..."
            tr "{size=-10000}{cps=*1000}Zła decyzja ale kim ja niby jestem żeby decydować./cps}{/size}{nw}"
            show bad_ending_screen 
            with fade
            while persistent.bad_ending == False:
               $ persistent.bad_ending = True
               call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'The bad ending' ")
            pause (9999)
            nr "The game will be shutdown, its not a crash."
            $ renpy.quit()

   #max room empty (For movement)

   label max_room_empty:
      scene Bedroom_max
      with dissolve
   menu:
      "Go to the living room.":
         jump salon_empty

      "Go back to sleep":
         nr "Are you sure you want to waste time instead of retaking your tests?"
         tr "{size=-10000}{cps=*1000}Jesteś pewny że wolisz marnować swój czas zamiast poprawiać testy? {/cps}{/size}{nw}"
         menu:
            "Yes, i am sure":
               nr "Alright, you do you."
               tr "{size=-10000}{cps=*1000}Ok, twoja decyzja.{/cps}{/size}{nw}"
               nr "You waste time laying in bed all day."
               tr "{size=-10000}{cps=*1000}Marnujesz swój czas leżąc w łóżku cały dzień{/cps}{/size}{nw}"
               $ day += 1
               jump day2
            "No":
               nr "Good choice"
               tr "{size=-10000}{cps=*1000}Dobry wybór{/cps}{/size}{nw}"
               nr "You go downstairs"
               tr "{size=-10000}{cps=*1000}Schodzisz po schodach na dół{/cps}{/size}{nw}"
               jump salon_empty


   #label for pool

   label pool:
      stop test
      scene poolroom
      with dissolve

   menu:
      "Go back":
         call Corridor_straight from _call_Corridor_straight_3 


   #label for cafeteria
   label caffeteria:
      stop test
      scene school_cafeteria
      show Lesie at left
      with dissolve
   menu:
      "Go back":
         call Corridor_straight from _call_Corridor_straight_4 
      "Talk to Lessie":
         l "Hey."
         g "Hello."
   if Lesie_started == False and Lesie_completed == False:
         l "Could you give this letter to Robbert? I have a huge crush on him and i want him to see it."
         tr "{size=-10000}{cps=*1000}Mógłbyś dać ten list Robbertowi? Mam na nim wielkiego crusha, i chciałabym żeby to zobaczył.{/cps}{/size}{nw}"
         menu: 
          "Sure thing!":
             $ Lesie_started = True
             $ Lesie_completed = False
             jump Corridor_straight
          "Don't have time for it, sorry":
             jump Corridor_straight
   elif Lesie_started == True and Lesie_completed == False:
         l "Did you give it to Robbert yet?"
         tr "{size=-10000}{cps=*1000}Dałeś już go Robbertowi?{/cps}{/size}{nw}"
         jump Corridor_straight
   elif Lesie_started == True and Lesie_completed == True:
         l "Thank you so much! I will make this up for you."
         tr "{size=-10000}{cps=*1000}Bardzo ci dziękuję! Odwdzięcze ci się.{/cps}{/size}{nw}"
         
         if favor_Lesie == False:
            $ favors += 1
            $ favor_Lesie = True
            nr "You get a favor!"
            tr "{size=-10000}{cps=*1000}Zdobywasz przyługę.{/cps}{/size}{nw}"
            while persistent.achievement_love_birds == False:
               $ persistent.achievement_love_birds = True
               call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'Love birds' ")
            jump Corridor_straight
         elif favor_Lesie == True:
            jump Corridor_straight


   #label for empty living room.
   label salon_empty:
      scene salon
      with dissolve
      "Your mother went to work, the house is empty."
      tr "{size=-10000}{cps=*1000}Twoja mama poszła do pracy, twój dom jest pusty.{/cps}{/size}{nw}"
   menu:
          "Go outside":
             stop day2
             play ambience "ambience_birds.mp3" volume 0.45
             jump porch
             

          "Go back to your room":
            jump max_room_empty
            


   label porch:
         scene max_porch
         with dissolve
   menu: 
        "Go to school":
         if (bus % 2) == 0  and bus != 15:
            scene bus1
            with dissolve
            pause (1)
            jump school_entrance
         elif (bus % 2) != 0  and bus != 15:
            scene bus2
            with dissolve
            pause (1)
            jump school_entrance
         elif bus == 15:     
            if persistent.bus_easteregg == False:
               call screen GameGuide("You have unlocked an achievement! \n The achievement you've got is: \n 'A normal bus?' ")
               $ persistent.bus_easteregg = True
               
               scene bus3
               with dissolve
               pause(1)
               jump school_entrance
            else: 
               scene bus1
               with dissolve
               pause(1)
               jump school_entrance
            
        "Go back inside":
            stop ambience
            play day2 "day2.mp3" volume 0.35
            jump salon_empty

   menu:
         "Do you want to go back to school?"
         "Yes":
              jump school_entrance

         "No":
              "You will get in trouble, but you do you..."
              jump salon_empty


   label max_experiment:
      play stress "stress.wav" volume 0.65
      scene Bedroom_max_Night
      show Lily_night at right
      show max_night at left
      with dissolve
      g "Lilly, please help me."
      tr "{size=-10000}{cps=*1000}Lilly, prosze pomóż mi.{/cps}{/size}{nw}"
      g "I have to retake all my exams or I will get expelled!"
      tr "{size=-10000}{cps=*1000}Muszę poprawić wszystkie swoje testy albo zostanę wyrzucony ze szkoły!{/cps}{/size}{nw}"
      a "You what!?"
      tr "{size=-10000}{cps=*1000}Co zrobiłeś!?{/cps}{/size}{nw}"
      a "Alright, we musn't panic. I know how to get your out of this mess."
      tr "{size=-10000}{cps=*1000}Ok nie możemy panikować. Wiem jak cię z tego wyciągnąć{/cps}{/size}{nw}"
      g "What do you mean?"
      tr "{size=-10000}{cps=*1000}Co masz na myśli?{/cps}{/size}{nw}"
      a "You will see..."
      tr "{size=-10000}{cps=*1000}Zobaczysz...{/cps}{/size}{nw}"
      
      hide Lily_night
      hide max_night
      show Lily_Experiment_On_max at right
      with dissolve
      a "Don't move. It won't hurt."
      tr "{size=-10000}{cps=*1000}Nie ruszaj się. Nie będzie bolało.{/cps}{/size}{nw}"
      hide Lily_Experiment_On_max with dissolve
      stop stress
      play transformation "transformation.mp3"
      show white with hpunch
      pause (1)
      hide white 
      show Lily_night at right
      show max_night at left
      with dissolve
      a "It worked!"
      tr "{size=-10000}{cps=*1000}Zadziałało!{/cps}{/size}{nw}"
      nr "You, player are now in the mind of Max Wilder! \nYou must help him retake all of his tests and make sure he passes."
      tr "{size=-10000}{cps=*1000}Ty, gracz jesteś teraz w ciele Maxa Wildera! \nMusisz pomódz mu zdać wszystkie jego testy i upewnić się że zda do następnej klasy{/cps}{/size}{nw}"
      nr "Good luck!"
      tr "{size=-10000}{cps=*1000}Powodzenia{/cps}{/size}{nw}"
      a "You should go to sleep, you are propably exhausted."
      tr "{size=-10000}{cps=*1000}Powinieneś iść spać, jesteś pewnie wykończony.{/cps}{/size}{nw}"
      nr "You go to sleep"
      tr "{size=-10000}{cps=*1000}Idziesz do snu.{/cps}{/size}{nw}"
      $ day += 1
      jump day2


      




label splashscreen:
   scene black with dissolve
   pause (1)
   show studio_logo with dissolve
   pause (2)
   hide studio_logo with dissolve
   show black with dissolve
   pause (1)
   
   return
