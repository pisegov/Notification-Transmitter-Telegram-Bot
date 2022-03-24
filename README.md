# Notification Transmitter Telegram Bot

A Telegram bot for transmitting notifications from an Android device

![1](https://user-images.githubusercontent.com/58353454/159930890-832a7e3b-02d0-4856-8918-f7514b97ecaf.jpg)

## Purpose

* The bot is created to solve my personal problem: I always get stuck in social networks
* I wanted to remove the apps of some of them from my phone, but not lose the ability to catch posts sent to me by my
  friends.
* It also allows catching messages with some login codes sent to an alternate phone number

## How it works

* The [Android application](https://github.com/pisegov/Notification-Transmitter-Android-App) is installed to spare
  android phone
* The phone is connected to the internet
* The app has been granted permission to access notifications
* Social network applications and transmitter app are running on the phone with battery saving turned off
* When a notification arrives, the application catches it and sends a http request with the notification text to a
  remote server with a running Telegram bot
* The Telegram bot is sending message with response data

## Features

* Uses Flask framework to implement a simple server with an API method for receiving notifications from the Android app
* Uses aiogram framework to implement the chat bot
* Runs the bot and the server in different threads
* It is deployed on Heroku
* In addition, it is a simple echo bot :joy:
