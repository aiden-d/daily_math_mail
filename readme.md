# Description

This project contains a simple mailer script which can be used to send a question at a desired frequency to a list of users. The project is ideally hosted on an always-on low-power computer such as a Raspberry Pi

The concept of spaced-repetition, where a user re-exposes themselves to concepts over an iteratively spaced timeline, is highly regarded in the revision literature. Please feel free to read up more on it (see [this](https://journals.sagepub.com/doi/abs/10.1177/2372732215624708) and [this](https://www.pnas.org/doi/10.1073/pnas.1815156116)).

# Workings

Images of questions can be imported into here using a variety of tools (check out my other repos) and are stored in  the `images/` directory, with the image being titled X.png and the answer being X-ms.png (where X is any string). The index.txt file contains the category of each question, used in the email description.

# Installation

Clone the repo using the following command:

``` bash
git clone git@github.com:aiden-d/daily_question_mailer.git
```
Navigate into the repo:
```bash
cd daily_question_mailer
```
Setup the images folder and index.txt

Setup the `send_mail.py` script, filling in your email address, password and recipients.

# Server Setup

Once you have finished the basic installation and setup, you may want to host it to send on a daily basis.

You may wish to do this with Cron. The following is a Cron tutorial for Ubuntu based systems:

Update package list

```bash 
sudo apt update
```

Install Cron

```bash 
sudo apt install cron
```

Enable it to run in background

```bash 
sudo systemctl enable cron
```

Edit the config

```bash
crontab -e
```

Paste the following in:
```
0 0 6 * * ? python3 PATH_OF_SEND_MAIL_SCRIPT
```

Replace `6` with the hour of the day which you want to send the mail.

Confirm it is successful using
```bash 
crontab -l
```

