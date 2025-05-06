from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Configurações iniciais
TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo token do seu bot

# Dados sobre a FURIA
proximos_jogos = """
🗓️ Próximos jogos da FURIA:
• 15/05 - FURIA vs MIBR - ESL Pro League
• 20/05 - FURIA vs NAVI - BLAST Premier
• 25/05 - FURIA vs FaZe - IEM Rio
"""

elenco = """
🎮 Elenco Principal:
• arT (Capitão)
• KSCERATO
• yuurih
• FalleN
• chelo
• guerri (Técnico)
"""

curiosidades = """
🔍 Curiosidades:
- Fundada em 2017
- Nome vem do estilo de jogo agressivo
- Maior conquista: 2º no ESL Pro League S11
- Mascote oficial: O lobo guará
"""

redes_sociais = """
📱 Redes Sociais da FURIA:
• Twitter: @FURIA
• Instagram: @furiagg
• Site: furia.gg
• YouTube: FURIA Esports
"""

# Função de start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ['Próximos jogos', 'Elenco atual'],
        ['Curiosidades', 'Redes Sociais'],
        ['Enviar mensagem de apoio']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "👋 Olá, fã da FURIA! Eu sou o FURIA FanBot!\n\n"
        "O que você quer saber hoje? Escolha uma opção abaixo ou digite "
        "'vamo furia' para uma surpresa! 🔥",
        reply_markup=reply_markup
    )

# Comando secreto para verdadeiros fãs
async def secret_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if "vamo furia" in text:
        await update.message.reply_text("🔥 VAMO FURIA! 🔥\n\n"
                                      "🎶 DUM DUM DUM FURIA! 🎶")
    elif "art" in text:
        await update.message.reply_text("AR TUDO! 🎯")
    elif "fallen" in text:
        await update.message.reply_text("LENDA DO CS BRASILEIRO! 🐺")

# Função principal para lidar com mensagens
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    if text == 'Próximos jogos':
        await update.message.reply_text(proximos_jogos)
    elif text == 'Elenco atual':
        await update.message.reply_text(elenco)
    elif text == 'Curiosidades':
        await update.message.reply_text(curiosidades)
    elif text == 'Redes Sociais':
        await update.message.reply_text(redes_sociais)
    elif text == 'Enviar mensagem de apoio':
        await update.message.reply_text("📩 Digite sua mensagem de apoio para a equipe FURIA:")
    else:
        await secret_command(update, context)
        if not any(x in text.lower() for x in ["vamo furia", "art", "fallen"]):
            await update.message.reply_text(
                f"✅ Sua mensagem foi enviada para a equipe!\n\n"
                f"'{text}'\n\n"
                f"#GoFURIA 🔥\n"
                f"📢 Compartilhe nosso bot: @furiafanofc_bot"
            )

def main() -> None:
    # Cria a Application e passa o token
    application = Application.builder().token(TOKEN).build()
    
    # Registra os handlers
    application.add_handler(CommandHandler("start", start))
    
    # Handler para mensagens
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, secret_command), 
        group=1
    )
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message), 
        group=2
    )
    
    # Roda o bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()