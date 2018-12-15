import json

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from device.broker import Broker

api = "750479155:AAHni_YJJxGbbFjRHKmYmBvniMX6_TP1rXQ"


class BotBroker(Broker):
    def __init__(self):
        Broker.__init__(self)
        self.run()
        self.subscribe()
        self.action_flag = 'action'
        self.publish("status", {})

    def light_status(self):
        status = ''
        for key in self.payload.keys():
            light = self.payload.get(key)

            status = status + light['name']
            status = status + self.is_active(light)
            status = status + "\n"

        return status

    def lights_as_actions(self):
        strings = []
        for key in self.payload.keys():
            light = self.payload.get(key)
            status, action = self.turn_off_light(light)
            string = status + light['name'] + "!"

            strings.append({'label': string, 'action': action, 'id': key})

        return strings

    def is_active(self, light):
        if light['status']:
            return ' is on.'
        else:
            return ' is off.'

    def turn_off_light(self, light):
        if light['status']:
            return 'Turn off ', False
        else:
            return 'Turn on ', True

    def act_on_lights(self, id, action):
        self.payload[id]['action'] = action
        self.publish(self.action_flag, self.payload)

    def all_lights_off(self):
        for key in self.payload.keys():
            self.payload.get(key)['action'] = False

        self.publish(self.action_flag, self.payload)


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
        print("error error\n")
        print(error)

    def status(self, bot, update):
        update.message.reply_text(self.light_status())

    def lights(self, bot, update: Update):
        button = [KeyboardButton("lights")]
        print('ran')
        # bot.send_message(chat_id=update.message.chat_id, text="which light",
        #                  reply_markup=ReplyKeyboardMarkup(button))
        # # chat_id = update.chat["id"]
        # # print(update.message.chat_id)

        keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                     InlineKeyboardButton("Option 2", callback_data='2')],

                    [InlineKeyboardButton("Option 3", callback_data='3')]]

        reply_markup = InlineKeyboardMarkup(self.lights_keyboard())

        update.message.reply_text('Please choose:', reply_markup=reply_markup)

    def lights_keyboard(self):
        buttons = []

        all_off = [InlineKeyboardButton("Turn off all lights", callback_data="all off")]

        buttons.append(all_off)
        print(self.lights_as_actions())
        for items in self.lights_as_actions():
            buttons.append(self.create_button(items['label'], (items['action'], items['id'])))
        print(buttons)
        return buttons

    def create_button(self, label, action):
        json_data = json.dumps(action)
        return [InlineKeyboardButton(label, callback_data=json_data)]

    def button(self, bot, update):
        query = update.callback_query

        if query.data == "all off":
            print("all off")
            self.all_lights_off()
        else:

            data = json.loads(query.data)
            print(type(data))
            self.act_on_lights(data[1], data[0])

        bot.edit_message_text(text="Lights Updated",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    def main(self):

        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))
        self.dp.add_handler(CommandHandler("status", self.status))
        self.dp.add_handler(CommandHandler("lights", self.lights))
        self.dp.add_handler(CallbackQueryHandler(self.button))
        self.dp.add_error_handler(self.error)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    print("Starting up the bots")
    b = Bot()
    b.main()
