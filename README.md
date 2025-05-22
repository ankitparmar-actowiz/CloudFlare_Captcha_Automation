# SeleniumBase Cloud Flare Turnstile CAPTCHA Bypass Script for Hisco.com

This repository contains a Python script that uses [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) with stealth (undetectable/undetected-chromedriver) settings to access [Hisco.com](https://www.hisco.com) and automatically attempt to click and bypass a CAPTCHA challenge using SeleniumBase's `uc_gui_click_captcha()` method.

## 🚀 Features

- Uses `SeleniumBase`'s undetectable Chrome (`uc=True`) for stealth automation.
- Opens the target website (`hisco.com`) and maximizes the window.
- Waits for the page to fully load and interactively attempts to bypass CAPTCHA using GUI click simulation.

## 🧰 Requirements

Install the required Python package:

```bash
pip install seleniumbase
