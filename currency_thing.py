import discord
import asyncio
import time
from forex_python.converter import CurrencyRates as cr

client = discord.Client()

hashtable = {
'HUF' : "Hungarian Forint :flag_hu:", 
'KRW' : "South Korean Won :flag_kr:", 
'CNY' : "Chinese Yuan :flag_cn:", 
'RUB' : "Russian Ruble :flag_ru:", 
'SEK' : "Swedish Krona :flag_se:", 
'TRY' : "Turkish Lira :flag_tr:", 
'PHP' : "Philippine Piso :flag_ph:", 
'CZK' : "Czech Koruna :flag_cz:", 
'THB' : "Thai Bhat :flag_th:", 
'PLN' : "Polish Zloty :flag_pl:", 
'EUR' : "European Euro :flag_eu:", 
'MYR' : "Malaysian Ringgit :flag_my:", 
'HKD' : "Hong Kong Dollar :flag_hk:", 
'AUD' : "Australian Dollar :flag_au:", 
'HRK' : "Croatian Kuna :flag_hr:", 
'CAD' : "Canadian Dollar :flag_ca:", 
'JPY' : "Japanese Yen :flag_jp:", 
'BGN' : 'Bulgarian Lev :flag_bg:', 
'RON' : "Romanian Leu :flag_ro:", 
'CHF' : "Swiss Franc :flag_ch:", 
'ILS' : "Israeli New Shekel :flag_il:", 
'NOK' : "Norwegian Krone :flag_no:", 
'BRL' : "Brazilian Real :flag_br:", 
'MXN' : "Mexican Peso :flag_mx:", 
'INR' : "Indian Rupee :flag_in:", 
'GBP' : "Great British Pound :flag_gb:", 
'DKK' : "Danish Krone :flag_dk:", 
'SGD' : "Singapore Dollar :flag_sg:", 
'IDR' : "Indonesian Rupiah :flag_id:", 
'NZD' : "New Zealand Dollar :flag_nz:", 
'ZAR' : "South African Rand :flag_za:"
}

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')
	while (1 == 1):
		output = ""
		c = cr()
		rates = c.get_rates('USD')
		print (rates)
		c_list = []
		for i in rates:
			c_list.append(i)
		print (c_list)
		timestamp = ("%s"%(time.strftime("%c")))
		await client.send_message(client.get_channel(CHANNEL ID GOES HERE), 'PRICES OF USD:dollar: BY WORLD CURRENCIES AS OF %s'%(timestamp))
		for i in c_list:
			output += (("%s : %s"%(hashtable[i], rates[i])) + "\n")
			print(output)
		await client.send_message(client.get_channel(CHANNEL ID GOES HERE), output)
		print("sleeping for 4 hours")
		time.sleep(60*60*4)

client.run(BOT TOKEN GOES HERE)
