import interactions
from decouple import config
from interactions import slash_command, SlashContext, SlashCommand

Var_1 = config('VAR1')
Var_2 = config('VAR2')
BOT_TOKEN = Var_1 + Var_2
bot = interactions.Client(token=BOT_TOKEN)
base = SlashCommand(
    name="test",
    description="Commands involving logs"
)

@slash_command(name="rps", description="rock, paper , scissors")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")



bot.start()
if __name__ == "__main__":
    bot.start()
