def Travel_Assist():
    print("Hello,How can i help you?")
    
    while True:
        user_input = input("You:").upper()
        
        if user_input in["HI"]:
            print("Travel_Assist:Hello!")
        
        elif user_input in["BEST PLACES IN BANGLORE"]:
            print("Travel_Assist:\nwhich type of places you like to visit.\n1.Museum\n2.Amusement Park\n3.Temples\n4.zoo & Gardens\n5.Hill Stations\n6.Restaurants\n7.Cafes")
            
            
        elif user_input in["MUSEUM"]:
            print("Travel_Assist:\nVisvesvaraya Industrial & Technological Museum \nGovernment Museum\nHAL Heritage Centre and Aerospace Museum\nKarnataka Chitrakala Parishath\nVenkatappa Art Gallery")
            
        elif user_input in["AMUSEMENT PARK"]:
            print("Travel_Assist:\nFun World Amusement Park\nWonderla Amusement Park\nFantacy Park\nClub Cabana Amusement Park")
        
        elif user_input in["TEMPLES"]:
            print("Travel_Assist:\nISKCON temple\nShrungagiri Sri Shanmukha Swami Gudi\nShri Gavi Gangadhareshwara Swamy Temple\nSri Rajarajeshwari Temple\nSri Dakshinamukha Nandi Tirtha Kalyaani Kshetra\nShri Kadu Mallikarjuna Swamy Temple\nShri Bande Mahakali Temple (Moola udbhava Devi).")
            
        elif user_input in["ZOO & GARDENS"]:
            print("Tavel_Assist:\nBannerghatta zoo\nButterfly Park\nRangoli Garden\nCubbon Park\nLalbagh Botanical Garden\nMahathmaGandhi Botanical Garden")
            
        elif user_input in["HILL STATIONS"]:
            print("Travel_Assist:\nSavandurga\nAntargange\nNandi Hills\nMakalidurga\nMadhugiri\nMullayangiri Peak")
            
        elif user_input in["RESTAURANTS"]:
            print("Travel_Assist:\nVeg\nNon Veg")
            
        elif user_input in["VEG"]:
            print("Travel_Assist:\nSattvam Restaurant\nThe Higher Taste Restaurant\nStreet Storyss\nKonark Vegetarian Restaurant\n Green Theory\n Gramin | Veg Restaurant")
            
        elif user_input in["NON VEG"]:
            print("Travel_Assist:\nEmpire Restaurant\nKarama Restaurant\nMeghana Foods\nShivaji Restaurant\nRK's Family Restaurant\nTasty Paradise\nBarbeque Nation\nImperial Restaurant")
            
        elif user_input in["CAFES"]:
            print("Travel_Assist:\nThe illusion Cafe\nDyu Art Cafe\nThe Hole In The Wall Cafe\nThe Bangalore Cafe\nHard Rock Cafe")
            
        elif user_input in["THANK YOU"]:
            print("Travel_Assist:\nThank you have a nice day!")
            
        else:
            print("Travel_Assist:I'm not sure how to respond to this")
            
Travel_Assist()
