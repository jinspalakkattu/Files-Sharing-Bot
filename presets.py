# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>Click the below button</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you getting movies from</code> @MovieKeralam. " \
                   "<code>Just Keep this message live Here</code>đ\n\n" \
                   "<b>My code can be seen: </b><a href='https://github.com/m4mallu/gofilesbot'> HERE</a>"
    CLEAN_CHAT_MSG = "â ď¸ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\nđ <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact Movie name.\n\nđ I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. đ˘</b>\n\n<code>Bot won't work in PM, Ask in ma Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>Unable to send medias</b> âď¸\n<code>Click the below button\nAsk here for movies later!</code>"
    MEDIA_SEND_TEXT = "<code>Media dispatched as PM đĽł</code>"
    NO_MEDIA = "Requested movie: <b>{}</b>\n\n<b>Not available " \
               "Right Now</b>\n<code>Possible Causes : đ¤\n\nâ­ď¸ Not " \
               "released yet</code>\nâ­ď¸ <a href='https://www.google.com/search?q={}'> Spelled incorrectly</a>\n" \
               "<code>â­ď¸ Unwanted texts in Msgs\nâ­ Asking theatre prints\nâ­ Not in ma Database</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
