from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🚸ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ🚸 ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🌀ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs🌀", url="https://t.me/moi_bot_lists/4")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ ᴍᴇ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ ᴍᴜᴋᴇsʜ ᴋʜᴜsʜɪ ♥", url="https://t.me/mukhushi_official")],
    ]

    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ʏᴏᴜ  ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ  (ᴇᴠᴇɴ  ᴠᴇʀsɪᴏɴ 2) ᴀɴᴅ  ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ  ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

 ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- @moi_bot_lists
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴍᴏɪ ʙᴏᴛ 
/help - ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ 
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ 
/generate - ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss 
/restart - ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ  ʙʏ @itz_mst_boy  ᴘᴏᴡᴇʀᴅᴇᴅ ʙʏ @moi_bot_lists

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](tg://need_update_for_some_feature/)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ  : @itz_mst_boy
    """
