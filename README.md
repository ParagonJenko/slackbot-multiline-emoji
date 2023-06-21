# A small Python web app to create multiline Slackbot emojis.

_This is an alpha version - use at own risk of emojis looking funky - I'd probably try do them in your DMs_

## Why:

I've been doing this manually which is error prone - and I'd like to play with Python again.

## What:

I'm manually using an [Image Splitter](https://ruyili.ca/image-splitter/) but there is this [split-image](https://pypi.org/project/split-image/) Python package you can use.

The **MVP** of this project is: To be able to copy and paste a command that turns your emojis into a string that you can enter into Slackbot.

Format of response:
`command` \n :0_0: 1_0: \n :0_1: :1_1: \n

X X
X X

X X X
X X X
X X X

## How:

1. You need to go to your {workspace}.slack.com/customize/emoji and upload all sections of your emoji.
2. You then need to go to {workspace}.slack.com/customize/slackbot sedction and enter the string generated.

## WHY IS THIS THE END OF THIS?

I've attempted to automate this to be as good as I want it to, but the library I found for splitting images wasn't very good - and really that's a key bit.

Sadly my adventure back into Python is over and I'll make this in another language with another library unless I want to come back and debug the library.
