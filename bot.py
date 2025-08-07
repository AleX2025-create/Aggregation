import telebot
import time
import subprocess
import pyautogui
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN ='8130888820:AAF9FL-Y4TtyrBs8xCWiECQAqeL4w7lne1c'
ADMIN_ID ="328114809"
SCRIPTS_DIR = r"C:\Users\s.oreshkin\ACPO"

# bot = telebot.TeleBot(TOKEN)


async def run_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        script_name = context.args[0] if context.args else "HHRu.ipynb"
        script_path = f"{SCRIPTS_DIR}\\{script_name}"

        subprocess.Popen(["code", "--reuse-window", script_path], shell=True) # Запускаем VS Code с файлом
        time.sleep(2)  # Ждём открытия VS Code
        pyautogui.hotkey('ctrl', 'alt', 'enter')  #Запуск скрипта путем нажатия кнопок Работает только локально!

        await update.message.reply_text(f"✅ Скрипт {script_name} запущен")
    except IndexError:
        await update.message.reply_text("ℹ️ Укажите имя скрипта: /run ННRu")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка: {str(e)}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔧 Бот для запуска скриптов. Используйте /run HHRu")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("run", run_script))

    print("Бот запущен...")
    app.run_polling()



if __name__ == '__main__':
    main()

