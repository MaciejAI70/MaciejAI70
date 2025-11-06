# Lekcja 1: Wprowadzenie do Claude Code Skills

## Czym są Skills?

Skills w Claude Code to specjalne instrukcje, które rozszerzają możliwości asystenta AI. Wyobraź sobie je jako "supermoc" dla Claude'a - każdy skill uczy go nowej umiejętności lub specjalizacji.

## Podstawowa koncepcja

```
┌─────────────────────────────────────┐
│  Claude (podstawowa wersja)         │
│  - Potrafi: ogólna konwersacja      │
│  - Rozumie: różne tematy ogólnie    │
└─────────────────────────────────────┘
                 +
┌─────────────────────────────────────┐
│  Skill (np. "Code Reviewer")        │
│  - Specjalizacja w code review      │
│  - Konkretne workflow                │
│  - Best practices                    │
└─────────────────────────────────────┘
                 =
┌─────────────────────────────────────┐
│  Claude + Skill                     │
│  - Potrafi wszystko co wcześniej    │
│  - PLUS: profesjonalny code review  │
│  - Używa strukturyzowanego procesu  │
└─────────────────────────────────────┘
```

## Jak działają Skills?

1. **Tworzysz plik skill.md** z instrukcjami
2. **Umieszczasz go w `.claude/skills/nazwa-skillu/`**
3. **Aktywujesz skill** przez `/nazwa-skillu` w Claude Code
4. **Claude otrzymuje dodatkowe instrukcje** i wie jak się zachować

## Struktura pliku skill.md

Plik skill.md to zwykły plik markdown zawierający instrukcje. Claude je czyta i stosuje.

### Przykład minimalny

```markdown
You are a friendly greeter. When activated, you greet the user warmly.
```

### Przykład strukturalny

```markdown
You are a task organizer. When this skill is activated, you:

1. Help break down complex tasks
2. Prioritize using proven methods
3. Create actionable plans

## Guidelines
- Be clear and concise
- Ask questions if context is missing
- Focus on practical steps

Remember: Your goal is to help users achieve their tasks efficiently!
```

## Anatomia dobrego skillu

Dobry skill zawiera:

### 1. Rola / Persona
```markdown
You are a [specialized role]...
```
Definiuje "kim" jest Claude gdy skill jest aktywny.

### 2. Scope / Zakres
```markdown
When this skill is activated, you:
- Function 1
- Function 2
- Function 3
```
Co dokładnie skill robi.

### 3. Guidelines / Wytyczne
```markdown
## Guidelines
- Guideline 1
- Guideline 2
```
Jak skill powinien się zachowywać.

### 4. Przykłady (opcjonalne ale polecane)
```markdown
## Example
User: [query]
Your response: [response]
```
Pokazują oczekiwane zachowanie.

## Gdzie skills są używane?

Skills są używane wszędzie tam gdzie potrzebujesz:

- 🎯 **Specjalizacji**: Ekspert w konkretnej dziedzinie
- 📋 **Struktury**: Spójny format odpowiedzi
- 🔄 **Workflow**: Określony proces pracy
- 🎨 **Stylu**: Konkretny ton komunikacji
- 🧩 **Integracji**: Współpraca z narzędziami/API

## Przykłady zastosowań

### Dla programistów:
- Code reviewer
- Test generator
- Documentation writer
- Bug analyzer
- Refactoring assistant

### Dla projektów:
- Task planner
- Meeting summarizer
- Decision maker
- Risk assessor

### Dla danych:
- CSV analyzer
- JSON formatter
- Data validator
- Report generator

### Dla nauki:
- Study planner
- Quiz generator
- Concept explainer
- Exercise creator

## Drzewo decyzyjne: Czy potrzebuję skillu?

```
Czy masz powtarzalne zadanie?
├─ NIE → Możesz użyć Claude'a bezpośrednio
└─ TAK → Czy wymaga specjalizacji/struktury?
    ├─ NIE → Możesz użyć Claude'a bezpośrednio
    └─ TAK → Stwórz skill! ✅
```

## Korzyści z używania Skills

### 1. Spójność
Skill zapewnia, że Claude zawsze odpowiada w ten sam, strukturalny sposób.

### 2. Specjalizacja
Skill może zawierać szczegółową wiedzę specjalistyczną.

### 3. Reużywalność
Raz stworzony skill możesz używać wielokrotnie.

### 4. Współdzielenie
Możesz udostępnić skill innym (lub użyć cudzego).

### 5. Organizacja
Skills pomagają organizować różne "tryby" pracy z Claude.

## Co dalej?

W następnej lekcji stworzysz swój pierwszy skill od podstaw!

Przejdź do: `02-first-skill.md`

---

## Ćwiczenie do przemyślenia

Pomyśl o zadaniach, które wykonujesz regularnie. Które z nich mogłyby skorzystać na stworzeniu dedykowanego skillu?

Zapisz 3 pomysły:
1. _______________________
2. _______________________
3. _______________________

Wrócimy do nich gdy nauczysz się tworzyć skills!
