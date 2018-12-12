from telegram.ext import Updater, CommandHandler

from device.broker import Broker

api = "750479155:AAHni_YJJxGbbFjRHKmYmBvniMX6_TP1rXQ"


class BotBroker(Broker):
    def __init__(self):
        Broker.__init__(self)
        self.run()
        self.subscribe()

    def light_status(self):
        status = ''
        for key in self.payload.keys():
            light = self.payload.get(key)

            status = status + light['name']
            status = status + self.is_active(light)
            status = status + "\n"

        return status

    def is_active(self, light):
        if light['status']:
            return ' is on.'
        else:
            return ' is off.'


class Bot(BotBroker):

    def __init__(self):
        BotBroker.__init__(self)
        self.updater = Updater(api)
        self.dp = self.updater.dispatcher

    def start(self, bot, update):
        update.message.reply_text('Well Hello there')

    def help(self, bot, update):
        update.message.reply_text('Welcome to this bot')

    def error(self, bot, update, error):
        """Log Errors caused by Updates."""
        print("error error")

    def lights(self, bot, update):
        update.message.reply_text(self.light_status())

    def main(self):

        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))
        self.dp.add_handler(CommandHandler("lights", self.lights))
        self.dp.add_error_handler(self.error)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    print("Starting up the bots")
    b = Bot()
    b.main()
