from discord.ext.commands import Context


class RainContext(Context):
    """Overwrites default Context to save READs to MongoDB"""
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.guild_config_cache = None

    async def guild_config(self):
        if self.guild_config_cache is None:
            self.guild_config_cache = await self.bot.mongo.config.guilds.find_one({'guild_id': str(self.guild.id)})

        return self.guild_config_cache
