import interactions
from decouple import config
from interactions import slash_command, SlashContext, SlashCommand, slash_option, SlashCommandChoice, OptionType

Var_1 = config('VAR1')
Var_2 = config('VAR2')
BOT_TOKEN = Var_1 + Var_2
bot = interactions.Client(token=BOT_TOKEN)
base = SlashCommand(
    name="test",
    description="Commands involving logs"
)

@slash_command(name="rps", description="rock, paper , scissors")
@slash_option(
    name="rps_option",
    description="RPS Option",
    required=True,
    opt_type=OptionType.STRING,
    choices=[
        SlashCommandChoice(name="rock", value="rock"),
        SlashCommandChoice(name="paper", value="paper"),
        SlashCommandChoice(name="scissors", value="scissors")
    ]

)

async def my_command_function(ctx: SlashContext,rps_option):
    await ctx.send(rps_option, ephemeral=True)

bot.start()
if __name__ == "__main__":
    bot.start()
