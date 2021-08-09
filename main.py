import random, json, os, ctypes, time

try:
    import requests, ctypes
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama ctypes')

init(convert=True)
class Client:
    def __init__(self):
        self.tokens = open("tokens.txt").read().split("\n")
        self.session = requests.Session()

    def RandomColor(self):
        randcolor = random.randint(0x000000, 0xFFFFFF)
        return randcolor

    def clear(self):
        os.system("clear")

    def Headers(self, token: str):
        headers = {
            "Content-Type": "application/json",
            "authorization": token,
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
        }
        return headers

    def friendRequest(self, userID):
      for token in self.tokens:
        _data = self.session.put(f"https://discord.com/api/v6/users/@me/relationships/{userID}", json={}, headers=self.Headers(token))

        if _data.status_code == 204:
          print(" Sent A Friend Request :D")

      self.clear()
      self.start()

    def leaveServer(self, serverID):
        for token in self.tokens:
            _data = self.session.delete(f"https://discord.com/api/v6/users/@me/guilds/{serverID}", headers=self.Headers(token))

            if _data.status_code == 204:
                print(f"[{Fore.CYAN}!!{Fore.RESET}] Left the server!")

        self.clear()
        self.start()

    def spam(self, message: str, channelID: str, tts: bool, amount: int, delay: int):
        _message = {
            "content": message,
            "tts": tts,
        }
        for _ in range(amount):
            time.sleep(delay)
            for token in self.tokens:
                _data = self.session.post(f"https://discordapp.com/api/v6/channels/{channelID}/messages",json=_message,headers=self.Headers(token))

                if _data.status_code == 200:
                    print(f"[{Fore.CYAN}!!{Fore.RESET}] Sent a new message!")
        self.clear()
        self.start()

    def join(self, code: str):
        for token in self.tokens:
            _data = self.session.post(f"https://discordapp.com/api/v6/invites/{code}",headers=self.Headers(token))

            if _data.status_code in [200, 204]:
                print(f"[{Fore.BLUE}!!{Fore.RESET}] Joined the {_data.json()['guild']['name']} server.")

        self.clear()
        self.start()

    def start(self):
        if self.tokens == []:
            print(f'{Fore.BLUE}[{Fore.RESET}Error:{Fore.BLUE}] Could not find tokens.txt file.')
            exit(0)

        print(f"{Fore.BLUE}[{Fore.RESET}1{Fore.BLUE}] Join Server {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}2{Fore.BLUE}] Leave Server {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}3{Fore.BLUE}] Spam channel {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}4{Fore.BLUE}] Spam Friend Requests {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}5{Fore.BLUE}] Exit Application {Fore.RESET}")

        option = int(input("> "))

        if option not in [1, 2, 3, 4, 5]:
            print(f"[{Fore.RED}Invalid Option{Fore.RESET}]")
            time.sleep(1)
            self.start()

        if option == 1:
            print(f"[{Fore.BLUE}>{Fore.RESET}] Server Invite {Fore.RESET}")
            code = str(input("> "))

            if "https://discord.gg/" in code:
                code = code.split("https://discord.gg/")[1]
            else:
                code = code
            self.join(code)

        if option == 2:
            print(f"[{Fore.BLUE}>{Fore.RESET}] Server Id {Fore.RESET}")
            server = str(input("> "))
            self.leaveServer(server)

        if option == 3:
            print(f"[{Fore.BLUE}>{Fore.RESET}] Channel Id {Fore.RESET}")
            channelID = str(input("> "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Message Content {Fore.RESET}")
            message = str(input("> "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Amount of messages to send {Fore.RESET}")
            amount = int(input(" "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Delay (1,2,3)[seconds] {Fore.RESET}")
            delay = int(input(" "))

            self.spam(message=message,channelID=channelID,tts=False,amount=amount,delay=delay)

        if option == 4:
          print(f"[{Fore.BLUE}>{Fore.RESET}] User Id {Fore.RESET}")
          self.friendRequest(str(input("> ")))

        if option == 5:
            exit()

if __name__ == "__main__":
    Client().start()
