# Architektura Skills Instructor

## Przegląd

Skills Instructor to kompleksowy system nauczania tworzenia skills dla Claude Code. Jest zaprojektowany jako interaktywne narzędzie edukacyjne z modułową strukturą.

## Struktura projektu

```
MaciejAI70/
│
├── README.md                          # Główna dokumentacja projektu
├── QUICKSTART.md                      # Szybki start (5 min)
├── ARCHITECTURE.md                    # Ten plik - architektura systemu
│
├── skills-instructor.py               # 🎓 Główny interaktywny nauczyciel
│   │
│   ├── SkillsInstructor (klasa)
│   │   ├── welcome()                  # Ekran powitalny
│   │   ├── main_menu()                # Menu główne
│   │   ├── lesson_1_introduction()    # Lekcja 1: Teoria
│   │   ├── lesson_2_first_skill()     # Lekcja 2: Pierwszy skill
│   │   ├── lesson_3_calculator()      # Lekcja 3: Skills z parametrami
│   │   ├── lesson_4_advanced()        # Lekcja 4: Zaawansowane
│   │   ├── show_documentation()       # Dokumentacja
│   │   ├── test_skills()              # Narzędzia testowe
│   │   └── show_help()                # System pomocy
│   │
│   └── Utility methods
│       ├── print_header()             # Formatowanie UI
│       ├── print_box()                # Kolorowe ramki
│       ├── slow_print()               # Efekt pisania
│       └── get_user_choice()          # Input handling
│
├── skills/                            # 📚 Przykładowe skills
│   ├── beginner/                      # Dla początkujących
│   │   ├── hello-skill-example.md     # Najprostszy przykład
│   │   └── task-helper-example.md     # Skill z funkcjami
│   │
│   └── advanced/                      # Zaawansowane
│       └── code-reviewer-example.md   # Profesjonalny skill
│
├── lessons/                           # 📖 Materiały szkoleniowe
│   ├── 01-introduction.md             # Teoria: Czym są skills?
│   ├── 02-first-skill.md              # Praktyka: Pierwszy skill
│   ├── 03-advanced-skills.md          # Zaawansowane techniki
│   └── 04-testing.md                  # Testowanie i debugging
│
├── templates/                         # 📋 Szablony
│   ├── skill-template-basic.md        # Szablon dla prostych skills
│   └── skill-template-advanced.md     # Szablon dla zaawansowanych
│
└── .claude/                           # (Tworzony podczas nauki)
    └── skills/                        # Skills utworzone przez użytkownika
        ├── hello-skill/
        ├── calculator/
        ├── web-research/
        └── ... (inne utworzone przez użytkownika)
```

## Przepływ nauczania

```
Start
  │
  ▼
┌─────────────────┐
│ Welcome Screen  │ ← Personalizacja (imię użytkownika)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Main Menu     │ ◄──────────────┐
└────────┬────────┘                │
         │                          │
         ├─► Lekcja 1: Introduction │
         │   (Teoria)               │
         │                          │
         ├─► Lekcja 2: First Skill  │
         │   (Hands-on)             │
         │   • Tworzy strukturę     │
         │   • Pisze skill.md       │
         │   • Testuje              │
         │                          │
         ├─► Lekcja 3: Calculator   │
         │   (Parametry)            │
         │                          │
         ├─► Lekcja 4: Advanced     │
         │   (Profesjonalny skill)  │
         │                          │
         ├─► Documentation          │
         │   • Linki do zasobów     │
         │   • Lokalne materiały    │
         │                          │
         ├─► Test Skills            │
         │   • Lista skills         │
         │   • Porady testowe       │
         │                          │
         ├─► Help                   │
         │   • FAQ                  │
         │   • Troubleshooting      │
         │                          │
         └─► Exit ─────────────────►│
```

## Filozofia designu

### 1. Interaktywność
- **Guided Learning**: Użytkownik jest prowadzony krok po kroku
- **Hands-on Practice**: Tworzenie rzeczywistych skills podczas nauki
- **Immediate Feedback**: Możliwość natychmiastowego testowania

### 2. Progresywność
```
Level 1: Teoria (co to jest skill?)
    ↓
Level 2: Prosty skill (hello world)
    ↓
Level 3: Funkcjonalny skill (kalkulator)
    ↓
Level 4: Zaawansowany skill (web research)
```

### 3. Modułowość
Każdy komponent jest niezależny:
- Lekcje można przechodzić w dowolnej kolejności (choć zalecana jest sekwencja)
- Przykłady można studiować oddzielnie
- Szablony można używać niezależnie od lekcji

### 4. Dual-mode learning
Dwa tryby nauki:
- **Interactive** (skills-instructor.py): Prowadzony kurs
- **Self-paced** (pliki .md): Nauka we własnym tempie

## Komponenty systemu

### 1. Interaktywny Instruktor (skills-instructor.py)

**Odpowiedzialności:**
- Prowadzenie użytkownika przez lekcje
- Tworzenie struktur katalogów
- Generowanie przykładowych skills
- Walidacja i testowanie
- Interfejs użytkownika (menu, formatowanie)

**Kluczowe cechy:**
- Kolorowe outputy (ANSI colors)
- Obsługa błędów (KeyboardInterrupt, exceptions)
- Personalizacja (użytkownik podaje imię)
- Progress tracking (przez lekcje)

### 2. Przykładowe Skills (skills/)

**Cel:** Pokazać różne poziomy złożoności

**Beginner:**
- `hello-skill-example.md`: Absolute minimum
- `task-helper-example.md`: Wprowadzenie do struktury

**Advanced:**
- `code-reviewer-example.md`: Profesjonalny, pełny przykład

