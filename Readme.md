### Background
- This is a model inference translation plugin based on [SenseVoice](https://github.com/FunAudioLLM/SenseVoice)
- It use telegram as communication link, **allowing deployment on public server that banned Application-level ports**
- As provided by SenseVoice, it support hybrid language translation
- IOS shortcut is chosen as the way of plugin
### Work Flow
- Click and awoke shortcut on IOS device --> Automatically Record audio & Send to telegram chat through bot --> Server's telegram client receive audio file & start inference --> Server send result message to chat through your telegram account --> IOS device get result message, alert result & copy to clipboard
- Based on my shortcut implementation, alerted result will be translated to Chinese, clipboard message will not be translated
### Requirements
1. No additional hardware requirements once you can run [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) model inference