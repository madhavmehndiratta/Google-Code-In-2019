from telegram.ext import Updater , CommandHandler,MessageHandler, Filters
import logging
import json
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

req = requests.get("https://api.github.com/orgs/fedora-infra/repos").content.decode("UTF-8")

def start(update, context):
    update.message.reply_text("Hola!, run /help to view the commands")

def help(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here's a list of commands you can use: \n /repos : List all the repositories\n /forks <repos_name> : Returns number of forks for <repos_name>\n /allforks : List all repositories with their corresponding number of forks \n /help : See list of available commands")

def repos(update, context):
    message = "\n"

    for repo in json.loads(req):
        message += repo["name"] + "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def forks(update, context):
    name = update.message.text.split(" ")
    if len(name) > 1:

        for repo in json.loads(req):
            if repo["name"] == name[1]:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Number of forks for " + name[1] + " are: " + str(repo["forks"]))
                return

        context.bot.send_message(chat_id=update.effective_chat.id, text="Please specify a valid repository name")

    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please specify a repository name")

def allforks(update, context):
    message = ""
    message += "\n"
    for repo in json.loads(req):
        message += repo["name"] + " - " + str(repo["forks"]) + "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(message))

def main():
    updater = Updater(token="#YOUR_BOT_TOKEN", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("repos", repos))   
    updater.dispatcher.add_handler(CommandHandler("forks", forks))
    updater.dispatcher.add_handler(CommandHandler("allforks", allforks))  
    updater.start_polling()
    updater.idle()

main()