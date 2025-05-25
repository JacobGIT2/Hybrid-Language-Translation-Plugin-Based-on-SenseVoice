# 📱 Client Configuration

---

## 🔧 Setup Steps  
1. **🤖 Apply for Telegram Account & Bot**  
   - Register a Telegram account and create a bot.  
   - Save the **Bot ID** for later use.  

2. **📲 Add Shortcuts to iOS**  
   - Install **awaitUpdate Template.shortcut** and **Translate Template.shortcut** in iOS Shortcuts.  

3. **🔑 Configure Shortcuts**  
   - Replace `<Bot id>` and `<chat_id>` in the shortcuts with your actual Bot ID and chat ID.  
   - To find your chat ID, use:  
     ```bash
     https://api.telegram.org/bot<Bot_id>/getUpdates
     ```

---

## 📝 Understanding the Shortcuts  
- **Translate Template.shortcut**:  
  - 🌐 Acts as the client service gateway.  
  - 🎤 Posts recorded audio to the Telegram chat via your bot.  

- **awaitUpdate Template.shortcut**:  
  - 📥 Retrieves chat messages using Telegram's `getUpdates` API.  
  - 📋 Fetches the translation results.  

---

**Note**: Complete all steps to ensure proper client functionality.