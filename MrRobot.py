# Coded by Shaydy

import json
import requests
import time
import os
import phonenumbers
import socket
import threading
from queue import Queue
from phonenumbers import carrier, geocoder, timezone
from ip2geotools.databases.noncommercial import DbIpCity
from sys import stderr, modules
from colorama import init, Fore, Back, Style

init()

def main():
    os.system( "cls" )
    stderr.writelines( f"""{ Style.BRIGHT }{ Fore.RED }
        ███╗   ███╗██████╗   ██████╗  █████╗ ██████╗  █████╗ ████████╗
        ████╗ ████║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
        ██╔████╔██║██████╔╝  ██████╔╝██║  ██║██████╦╝██║  ██║   ██║
        ██║╚██╔╝██║██╔══██╗  ██╔══██╗██║  ██║██╔══██╗██║  ██║   ██║
        ██║ ╚═╝ ██║██║  ██║  ██║  ██║╚█████╔╝██████╦╝╚█████╔╝   ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═╝  ╚═╝ ╚════╝ ╚═════╝  ╚════╝    ╚═╝

                            By Shaydy{ Fore.RESET }          
            
            { Style.BRIGHT }{ Fore.WHITE }[1]{ Fore.RESET }{ Fore.GREEN } IP Tracker{ Fore.RESET }
            { Fore.WHITE }[2]{ Fore.RESET }{ Fore.GREEN } Show Your IP{ Fore.RESET }
            { Fore.WHITE }[3]{ Fore.WHITE }{ Fore.GREEN } Phone Tracker{ Fore.RESET }
            { Fore.WHITE }[4]{ Fore.WHITE }{ Fore.GREEN } Username Tracker{ Fore.RESET }
            { Fore.WHITE }[5]{ Fore.WHITE }{ Fore.GREEN } Port Scanner{ Fore.RESET }
            { Fore.WHITE }[0]{ Fore.WHITE }{ Fore.GREEN } Exit{ Fore.RESET }{ Style.RESET_ALL }
    """)

    input_user = input( f"\n  { Style.BRIGHT }{ Fore.BLUE }@Elliot~# { Fore.RESET }{ Style.RESET_ALL }" )

    if input_user == "1":
        os.system( "cls" )
        time.sleep( 1 )
        stderr.writelines( f"""{ Style.BRIGHT }{ Fore.WHITE }
                    |--------------------------------|
                    |            { Fore.RED }MR ROBOT{ Fore.RESET }            |
                    |--------------------------------|{ Style.RESET_ALL }

        """)

        try:
            def resolve_city( ip ):
                response = DbIpCity.get( ip, api_key="free" )
                return response.city

            def resolve_country( ip ):
                response = DbIpCity.get( ip, api_key="free" )
                return response.country

            def IP_Track():
                ip = input( f"{ Style.BRIGHT }{ Fore.WHITE }\n Enter IP target{ Fore.RESET } : { Fore.RED }" )
                city = resolve_city( ip )
                country = resolve_country( ip )
                print( f"{ Fore.RESET }{ Style.RESET_ALL }" )
                print( f" { Style.BRIGHT }{ Fore.GREEN }============= { Fore.RESET }{ Fore.RED }INFORMATION IP ADDRESS { Fore.RESET }{ Fore.GREEN }============={ Fore.RESET }{ Style.RESET_ALL }" )
                req_api = requests.get( f"http://ipwho.is/{ ip }" )
                ip_data = json.loads( req_api.text )
                time.sleep( 1 )
                print( f"{ Style.BRIGHT }{  Fore.WHITE  }\n IP target       :{  Fore.RESET  }", ip )
                print( f"{  Fore.WHITE  } Type IP         :{  Fore.RESET  }", ip_data[ "type" ] )
                print( f"{  Fore.WHITE  } Country         :{  Fore.RESET  }", ip_data[ "country" ] )
                print( f"{  Fore.WHITE  } Country Code    :{  Fore.RESET  }", ip_data[ "country_code" ] )
                print( f"{  Fore.WHITE  } City            :{  Fore.RESET  }", ip_data[ "city" ] )
                print( f"{  Fore.WHITE  } Continent       :{  Fore.RESET  }", ip_data[ "continent" ] )
                print( f"{  Fore.WHITE  } Continent Code  :{  Fore.RESET  }", ip_data[ "continent_code" ] )
                print( f"{  Fore.WHITE  } Region          :{  Fore.RESET  }", ip_data[ "region" ] )
                print( f"{  Fore.WHITE  } Region Code     :{  Fore.RESET  }", ip_data[ "region_code" ] )
                print( f"{  Fore.WHITE  } Latitude        :{  Fore.RESET  }", ip_data[ "latitude" ] )
                print( f"{  Fore.WHITE  } Longitude       :{  Fore.RESET  }", ip_data[ "longitude" ] )
                lat = int( ip_data[ "latitude" ] )
                lon = int( ip_data[ "longitude" ] )
                print( f"{ Fore.WHITE } Maps            :{ Fore.RESET }", f"https://www.google.com/maps/@{ lat },{ lon },8z" )
                print( f"{ Fore.WHITE } EU              :{ Fore.RESET }", ip_data[ "is_eu" ] )
                print( f"{ Fore.WHITE } Postal          :{ Fore.RESET }", ip_data[ "postal" ] )
                print( f"{ Fore.WHITE } Calling Code    :{ Fore.RESET }", ip_data[ "calling_code" ] )
                print( f"{ Fore.WHITE } Capital         :{ Fore.RESET }", ip_data[ "capital" ] )
                print( f"{ Fore.WHITE } Borders         :{ Fore.RESET }", ip_data[ "borders" ] )
                print( f"{ Fore.WHITE } Country Flag    :{ Fore.RESET }", ip_data[ "flag" ][ "emoji" ] )
                print( f"{ Fore.WHITE } ASN             :{ Fore.RESET }", ip_data[ "connection" ][ "asn" ] )
                print( f"{ Fore.WHITE } ORG             :{ Fore.RESET }", ip_data[ "connection" ][ "org" ] )
                print( f"{ Fore.WHITE } ISP             :{ Fore.RESET }", ip_data[ "connection" ][ "isp" ] )
                print( f"{ Fore.WHITE } Domain          :{ Fore.RESET }", ip_data[ "connection" ][ "domain" ] )
                print( f"{ Fore.WHITE } ID              :{ Fore.RESET }", ip_data[ "timezone" ][ "id" ] )
                print( f"{ Fore.WHITE } ABBR            :{ Fore.RESET }", ip_data[ "timezone" ][ "abbr" ] )
                print( f"{ Fore.WHITE } DST             :{ Fore.RESET }", ip_data[ "timezone" ][ "is_dst" ] )
                print( f"{ Fore.WHITE } Offset          :{ Fore.RESET }", ip_data[ "timezone" ][ "offset" ] )
                print( f"{ Fore.WHITE } UTC             :{ Fore.RESET }", ip_data[ "timezone" ][ "utc" ] )
                print( f"{ Fore.WHITE } Current Time    :{ Fore.RESET }{ Style.RESET_ALL }", ip_data[ "timezone" ][ "current_time" ] )
                print( f"\n   ======== Other Info ========" )
                print( f"{ Fore.WHITE }     City : { city }" )
                print( f"{ Fore.WHITE }     Country : { country }" )

            if __name__ == "__main__":
                IP_Track()

        except KeyError:
            print( f"   { Style.BRIGHT }{ Fore.RED }Check you ip!{ Fore.RESET }{ Style.RESET_ALL }" )

        except KeyboardInterrupt:
            print( f" { Style.BRIGHT }\n{ Fore.RED }[!] PROGRAM STOPPED.{ Fore.RESET }{ Style.RESET_ALL }" )

        input( f"{ Fore.RED }Press Enter{ Fore.RESET }" )
        main()

    elif input_user == "2":
        os.system( "cls" )
        time.sleep( 1 )
        stderr.writelines( f"""{ Style.BRIGHT }{ Fore.WHITE }
                    |--------------------------------|
                    |            { Fore.RED }MR ROBOT{ Fore.RESET }            |
                    |--------------------------------|{ Style.RESET_ALL }
            
        """)

        try:
            def showIP():
                respone = requests.get( "https://api.ipify.org/" )
                Show_IP = respone.text
                
                print( f"\n { Style.BRIGHT }{ Fore.WHITE }=========={ Fore.RESET } { Fore.GREEN }SHOW INFORMATION YOUR IP { Fore.RESET }{ Fore.WHITE }=========={ Fore.RESET }" )
                print( f"\n { Fore.RED }[+]{ Fore.RESET } { Fore.WHITE }Your IP Adrress : { Fore.RESET }{ Fore.RED }{ Show_IP }{ Fore.RESET }" )
                print( f"\n { Fore.WHITE }=============================================={ Fore.RESET }{ Style.RESET_ALL }" )

            if __name__ == "__main__":
                showIP()

        except KeyboardInterrupt:
            print( f" \n{ Style.BRIGHT }{ Fore.RED }[!] PROGRAM STOPPED.{ Fore.RESET }{ Style.RESET_ALL }" )

        input( f"{ Fore.RED }Press Enter{ Fore.RESET }" )
        main()

    elif input_user == "3":
        os.system( "cls" )
        time.sleep( 1 )
        stderr.writelines( f"""{ Style.BRIGHT }{ Fore.WHITE }
                    |--------------------------------|
                    |            { Fore.RED }MR ROBOT{ Fore.RESET }            |
                    |--------------------------------|{ Style.RESET_ALL }
            
        """)

        try:
            def phoneGW():
                User_phone = input( f"\n { Style.BRIGHT }{ Fore.YELLOW }Enter phone number target { Fore.RESET }Example: { Fore.YELLOW }+7925xxxxxxxxx{ Fore.RESET }: { Fore.RED }" )
                default_region = "ID"

                parsed_number = phonenumbers.parse( User_phone, default_region )
                region_code = phonenumbers.region_code_for_number( parsed_number )
                jenis_provider = carrier.name_for_number( parsed_number, "en" )
                location = geocoder.description_for_number( parsed_number, "id" )
                is_valid_number = phonenumbers.is_valid_number( parsed_number )
                is_possible_number = phonenumbers.is_possible_number( parsed_number )
                formatted_number = phonenumbers.format_number( parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL )
                formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing( parsed_number, default_region, with_formatting=True )
                number_type = phonenumbers.number_type( parsed_number )
                timezone1 = timezone.time_zones_for_number( parsed_number )
                timezoneF = ', '.join( timezone1 )

                print( f"\n { Fore.RED }=========={ Fore.RESET } { Fore.GREEN }SHOW INFORMATION PHONE NUMBERS{ Fore.RESET } { Fore.RED }=========={ Fore.RESET }" )
                print( f"\n { Fore.WHITE }Location             { Fore.RESET }:{ Fore.GREEN } { location }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Region Code          { Fore.RESET }:{ Fore.GREEN } { region_code }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Timezone             { Fore.RESET }:{ Fore.GREEN } { timezoneF }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Operator             { Fore.RESET }:{ Fore.GREEN } { jenis_provider }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Valid number         { Fore.RESET }:{ Fore.GREEN } { is_valid_number }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Possible number      { Fore.RESET }:{ Fore.GREEN } { is_possible_number }{ Fore.RESET }" )
                print( f" { Fore.WHITE }International format { Fore.RESET }:{ Fore.GREEN } { formatted_number }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Mobile format        { Fore.RESET }:{ Fore.GREEN } { formatted_number_for_mobile }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Original number      { Fore.RESET }:{ Fore.GREEN } { parsed_number.national_number }{ Fore.RESET }" )
                print( f" { Fore.WHITE }E.164 format         { Fore.RESET }:{ Fore.GREEN } { phonenumbers.format_number( parsed_number, phonenumbers.PhoneNumberFormat.E164 ) }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Country code         { Fore.RESET }:{ Fore.GREEN } { parsed_number.country_code }{ Fore.RESET }" )
                print( f" { Fore.WHITE }Local number         { Fore.RESET }:{ Fore.GREEN } { parsed_number.national_number }{ Fore.RESET }{ Style.RESET_ALL }" )

                if number_type == phonenumbers.PhoneNumberType.MOBILE:
                    print( f"   This is a mobile number" )
                elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                    print( f"   This is a fixed-line number" )
                else:
                    print( f"   This is another type of number")

            if __name__ == "__main__":
                phoneGW()

        except KeyboardInterrupt:
            print( f" \n{ Fore.RED }[!] PROGRAM STOPPED.{ Fore.RESET }" )

        input( f"{ Fore.RED }Press Enter{ Fore.RESET }" )
        main()

    elif input_user == "4":
        os.system( "cls" )
        time.sleep( 1 )
        stderr.writelines( f"""{ Style.BRIGHT }{ Fore.WHITE }
                    |--------------------------------|
                    |            { Fore.RED }MR ROBOT{ Fore.RESET }            |
                    |--------------------------------|{ Style.RESET_ALL }
                
        """)
        try:
            def TrackLu( username ):
                results = {}
                social_media = [
                { "url": "https://www.github.com/{}", "name": "GitHub" },
                { "url": "https://www.pinterest.com/{}", "name": "Pinterest" },
                { "url": "https://www.youtube.com/{}", "name": "Youtube" },
                { "url": "https://www.tiktok.com/@{}", "name": "TikTok" },
                { "url": "https://www.twitch.tv/{}", "name": "Twitch" },
                { "url": "https://www.snapchat.com/add/{}", "name": "Snapchat" },
                { "url": "https://www.telegram.me/{}", "name": "Telegram" }
                ]

                for site in social_media:
                    url = site[ "url" ].format( username )
                    response = requests.get( url )
                    if response.status_code == 200:
                        results[ site[ "name" ] ] = url
                    else:
                        results[ site[ "name" ] ] = ( f"{ Style.BRIGHT }{ Fore.RED }[-]{ Fore.RESET } { Fore.WHITE }Username not found!{ Fore.RESET }{ Style.RESET_ALL }" )
                return results
            username = input( f"\n { Style.BRIGHT }{ Fore.YELLOW }Enter Username{ Fore.RESET } : { Fore.RED }" )
            print(f"\n { Fore.RESET }{ Fore.WHITE }=========={ Fore.RESET } { Fore.GREEN }INFORMATION USERNAME{ Fore.RESET } { Fore.WHITE }=========={ Fore.RESET }{ Style.RESET_ALL }")
            print()
            results = TrackLu( username )

            for site, url in results.items():
                print( f" { Style.BRIGHT }{ Fore.GREEN }[+] { site }{ Fore.RESET } : { Fore.RED }{ url }{ Fore.RESET }" )

        except KeyboardInterrupt:
            print( f" \n{ Fore.RED }[!] PROGRAM STOPPED.{ Fore.RESET }{ Style.RESET_ALL }" )

        input( f"{ Fore.RED }Press Enter{ Fore.RESET }" )
        main()

    elif input_user == "5":
        os.system( "cls" )
        time.sleep( 1 )
        stderr.writelines( f"""{ Style.BRIGHT }{ Fore.WHITE }
                    |--------------------------------|
                    |            { Fore.RED }MR ROBOT{ Fore.RESET }            |
                    |--------------------------------|{ Style.RESET_ALL }
            
        """)

        try:
            def PortScanner():
                socket.setdefaulttimeout( 0.25 )
                lock = threading.Lock()

                ip_address = input( f"  { Style.BRIGHT }{ Fore.RED }[~]{ Fore.RESET } IP Address : { Fore.RED }" )
                host = socket.gethostbyname( ip_address )
                print ( f"  { Fore.RESET }{ Fore.RED }[~]{ Fore.RESET } { Fore.YELLOW }Scanning on IP Address: { Fore.RESET }", host )

                def scan( port ):
                    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
                    try:
                        con = sock.connect( ( host, port ) )
                        with lock:
                            print( f"{ Fore.RED }{ port }{ Fore.RESET } is open" )
                        con.close()
                    except:
                        pass

                def execute():
                    while True:
                        worker = queue.get()
                        scan( worker )
                        queue.task_done()
                    
                queue = Queue()
                start_time = time.time()
                
                for x in range( 100 ):
                    thread = threading.Thread( target = execute )
                    thread.daemon = True
                    thread.start()
                
                for worker in range( 1, 500 ):
                    queue.put( worker )
                
                queue.join()

                print( f"   Time taken: { time.time() - start_time }{ Style.RESET_ALL }" )

            if __name__ == "__main__":
                PortScanner()

        except KeyboardInterrupt:
            print( f" \n{ Style.BRIGHT }{ Fore.RED }[!] PROGRAM STOPPED.{ Fore.RESET }{ Style.RESET_ALL }" )

        input( f"{ Fore.RED }Press Enter{ Fore.RESET }" )
        main()

    elif input_user == "0":
        print( f"\n  { Style.BRIGHT }{ Fore.RED }Bye!{ Fore.RESET }{ Style.RESET_ALL }" )

    else:
        main()

if __name__ == "__main__":
    main()