**Każdy przykład zawiera:**
- Pełny kod skillu
- Wyjaśnienie struktury
- Kluczowe elementy
- Sugestie modyfikacji

### 3. Materiały Szkoleniowe (lessons/)

**Format:** Markdown documents

**Struktura każdej lekcji:**
1. Wprowadzenie (co się nauczysz)
2. Teoria (koncepty)
3. Praktyka (kod, przykłady)
4. Ćwiczenia (do samodzielnego wykonania)
5. Podsumowanie (key takeaways)

**Progresja:**
- 01: Teoria i podstawy
- 02: Pierwszy prosty skill (hands-on)
- 03: Zaawansowane techniki
- 04: Testowanie i debugging

### 4. Szablony (templates/)

**Cel:** Ułatwić tworzenie nowych skills

**Basic template:**
- Minimalna struktura
- Placeholder'y do wypełnienia
- Przykład wypełnienia

**Advanced template:**
- Pełna profesjonalna struktura
- Wszystkie sekcje
- Checklist przed użyciem

## Flow danych

### Tworzenie skillu przez instruktora

```python
User → Lesson 2 → lesson_2_first_skill()
                        ↓
                  1. Tworzy katalog
                     os.makedirs(".claude/skills/hello-skill")
                        ↓
                  2. Generuje skill.md
                     Path.write_text(skill_content)
                        ↓
                  3. Instrukcje testowania
                     Pokazuje jak użyć /hello-skill
                        ↓
                  User testuje w Claude Code
```

### Samodzielna nauka

```
User → Czyta lessons/02-first-skill.md
         ↓
    Kopiuje strukturę
         ↓
    Tworzy własny skill
         ↓
    Testuje
         ↓
    Iteruje
```

## Decyzje architektoniczne

### Dlaczego Python zamiast Bash?

**Wybrano Python bo:**
- ✅ Lepsze formatowanie i UI (print_box, colors)
- ✅ Łatwiejsza obsługa błędów
- ✅ Bardziej czytelny kod dla początkujących
- ✅ Cross-platform (Linux, macOS, Windows)
- ✅ Bogatsza standard library

### Dlaczego pojedynczy plik Python?

**Wybrano monolith bo:**
- ✅ Prostszy deployment (jeden plik)
- ✅ Łatwiejszy do zrozumienia dla learnerów
- ✅ Nie wymaga instalacji dependencji
- ✅ Można łatwo skopiować/udostępnić

### Dlaczego Markdown dla lekcji?

**Wybrano .md bo:**
- ✅ Czytelny w raw form (nie wymaga renderowania)
- ✅ Wspierany przez GitHub
- ✅ Łatwy do edycji
- ✅ Może zawierać code blocks z syntax highlighting
- ✅ Standard dla dokumentacji

## Rozszerzalność

System jest zaprojektowany do łatwego rozszerzania:

### Dodanie nowej lekcji

1. Dodaj metodę `lesson_X_nazwa()` do klasy SkillsInstructor
2. Dodaj opcję w `main_menu()`
3. Opcjonalnie: Dodaj plik `.md` w `lessons/`

### Dodanie nowego przykładu

1. Stwórz plik w `skills/beginner/` lub `skills/advanced/`
2. Użyj spójnej struktury (zobacz istniejące przykłady)
3. Dodaj link w dokumentacji

### Dodanie nowego szablonu

1. Stwórz plik w `templates/`
2. Użyj [PLACEHOLDERS] dla miejsc do wypełnienia
3. Dodaj przykład wypełnienia
4. Dodaj checklist

## Best Practices dla maintainers

### Dodając nowe funkcje:

1. **Zachowaj prostotę**: System jest dla beginnerów
2. **Dodaj przykłady**: Każda nowa koncepcja = przykład
3. **Testuj z użytkownikami**: Czy intuicyjne?
4. **Dokumentuj**: Aktualizuj README i tę architekturę

### Kod Python (skills-instructor.py):

1. **Czytelność > Wydajność**: Kod jest też edukacyjny
2. **Komentuj nieliniowe flow**: Pomóż czytającym zrozumieć
3. **Obsługuj błędy gracefully**: Użytkownik = beginner
4. **User-friendly messages**: Jasne, pomocne komunikaty

### Materiały (lessons/):

1. **Struktura spójna**: Każda lekcja = ten sam format
2. **Progresywna złożoność**: Od prostego do zaawansowanego
3. **Praktyczne przykłady**: Pokazuj, nie tylko mów
4. **Ćwiczenia**: Daj możliwość praktyki

## Metryki sukcesu

Jak mierzyć czy system działa?

### Dla użytkownika:

- ✅ Może stworzyć działający skill w < 15 minut
- ✅ Rozumie kiedy używać skills
- ✅ Potrafi znaleźć pomoc gdy utknął
- ✅ Czuje się confident by eksperymentować

### Dla systemu:

- ✅ 90%+ instrukcji prowadzi do sukcesu
- ✅ Błędy są jasno komunikowane
- ✅ Przykłady działają out-of-the-box
- ✅ Dokumentacja odpowiada na najczęstsze pytania

## Przyszłe ulepszenia (V2+)

Możliwe rozszerzenia:

1. **Validator skills**: Automatyczna walidacja syntaksu skill.md
2. **Skills library**: Repozytorium gotowych skills
3. **Interactive testing**: Built-in test framework
4. **Version control integration**: Git workflow dla skills
5. **Team features**: Współdzielenie skills w zespole
6. **Advanced topics**: Multi-mode skills, skill chains

---

**Ostatnia aktualizacja:** 2025-11-06

**Wersja:** 1.0

**Maintainer:** Skills Instructor Team
