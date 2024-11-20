import os 
import discord
from dotenv import load_dotenv
from rich import print
from classes import ai
from sqlmodel import Session, select, or_

load_dotenv()

import database

bot_intent = discord.Intents.default()
bot_intent.message_content = True
bot_intent.messages = True
bot_intent.members = True

bot = discord.Bot(intents=bot_intent, owner_id=589381655710662656)

ART = r"""
[bold blue]
                    ████                    
              ████  ████  ████              
      ████    ████████████████    ████      
      ██████  ████████████████  ██████      
        ████      ████████      ████        
████    ████        ████        ████    ████
██████████████      ████      ██████████████
  ████████████████  ████  ████████████████  
      ████████████████████████████████      
              ████████████████              
                  ████████                  
              ████████████████              
      ████████████████████████████████      
  ████████████████  ████  ████████████████  
██████████████      ████      ██████████████
████    ████        ████        ████    ████
        ████      ████████      ████        
      ██████  ████████████████  ██████      
      ████    ████████████████    ████      
              ████  ████  ████              
                    ████                    
 
[/bold blue]
> {} is active 🤘🤘!
 - Made By Atharva
"""
@bot.event
async def on_ready():
    print(ART.format(bot.user))


token = str(os.getenv("DISCORD_TOKEN"))

extensions = ["ai", "fun"]
bot.load_extensions(*[f"cogs.{extension}" for extension in extensions])

if __name__ == "__main__":
    database.create_tables()
    ai.setup_client()
    bot.run(token)



















'''
print(os.getenv("DATABASE_URL"))

if __name__ == "__main__":
    database.create_tables()
    session = Session(database.engine)

    # select multiple rows from our data 
    statement = select(database.models.Session)
    result = session.exec(statement)

    # How to filter the data 
    statement = select(database.models.Session).where(database.models.Session.is_dm == True, database.models.Session.deleted == False)
    result = session.exec(statement)
'''

    
''' 
    database_session = Session(database.engine)

        # Create the instance 
    discord_channel_1 = database.models.Session(channel_id = "12345", is_dm = False)
    discord_channel_2 = database.models.Session(channel_id = "54321", is_dm = True)

        # Add the instance 
    database_session.add(discord_channel_1)
    database_session.add(discord_channel_2)

        # Commit the change
    database_session.commit()
'''


















#print(os.getenv("OPENAI_API_KEY"))
#print(os.getenv("DISCORD_TOKEN"))
#print(os.getenv("DATABASE_URL"))