"""
Модуль обработчика сообщений, не попадающих не под один фильтр.

"""

from telebot.types import Message
from loguru import logger
from loader import bot

@logger.catch
@bot.message_handler(state=None)
def bot_echo(message: Message):
    """
    Обработчик для текстовых сообщений без какого-либо состояния (эхо, но молчаливое).

    Функция не выполняет никаких действий и может быть использована как обработчик для сообщений,
    которые не подпадают ни под одно из состояний (не имеют своего специфического обработчика).
    Просто проходит через неё и ничего не происходит.

    Использовалась при создании, для отладки.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    pass
