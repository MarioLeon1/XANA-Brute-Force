# XANA-Brute-Force
Instagram Brute Force Tool made for educational purposes. Highly effective!

## Installing XANA

Set up your distro for the fun

```
git clone https://github.com/MarioLeon1/XANA-Brute-Force
pip -r install requirements.txt
```

## Installing Windscribe

This program needs the manual installation of Windscribe from your part.

**Windscribe is used for automatic proxy and IP switching while using the tool**

Visit https://esp.windscribe.com/ and create a free account. It'll take you less than 2 minutes
Just download and install it

### Get Windscribe to work

Once you've download and installed it, just open up the **terminal** again and type

```
windscribe start
windscribe login
```
Connect your account and you'll be ready to go!

## Using XANA

Once you're done with the setup, let's start to have fun.

```
cd XANA-Brute-Force
python attack.py
```

Write your target's username and let it work :)

# About

XANA uses a wordlist with the 1 000 000 most used passwords in the world, which makes the tool very effective.
You can still **change the wordlist** entering `attack.py`and changing line 146, where it says `passwords.txt`.

XANA uses a dictionary with the 1 000 000 most used passwords in the world, so believe me it will find any account, but still you can use any wordlist you desire entering the file `attack.py`and changing line 146 where it says `passwords.txt`.


