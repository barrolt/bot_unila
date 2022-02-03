# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import sqlite3
import random
import smtplib

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionAmbilNPM(Action):

    def name(self) -> Text:
        return "action_ambil_NPM"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = Db.create_connection(db_file="bot_unila.db")

        slot_value3 = tracker.get_slot("npm_slot")   
        #slot_value2 = next(tracker.get_latest_entity_values("email_mahasiswa_slot"), None)
        #dispatcher.utter_message(text=str(slot_value2))
        #slot_name = "Type"

        get_query_result = Db.select_by_npm(conn=conn,
                slot_value3=slot_value3)
        #dispatcher.utter_message(text=str(get_query_results))
    
        if get_query_result == 1:
            dispatcher.utter_message(response='utter_input_email') 
        else:
            dispatcher.utter_message(response='utter_gagal_npm')
        return



class Db:
    def create_connection(db_file):

        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def select_by_npm(conn,slot_value3):
        cur = conn.cursor()
        
        cur3 = conn.cursor()
        cur4 = conn.cursor()
        cur52 = conn.cursor()
        cur6 = conn.cursor()
        
        cur8 = conn.cursor()

        #cur3.execute("SELECT email FROM mahasiswa")
        cur52.execute("SELECT nip FROM tendik")

        #dataMahasiswa = cur3.fetchall()
        dataTendik2 = cur52.fetchall()

        print (slot_value3)

        x = str(slot_value3)

        for nt in dataTendik2:
            y = str(nt)
            print (nt)
            if x in y:
                cur6.execute(f"""select * from tendik where 
                        nip='{slot_value3}' """)
 
                return 1
                
 

class ActionRememberNpm(Action):

    def name(self) -> Text:
        return "action_remember_npm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_npm = next(tracker.get_latest_entity_values("npm"), None)
                
        #msg = f"Sure thing! I'll remember you NPM {current_npm}."
        #dispatcher.utter_message(text=msg)
        
        return [SlotSet("npm_slot", current_npm)]

class ActionAmbilData(Action):

    def name(self) -> Text:
        return "action_ambil_data"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = DbQueryingMethods.create_connection(db_file="bot_unila.db")

        slot_value = tracker.get_slot("npm_slot")   
        #slot_value2 = next(tracker.get_latest_entity_values("email_mahasiswa_slot"), None)
        slot_value2 = tracker.latest_message['text']
        
        #dispatcher.utter_message(text=str(slot_value2))
        #slot_name = "Type"

        get_query_results = DbQueryingMethods.select_by_slot(conn=conn,
                slot_value=slot_value,slot_value2=slot_value2)
        #dispatcher.utter_message(text=str(get_query_results))
    
        if get_query_results == 1:
            dispatcher.utter_message(response='utter_balasan') 
        else:
            dispatcher.utter_message(response='utter_gagal')
        return



class DbQueryingMethods:
    def create_connection(db_file):

        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def select_by_slot(conn,slot_value,slot_value2):
        cur = conn.cursor()
        
        cur3 = conn.cursor()
        cur4 = conn.cursor()
        cur5 = conn.cursor()
        cur6 = conn.cursor()
        
        cur8 = conn.cursor()

        #cur3.execute("SELECT email FROM mahasiswa")
        cur5.execute("SELECT email FROM tendik")

        #dataMahasiswa = cur3.fetchall()
        dataTendik = cur5.fetchall()

        print (slot_value)
        print (slot_value2)

        tuple(slot_value2)

        for emailPersonal in dataTendik:
            print (emailPersonal)
            if slot_value2 in emailPersonal:
                cur6.execute(f"""select * from tendik where 
                        email='{slot_value2}' """)
                
                dataKolomTendik = cur6.fetchall() 

                for j in dataKolomTendik:
                    nip=str(j[0])
                    emailTendik=str(j[2])
    
                if ((slot_value==nip) and (slot_value2==emailTendik)):
                    cur8.execute(f"""select * from tendik where
                            email='{slot_value2}' and nip='{slot_value}' """)
                    rowsTendik = cur8.fetchall()
                    for rowT in rowsTendik:

                        user_name = rowT[1]
                        email_id = rowT[2]
          
                        # Code to send email
                        # Creating connection using smtplib module
                        s = smtplib.SMTP('smtp.gmail.com',587)
          
                        # Making connection secured
                        s.starttls() 
          
                        # Authentication
                        s.login("syauqi.joke@gmail.com", "mezquillacordoba")
          
                        # Message to be sent
                        message = "Hello {} , This is a demo message".format(user_name)
          
                        # Sending the mail
                        s.sendmail("syauqi.joke@gmail.com",email_id, message)
          
                        # Closing the connection
                        s.quit()
          
                        # Confirmation message
                        
                        return 1
                
        print ("selesai seluruh for")


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
