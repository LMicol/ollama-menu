## Ollama Widget for Linux

So, I made this widget for Ollama on Linux because, for some [_unknown_](https://github.com/ollama/ollama/issues/690) reason, the Ollama team decided not to implement a way to stop a model while it's generating a response.

I was testing DeepSeek R1 14B this morning, and it was running with an _amazing_ 0.3 tokens/second. But when I tried to stop it—oh yeah, you can't! PC started lagging, and now, you get to open a terminal and kill the process manually with `sudo systemctl stop ollama`, all while your computer is practically frozen.

So, I got pissed off and built this systray app to solve this with one press of a button.

### Install

1. Clone the repo
2. Install the python requirements `pip install -r requirements.txt`
3. Run `install.sh` — it’ll create a service to run on startup (You may need to change the `ExecStart` path to your python installation location, you can check that with `whereis python`). 

Want to contribute? Go ahead, feel free to improve this mess.
