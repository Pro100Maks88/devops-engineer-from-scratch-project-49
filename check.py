import sys
print("Python path:", sys.path)

try:
    import brain_games
    print("✅ Пакет brain_games найден!")
    from brain_games.cli import welcome_user
    print("✅ Импорт welcome_user успешен!")
except ImportError as e:
    print("❌ Ошибка:", e)
