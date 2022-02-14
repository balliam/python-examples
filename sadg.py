@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message}, ({channel})")

    if message.author == client.user:
        return

        if user_message.lower() == '!queue':
            queue_list = str(message.author).split("#")[0]
            wait_list.append(queue_list)
            await message.channel.send('Added to the Queue!')
            return

    if message.channel.name == 'queue-list':
        if user_message.lower() == '!clist':
            wait_list.clear()
            await message.channel.send('The list has been cleared!')
            return
        elif user_message.lower() == '!qlist':
            await message.channel.send(wait_list)
            return