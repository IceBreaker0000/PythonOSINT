import requests
from bs4 import BeautifulSoup

print("Welcome to the OSINT User ID Fetcher!")

u = input("Type user id: ")
a = input("Type the Users Bday: ")

print("Is this the exact user info? (y/n)")
exact = input().strip().lower()

if exact != 'y':
    user_ids = [f"{u}{str(i).zfill(4)}" for i in range(10000)]
    print(f"Generated {len(user_ids)} user ids by appending 4-digit numbers.")
else:
    user_ids = [u, f"{u}{a}"]

def check_user_ids(user_ids):
    for u in user_ids:
        print(f"\nChecking user id: {u}")
        urls = [
            ("Instagram", f"https://www.instagram.com/{u}"),
            ("Facebook", f"https://www.facebook.com/{u}"),
            ("YouTube", f"https://www.youtube.com/@{u}"),
            ("Threads", f"https://www.threads.net/@{u}"),
            ("GitHub", f"https://www.github.com/{u}"),
            ("TikTok", f"https://www.tiktok.com/@{u}"),
            ("Twitter", f"https://www.twitter.com/{u}"),
            ("Reddit", f"https://www.reddit.com/user/{u}"),
            ("LinkedIn", f"https://www.linkedin.com/in/{u}"),
            ("Pinterest", f"https://www.pinterest.com/{u}"),
            ("Snapchat", f"https://www.snapchat.com/add/{u}"),
            ("Tumblr", f"https://www.tumblr.com/{u}"),
            ("Flickr", f"https://www.flickr.com/people/{u}"),
            ("Vimeo", f"https://vimeo.com/{u}"),
            ("SoundCloud", f"https://soundcloud.com/{u}"),
            ("Discord", f"https://discord.com/users/{u}"),
            ("Twitch", f"https://www.twitch.tv/{u}"),
            ("WhatsApp", f"https://wa.me/{u}"),
            ("Telegram", f"https://t.me/{u}"),
            ("Quora", f"https://www.quora.com/profile/{u}"),
            ("Medium", f"https://medium.com/@{u}"),
            ("GitLab", f"https://gitlab.com/{u}"),
            ("Bitbucket", f"https://bitbucket.org/{u}"),
            ("StackOverflow", f"https://stackoverflow.com/users/{u}"),
            ("Blogger", f"https://www.blogger.com/profile/{u}"),
            ("WordPress", f"https://{u}.wordpress.com"),
            ("MySpace", f"https://myspace.com/{u}"),
            ("DeviantArt", f"https://www.deviantart.com/{u}"),
            ("VK", f"https://vk.com/{u}"),
            ("Weibo", f"https://www.weibo.com/{u}"),
            ("Line", f"https://line.me/ti/p/{u}"),
            ("Clubhouse", f"https://www.joinclubhouse.com/@{u}"),
            ("Yandex", f"https://yandex.com/users/{u}"),
            ("Foursquare", f"https://foursquare.com/{u}"),
            ("Meetup", f"https://www.meetup.com/{u}"),
            ("Goodreads", f"https://www.goodreads.com/user/show/{u}"),
            ("Last.fm", f"https://www.last.fm/user/{u}"),
            ("Spotify", f"https://open.spotify.com/user/{u}"),
            ("Apple Music", f"https://music.apple.com/profile/{u}"),
            ("Amazon", f"https://www.amazon.com/{u}"),
            ("eBay", f"https://www.ebay.com/usr/{u}"),
            ("Craigslist", f"https://{u}.craigslist.org"),
            ("Yelp", f"https://www.yelp.com/user_details?userid={u}"),
            ("TripAdvisor", f"https://www.tripadvisor.com/Profile/{u}"),
            ("Pinterest", f"https://www.pinterest.com/{u}"),
            ("Baidu", f"https://www.baidu.com/s?wd={u}"),
            ("Alibaba", f"https://www.alibaba.com/member/{u}"),
            ("Reddit", f"https://www.reddit.com/user/{u}"),
            ("Tinder", f"https://tinder.com/@{u}"),
            ("Bumble", f"https://bumble.com/@{u}"),
            ("OkCupid", f"https://www.okcupid.com/profile/{u}"),
            ("Hinge", f"https://hinge.co/{u}"),
            ("Discord", f"https://discord.com/users/{u}"),
            ("Signal", f"https://signal.me/#p/{u}"),
            ("Clubhouse", f"https://www.joinclubhouse.com/@{u}"),
            ("Viber", f"https://invite.viber.com/?g2={u}"),
            ("Line", f"https://line.me/ti/p/{u}"),
            ("WeChat", f"https://weixin.qq.com/r/{u}"),
            ("Snapchat", f"https://www.snapchat.com/add/{u}"),
        ]

        for platform, url in urls:
            try:
                response = requests.get(url, timeout=5)
                page = response.text.lower()
                soup = BeautifulSoup(response.text, "html.parser")

                if platform == "Instagram":
                    if ("sorry, this page isn't available." in page or
                        soup.find("h2", string="Sorry, this page isn't available.")):
                        print(f"[-] {platform}: Not found.")
                    elif soup.find("img", {"alt": "Profile photo"}):
                        print(f"[+] {platform}: Found! {url}")
                    elif soup.find("meta", property="og:description", content=lambda c: c and "followers" in c.lower()):
                        print(f"[+] {platform}: Found! {url}")
                    elif 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

                elif platform == "Threads":
                    if ("sorry, this page isn't available." in page or
                        soup.find("h2", string="Sorry, this page isn't available.")):
                        print(f"[-] {platform}: Not found.")
                    elif soup.find("img", {"alt": "Profile photo"}):
                        print(f"[+] {platform}: Found! {url}")
                    elif 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

                elif platform == "Facebook":
                    if ("this content isn't available at the moment" in page or
                        "page isn't available" in page or
                        "page not found" in page or
                        soup.find("div", string=lambda s: s and "content isn't available" in s.lower())):
                        print(f"[-] {platform}: Not found.")
                    elif soup.find("meta", property="og:description", content=lambda c: c and "facebook" in c.lower()):
                        print(f"[+] {platform}: Found! {url}")
                    elif 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

                elif platform == "GitHub":
                    if response.status_code == 404:
                        print(f"[-] {platform}: Not found.")
                    elif soup.title and "not found" in soup.title.text.lower():
                        print(f"[-] {platform}: Not found.")
                    elif soup.find("img", {"alt": "Avatar"}):
                        print(f"[+] {platform}: Found! {url}")
                    elif soup.find("meta", property="og:title", content=lambda c: c and u.lower() in c.lower()):
                        print(f"[+] {platform}: Found! {url}")
                    elif 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

                elif platform == "YouTube":
                    if ("this channel does not exist" in page or
                        "404 not found" in page or
                        soup.find("meta", property="og:title", content=lambda c: c and "not found" in c.lower())):
                        print(f"[-] {platform}: Not found.")
                    elif soup.find("meta", property="og:title", content=lambda c: c and u.lower() in c.lower()):
                        print(f"[+] {platform}: Found! {url}")
                    elif 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

                else:
                    if 200 <= response.status_code < 300:
                        print(f"[+] {platform}: Found! {url}")
                    else:
                        print(f"[-] {platform}: Not found.")

            except requests.RequestException:
                print(f"[!] {platform}: Error accessing {url}")
        print("\nFinished checking all platforms.")

check_user_ids(user_ids)
print("OSINT User ID Fetcher completed.")