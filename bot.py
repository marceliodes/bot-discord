# Bot Python buat nyari jawaban
import discord
import random as rdm
import os
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Variabel buat random jawaban pilihan ganda
    Jawaban = ['A', 'B', 'C', 'D']

    # Variabel buat random jawaban kerang
    KerangAjaib = ['Iya', 'Tidak', 'Bisa jadi']

    # Buat jawaban
    if '>jawaban' in message.content:
        response = rdm.choice(Jawaban)
        await message.channel.send(response)

    # Buat Kerang
    elif '>kerang' in message.content:
        response = rdm.choice(KerangAjaib)
        await message.channel.send(response)

    # Ini about mengenai bot
    elif message.content == '>about':
        about = """Bot digunakan untuk mencari jawaban pilihan ganda. Awalnya bermula ketika UAS dan UU datang namun jawaban yang ada di otak tak kunjung datang,
\n lalu salah satu penduduk server ada yang mengeluh dan bilang "coba ada random generating buat jawaban jadi enak kalo ngasal".
\n Setelah mendengar perkataan itu, akhirnya manusia gabut ini terpikir untuk membuat bot discord dengan tujuan membantu para #TeamNgasal lebih nyaman dalam membidik jawaban.
\n Dan akhirnya jadi juga bot ini, walaupun sudah terpikirkan sejak lama namun baru sempat mengerjakannya.
        Kreator - Marcelio Desendra Adivio
        Tanggal dibuat - 3 Oktober 2020
        Akun IG - @marcelio.da
        Akun Twitter - @MarcelioDA"""

        await message.channel.send(about)

    # Ini untuk bantuan mengenai perintah bot
    elif message.content == '>help':
        await message.channel.send("""'>jawaban' untuk meminta jawaban kepada bot
        '>kerang' jika kebingungan dan membutuhkan pencerahan
        '>about' untung mengetahui tentang bot""")
    
    # Jika perintah tidak dikenali
    else:
        response = "Perintah salah, coba ketik '>help' untuk mengetahui perintah/input."
        await message.channel.send(response)

client.run("NzYxODA1Nzg3NjI1OTQ3MTUw.X3f87Q.U3QUYR2ArRAeCaO12aSYJRexB2U")

print("Bot Discord is stop")