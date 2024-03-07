import interactions
from decouple import config
from interactions import slash_command, SlashContext

Var_1 = config('VAR1')
Var_2 = config('VAR2')
BOT_TOKEN = Var_1 + Var_2
bot = interactions.Client(token=BOT_TOKEN)


@slash_command(name="my_command", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")
bot.start()
if __name__ == "__main__":
    bot.start()
