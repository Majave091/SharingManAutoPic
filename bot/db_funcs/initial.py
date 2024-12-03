from typing import Dict

from bot.base import database
from bot.utils import BOT_ID, logger


async def initial_database() -> None:
    """
    Initializes the database with default values if they are not already present.

    This function sets up initial configuration values in the database.
    It checks if certain keys exist in the database; if not, it adds them with default values.

    Default values added:
        - "GENERATE_URL": False
        - "PROTECT_CONTENT": False
        - "HUN_TEXT": A default picture start message
        - "IMG_TEXT": A default picture force message
        - "FORCE_TEXT": A default force text message
        - "START_TEXT": A default start text message
    """
    default_start_text = (
        "Hello, {mention}!\n"
        "The bot is up and running. These bots can store messages in custom chats, "
        "and users access them through the bot."
    )
    default_force_text = (
        "To view messages shared by bots, join first, then press the Try Again button."
    )
    default_hun_text = (
        "https://im.gurl.eu.org/file/AgACAgEAAxkDAAOvZ073oPuVGpESRKlxzoUQrBAQDloAApOxMRt_vHlGWWd5mu60EJsBAAMCAAN5AAM2BA.jpg"
    )
    default_img_text = (
        "https://im.gurl.eu.org/file/AgACAgEAAxkDAAOwZ0731kCFpCGuY1uWpnVmwgF43-sAApSxMRt_vHlGKHKfwBuyHgcBAAMCAAN5AAM2BA.jpg"
    )
    default_key_value_db: Dict[str, bool] = {
        "GENERATE_URL": False,
        "PROTECT_CONTENT": False,
        "HUN_TEXT": default_hun_text,
        "IMG_TEXT": default_img_text,
        "FORCE_TEXT": default_force_text,
        "START_TEXT": default_start_text,
    }

    bot_id = int(BOT_ID)
    doc = await database.get_doc(
        bot_id
    )  # Fetch the document once to avoid multiple database calls

    for key, value in default_key_value_db.items():
        data = key.replace("_", " ").title()

        if doc is None or key not in doc:
            await database.add_value(bot_id, key, value)
            logger.info(f"{data}: Default")
        else:
            logger.info(f"{data}: Existed")
