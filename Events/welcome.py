import interactions
from interactions import Extension, Embed, listen
import Funtions.config as cfg


class WelcomeEvent(Extension):

    @listen()
    async def on_member_add(self, ctx):
        # Pobierz kanał, na którym chcesz wysłać powiadomienie
        channel_id = cfg.get("WELCOME_CHANNEL_ID")
        channel = ctx.guild.get_channel(channel_id)
        # Tworzenie embeda
        #embed = Embed(title="New user!", description=f"👋🏼 Welcome on our serwer, {ctx.member.user.mention}!")
        #embed.set_thumbnail(url=ctx.member.avatar_url)

        # Wysłanie embeda na kanał
        await channel.send(f"👋🏼  **Welcome on ControlByte's discord server,** {ctx.member.user.mention}!")


