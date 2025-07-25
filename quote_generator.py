import random

quotes = [
    "Будь собой; все остальные роли уже заняты. — Оскар Уайльд",
    "Делай, что можешь, с тем, что имеешь, там, где ты есть. — Теодор Рузвельт",
    "Жизнь — это то, что с тобой происходит, пока ты строишь планы. — Джон Леннон",
    "Успех — это умение двигаться от поражения к поражению, не теряя энтузиазма. — Уинстон Черчилль",
    "Если хочешь иметь то, чего никогда не имел, начни делать то, что никогда не делал. — Неизвестный автор",
    "Счастье — это не пункт назначения, а способ путешествовать. — Маргарет Ли Ранбек"
]

def show_random_quote():
    quote = random.choice(quotes)
    print("\n🎯 Случайная цитата дня:\n")
    print(f"💬 {quote}\n")

if __name__ == "__main__":
    show_random_quote()
