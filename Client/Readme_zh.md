# 📱 客户端配置

---
[English](./Readme.md)

## 🔧 设置步骤  
1. **🤖 申请 Telegram 账户和机器人**  
   - 注册 Telegram 账户并创建机器人。  
   - 保存 **机器人 ID** 以备后用。  

2. **📲 添加 iOS 快捷指令**  
   - 在 iOS 快捷指令中安装 **awaitUpdate Template.shortcut** 和 **Translate Template.shortcut**。  

3. **🔑 配置快捷指令**  
   - 在快捷指令中替换 `<Bot id>` 和 `<chat_id>` 为实际的机器人 ID 和聊天 ID。  
   - 获取聊天 ID 的方法：  
     ```bash
     https://api.telegram.org/bot<Bot_id>/getUpdates
     ```

---

## 📝 快捷指令说明  
- **Translate Template.shortcut**：  
  - 🌐 作为客户端服务网关。  
  - 🎤 通过机器人将录制的音频发送到 Telegram 聊天。  

- **awaitUpdate Template.shortcut**：  
  - 📥 使用 Telegram 的 `getUpdates` API 获取聊天消息。  
  - 📋 获取翻译结果。  

---

**注意**：请完成所有步骤以确保客户端功能正常运行。