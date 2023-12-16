from colorama import init, Fore

# Inicializa o Colorama (pode ser necessário instalá-lo primeiro: pip install colorama)
init(autoreset=True)

message = """
{0}Hello, I'm Gabe, a university student currently living in Brazil.{1}
{2}I use this channel to capture and share my life experiences.{3}

{4}Connect with me:{5}
- {4}Instagram, Twitch, Twitter: {6}@NashiSore{7}

{8}For commercial inquiries, you can reach me at:{9}
{8}nashisore.contato@gmail.com{9}
"""

# Use códigos de cor do Colorama para realçar partes do texto
formatted_message = message.format(Fore.CYAN, Fore.RESET, Fore.YELLOW, Fore.RESET, Fore.GREEN, Fore.RESET, Fore.BLUE, Fore.RESET, Fore.MAGENTA, Fore.RESET)

print(formatted_message)
