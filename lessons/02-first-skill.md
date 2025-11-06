# Lekcja 2: Twój Pierwszy Skill

W tej lekcji stworzymy razem Twój pierwszy skill krok po kroku.

## Cel

Stworzyć prosty, działający skill typu "Hello World", który nauczy Cię podstaw.

## Skill: Friendly Greeter

Nasz pierwszy skill będzie:
- Witał użytkownika ciepło
- Pytał jak się czuje
- Dawał motywacyjny cytat
- Życzył udanego dnia

## Krok 1: Struktura katalogów

### Teoria

Claude Code szuka skills w określonej lokalizacji:
```
projekt/
└── .claude/
    └── skills/
        └── [nazwa-skillu]/
            └── skill.md
```

### Praktyka

W terminalu (w katalogu swojego projektu):

```bash
mkdir -p .claude/skills/friendly-greeter
```

**Co to robi?**
- `mkdir` = make directory (stwórz katalog)
- `-p` = create parent directories (stwórz też katalogi nadrzędne)
- `.claude/skills/friendly-greeter` = ścieżka do utworzenia

**Sprawdź czy się udało:**
```bash
ls -la .claude/skills/
```

Powinieneś zobaczyć katalog `friendly-greeter/`.

## Krok 2: Stwórz plik skill.md

### Teoria

Plik `skill.md` zawiera instrukcje dla Claude'a. Claude czyta ten plik gdy aktywujesz skill.

### Praktyka

Stwórz plik `.claude/skills/friendly-greeter/skill.md` z zawartością:

```markdown
You are a friendly greeter who brightens people's day.

## Your Role

When this skill is activated, you:
1. Greet the user with warmth and enthusiasm
2. Ask how they are doing today
3. Share an interesting fact or motivational quote
4. Wish them a wonderful day ahead

## Guidelines

- Be genuinely friendly and warm
- Use positive, uplifting language
- Keep the interaction brief but meaningful
- Adapt your energy to match the user's mood if they share it

## Example Interaction

User: /friendly-greeter

Your response:
"Hello there! 🌟 It's wonderful to see you! How are you doing today?

Here's something to brighten your day: Did you know that smiling, even when
you don't feel like it, can actually improve your mood? It's called the
facial feedback hypothesis!

Whatever you're working on today, I hope it goes amazingly well. You've got this! ✨"

Remember: Your goal is to make the user feel welcomed and energized!
```

**Zapisz plik!**

### Wyjaśnienie struktury

Przeanalizujmy co napisaliśmy:

```markdown
You are a friendly greeter who brightens people's day.
```
↑ **Persona**: Definuje "kim" jest Claude

```markdown
## Your Role
When this skill is activated, you:
1. ...
2. ...
```
↑ **Scope**: Lista konkretnych działań

```markdown
## Guidelines
- ...
- ...
```
↑ **Wytyczne**: Jak się zachować

```markdown
## Example Interaction
```
↑ **Przykład**: Pokazuje oczekiwane zachowanie

```markdown
Remember: ...
```
↑ **Przypomnienie**: Główny cel skillu

## Krok 3: Testowanie skillu

### Sposób 1: Claude Code CLI

Jeśli używasz Claude Code w terminalu:

```bash
claude
```

Potem w sesji:
```
/friendly-greeter
```

### Sposób 2: Bezpośrednie wywołanie

W katalogu z `.claude/skills/`:
```
claude skill friendly-greeter
```

### Co powinieneś zobaczyć?

Claude powinien:
✅ Ciepło Cię przywitać
✅ Zapytać jak się czujesz
✅ Podzielić się ciekawostką lub cytatem
✅ Życzyć miłego dnia

Jeśli tak się stało - **gratulacje!** Twój pierwszy skill działa! 🎉

## Krok 4: Eksperymentowanie

Teraz spróbuj zmodyfikować skill. Oto kilka pomysłów:

### Modyfikacja 1: Zmień ton

Zmień w `skill.md`:
```markdown
- Be genuinely friendly and warm
```

Na:
```markdown
- Be professional yet friendly
- Use business-appropriate language
```

**Testuj i obserwuj różnicę!**

### Modyfikacja 2: Dodaj więcej funkcji

Dodaj do sekcji "When this skill is activated, you:":
```markdown
5. Ask what the user plans to work on today
6. Offer a relevant productivity tip
```

**Testuj znowu!**

### Modyfikacja 3: Zmień styl cytatów

W Guidelines dodaj:
```markdown
- Share quotes related to technology and programming
- Focus on coding motivation
```

**Zobacz jak się zmienia!**

## Debugowanie - Co jeśli nie działa?

### Problem: "Skill nie został znaleziony"

✅ **Sprawdź**:
1. Czy ścieżka jest dokładnie: `.claude/skills/friendly-greeter/skill.md`
2. Czy jesteś w katalogu który ma folder `.claude/`
3. Czy nazwa skillu jest poprawna (bez spacji)

### Problem: "Skill działa ale nie jak oczekiwano"

✅ **Sprawdź**:
1. Czy instrukcje są jasne i konkretne?
2. Czy użyłeś przykładów?
3. Spróbuj być bardziej szczegółowy w opisie

### Problem: "Claude ignoruje niektóre instrukcje"

✅ **To normalne!**
- Claude stara się być pomocny, czasem interpretuje instrukcje
- Użyj mocniejszych sformułowań: "Always...", "Must...", "Never..."
- Dodaj przykłady pokazujące dokładnie co chcesz

## Kluczowe wnioski z Lekcji 2

✅ Skills to pliki `.md` w `.claude/skills/[nazwa]/skill.md`
✅ Struktura: Persona + Scope + Guidelines + Examples
✅ Testujesz przez `/nazwa-skillu`
✅ Możesz modyfikować i eksperymentować
✅ Jasne instrukcje = lepsze rezultaty

## Ćwiczenie

Stwórz własny prosty skill! Pomysły:

1. **Morning Planner**: Pomaga zaplanować dzień
2. **Break Reminder**: Przypomina o przerwach i relaksie
3. **Code Commenter**: Pomaga pisać komentarze do kodu
4. **Idea Validator**: Pomaga ocenić pomysły

Użyj tej samej struktury co `friendly-greeter`.

## Co dalej?

W następnej lekcji stworzymy bardziej zaawansowany skill z parametrami!

Przejdź do: `03-advanced-skills.md`

---

**Gratulacje!** Ukończyłeś Lekcję 2! 🎓

Teraz rozumiesz:
- Jak stworzyć strukturę dla skillu ✅
- Jak napisać instrukcje w skill.md ✅
- Jak testować skill ✅
- Jak debugować problemy ✅
