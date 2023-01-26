from typing import Type
import urllib.parse
import random
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from mautrix.types import RoomCreatePreset
from maubot import Plugin, MessageEvent
from maubot.handlers import command


class Config(BaseProxyConfig):

  def do_update(self, helper: ConfigUpdateHelper) -> None:
    helper.copy("quotes")

class QuotePlugin(Plugin):
  async def start(self) -> None:
    self.config.load_and_update()

  @command.new("quote")
  @command.argument("argument", pass_raw=True, required=True)
  async def quote(self, event: MessageEvent, argument: str) -> None:
    await event.mark_read()    

    quotes = self.config["quotes"]
    if argument and len(argument.split()) == 1:
      if argument in quotes:
        quote = random.choice(quotes[argument])
        await event.respond(f"{quote}")
      else:
        await event.reply(f"{argument} was not found in list of available quotes. Choose one from {list(quotes.keys())}")
    else:
      await event.reply(f"Please provide a source to quote. Choose one from {list(quotes.keys())}")

  @classmethod
  def get_config_class(cls) -> Type[BaseProxyConfig]:
    return Config