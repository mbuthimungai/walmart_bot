import os
import sys
from datetime import datetime, timedelta
import discord
import asyncio
import json
import random


sys.path.append(os.getcwd())
from scrapers.scraper import Walmart


async def menu(message, user, bot = None):
    """
    Handles different commands based on the user's input message and sends corresponding information to the user via private message.

    Args:
        - message (str): The user's input message, indicating the command to be executed.
        - user (discord.User): User object representing the user who initiated the command.
        - bot (discord.Client, optional): Discord bot object. Defaults to None.

    Returns:
        - None: This function does not return any value directly. It sends relevant information to the user via private message based on the input command.
    """
    if message == '!general' or message == '!help':
        embed = discord.Embed(title = "General", description = "General overview of bot.", color = 0xff9900)
        embed.add_field(name = '!commands', value = "List of available commands and their explanation.", inline = False)
        embed.add_field(name = '!about', value = "Provides the information about the bot and its purpose.", inline = False)
        embed.add_field(name = "!ping", value = "Check the bot's response time to the server.")
        embed.add_field(name = "!status", value = "Check the status of the Amazon's server.", inline = False)
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!commands':
        embed = discord.Embed(title ='Bot menu', description = "List of available commands and their explanation.", color = 0xff9900)
        embed.add_field(name = "!asin `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts ASIN from the provided product link.", inline = False)
        embed.add_field(name = "!rev `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts the top positive and top critical review of the product.", inline = False)
        embed.add_field(name = "!info `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts the detailed product informations.", inline = False)
        embed.add_field(name = "!info-asin `B0BCNKKZ91`", value = "Extracts the detailed product informations.", inline = False)
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!about':
        embed = discord.Embed(title = "About", description = "Provides the information about the bot and its purpose.", color = 0xff9900)
        embed.add_field(name = "Purpose", value = "The purpose of this bot is to extract product ASIN and product reviews by product link, and retrieve product information by pasting ASIN.", inline = False)
        embed.add_field(name = "Example Usage:",
                        value = "!asin `[product link]` - Extracts ASIN from the provided product link. \n"
                                "!rev `[product link]` - Extracts product reviews from the provided product link. \n"
                                "!info `[product link]` - Retrieves detailed product information using the provided link. \n"
                                "!info-asin `[ASIN]` - Retrieves detailed product information using the provided ASIN. \n",
                        inline = False
                        )
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!ping':
        latency = bot.latency
        embed = discord.Embed(title = "Ping",
                              description = f"Pong! Bot latency is {latency * 1000:.2f}ms.",
                              color = 0x008000,
                              )
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)


    # if message == '!status':
    #     repsonse = await Response('https://www.amazon.com').response()
    #     if repsonse == 200:
    #         embed = discord.Embed(title = "Status", description = f'Status code: 200', color = 0x008000)
    #         embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
    #         embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
    #         embed.timestamp = datetime.now()

    #         await user.send(embed = embed)
    #     else:
    #         embed = discord.Embed(title = "Status", description = repsonse, color = 0xFF0000)
    #         embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
    #         embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
    #         embed.timestamp = datetime.now()

    #         await user.send(embed = embed)
            
                        
async def send_product_data(datas, channel):
    """
    This function takes a user input and a suer object as parameters, call the Amazon class to get product data using ASIN,
    creates a discord embed with the product data, and send the embed to the user.

    Args:
        -userInput (str): User input.
        -user (discord.User): User object.

    Returns:
        -None
    """
    try:        
        name = datas['product_name']
        hyperlink = f"https://www.walmart.com/{datas['canonical_url']}"
        embed = discord.Embed(title = name, url = hyperlink, color = 0xff9900)
        embed.add_field(name = 'Price', value = f"${datas['current_price']}", inline = False)
        embed.add_field(name = 'Availability', value = datas['availability'], inline = False)
        # embed.add_field(name = "Store", value = f"[{datas['Store']}]({datas['Store link']})", inline = False)
        embed.add_field(name = 'Rating', value = datas['average_rating'], inline = False)
        embed.add_field(name = 'Review count', value = datas['review_count'], inline = False)
        embed.set_thumbnail(url = datas['image_link'])
        embed.timestamp = datetime.now()
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        await channel.send(embed = embed)
    except Exception as e:
        print(f"Error 2 {e}")
        await channel.send(f'Content loading error. Please try again in few minutes.')

async def getDataByProductSearch(scheduler, userInput, channel):
    links_to_pages = []
    links_to_pages.append(userInput)
    # https://www.walmart.com/search?q=earbuds&affinityOverride=default&page=2
    for i in range(2, 4):
        links_to_pages.append(f"{userInput}&page={i}")
        
    # file path
    file_path = "scraped.txt"
    
    # Check if file exists. If not, create it.
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
    
    in_text_file = []
    
    # Read file to retrieve asins
    with open("scraped.txt", "r") as file:
        in_text_file = file.readlines()
    
    # Remove leading and trailing spaces
    in_text_file = [item_id.strip() for item_id in in_text_file]
    for link_to_page in links_to_pages:
        try:            
            walmart = Walmart(link_to_page)
            print(link_to_page)
            products_data = await walmart.product_data_by_search()                        
            for product_data in products_data:
                if product_data["item_id"] in in_text_file:
                    continue
                with open("scraped.txt", "a") as file:
                    file.write(f"{product_data['item_id']}\n")
                await send_product_data(product_data, channel)
        except Exception as e:
            print(f"Error is happening here {e}")    
    scheduler.add_job(
        getDataByProductSearch, 
        'date', 
        run_date=datetime.utcnow() + timedelta(minutes=10), 
        args=[scheduler, userInput, channel]
    )
    
    
async def getProductDataCategory():
    from discordsFunctionalities.runBot import find_and_print_channel_by_name
    # Channel ID, 1202138418906406932
    channel = find_and_print_channel_by_name("electronics")
    electronics_links = []
    with open("./Electronics.txt", "r") as electronics_file:
        electronics_links = electronics_file.readlines()        
    electronics_links = [electronic_link.strip() for electronic_link in electronics_links]
    for electronic_link in electronics_links: 
        link_to_be_scraped = electronic_link 
        
        for i in range(2, 26):
            response_code = 0
            walmart = Walmart(link_to_be_scraped)
            print(f"{link_to_be_scraped}\n")
            returned_data = await walmart.product_data_by_category()
            data = returned_data[0]
            if not data:
                print("Faced a block....")                
                time_to_delay = random.randint(50, 60)
                await asyncio.sleep(time_to_delay)
                returned_data = await walmart.product_data_by_category()
                data = returned_data[0]
                response_code = returned_data[1]
            if response_code == 403:
                break
            if not data:
                continue
            data = json.loads(data)
            products_data = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"]                            
            formatted_prod_data = await walmart.extract_product_details(products_data)
            for product in formatted_prod_data:                
                await send_product_data(product, channel)
            link_to_be_scraped = f"{electronic_link}?page={i}&affinityOverride=default"