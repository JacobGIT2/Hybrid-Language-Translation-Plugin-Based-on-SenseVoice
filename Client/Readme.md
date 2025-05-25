### Client configuration
1. To successfully initialize, you need to apply a **telegram account** & a **telegram bot**. After registered the bot, keep the **Bot id**
2. Put both **awaitUpdate Template.shortcut** & **Translate Template.shortcut** into IOS's Shortcut
3. Replace \<Bot id> & \<chat_id> with your own bot's id & chat_id, you may get your chat_id using https://api.telegram.org/bot\<Bot id>/getUpdates
### More Explanation:
- **Translate Template.shortcut** is the client service gateway, it will POST the recorded audio to the telegram chat through your bot
- **awaitUpdate Template.shortcut** is the result retrieve module, it retrieve chat message with telegram api getUpdates