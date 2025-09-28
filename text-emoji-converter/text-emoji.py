import demoji


demoji.download_codes()
text = "Yesterday was amazing 😍! I woke up early ⏰, enjoyed a hot coffee ☕, and went for a walk in the park 🌳🏞️. The sun was shining brightly 🌞 and I saw many colorful flowers 🌸🌼🌺. Later, I met my friends 👬 and we played football ⚽ until evening 🌆. At night 🌙, I relaxed by watching a movie 🎬 with popcorn 🍿 and then went to sleep 😴."

print(demoji.findall(text))