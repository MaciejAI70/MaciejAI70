#!/usr/bin/env python3
"""
Skills Instructor - Interaktywny nauczyciel Claude Code Skills
"""

import os
import sys
import time
from pathlib import Path

class SkillsInstructor:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.current_lesson = 0
        self.user_name = ""

    def clear_screen(self):
        """Czyści ekran konsoli"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def print_header(self, text):
        """Wyświetla ładny nagłówek"""
        print("\n" + "="*70)
        print(f"  {text}")
        print("="*70 + "\n")

    def print_box(self, text, color="blue"):
        """Wyświetla tekst w ramce"""
        lines = text.split('\n')
        max_len = max(len(line) for line in lines)

        colors = {
            "blue": "\033[94m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "red": "\033[91m",
            "end": "\033[0m"
        }

        color_code = colors.get(color, colors["blue"])
        end_code = colors["end"]

        print(color_code + "┌" + "─" * (max_len + 2) + "┐")
        for line in lines:
            print("│ " + line.ljust(max_len) + " │")
        print("└" + "─" * (max_len + 2) + "┘" + end_code)

    def slow_print(self, text, delay=0.03):
        """Wyświetla tekst znak po znaku dla efektu"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def wait_for_enter(self, message="Naciśnij ENTER aby kontynuować..."):
        """Czeka na naciśnięcie ENTER"""
        input(f"\n{message}")

    def get_user_choice(self, options):
        """Pobiera wybór użytkownika z listy opcji"""
        while True:
            print("\nWybierz opcję:")
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")

            try:
                choice = input("\nTwój wybór (numer): ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice_num
                else:
                    print(f"❌ Proszę wybierz numer od 1 do {len(options)}")
            except ValueError:
                print("❌ Proszę wpisz numer")
            except KeyboardInterrupt:
                print("\n\nDo zobaczenia! 👋")
                sys.exit(0)

    def welcome(self):
        """Ekran powitalny"""
        self.clear_screen()
        print("\n\n")
        print("  ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗")
        print("  ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝")
        print("  ███████╗█████╔╝ ██║██║     ██║     ███████╗")
        print("  ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║")
        print("  ███████║██║  ██╗██║███████╗███████╗███████║")
        print("  ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝")
        print("\n")
        print("     I N S T R U K T O R   C L A U D E   C O D E")
        print("\n")

        time.sleep(1)

        self.print_box(
            "Witaj w interaktywnym kursie tworzenia Skills!\n"
            "Przeprowadzę Cię krok po kroku przez cały proces.\n\n"
            "Przygotuj się na praktyczną naukę! 🚀",
            "green"
        )

        self.wait_for_enter()

        self.user_name = input("\n🙋 Jak mam się do Ciebie zwracać? ").strip()
        if not self.user_name:
            self.user_name = "Uczniu"

        print(f"\n✨ Miło Cię poznać, {self.user_name}! Zaczynamy przygodę!")
        time.sleep(2)

    def main_menu(self):
        """Główne menu"""
        while True:
            self.clear_screen()
            self.print_header(f"Skills Instructor - Witaj {self.user_name}!")

            print("📚 MENU GŁÓWNE\n")

            options = [
                "🎓 Lekcja 1: Czym są Skills?",
                "🛠️  Lekcja 2: Stwórz swój pierwszy Skill",
                "🧮 Lekcja 3: Skill z parametrami (Kalkulator)",
                "🌐 Lekcja 4: Zaawansowany Skill (Web Fetch)",
                "🌍 Lekcja 5: Language Learning Skills (Nauka języków)",
                "📖 Dokumentacja i materiały",
                "🧪 Testuj swoje Skills",
                "❓ Pomoc",
                "🚪 Wyjście"
            ]

            choice = self.get_user_choice(options)

            if choice == 1:
                self.lesson_1_introduction()
            elif choice == 2:
                self.lesson_2_first_skill()
            elif choice == 3:
                self.lesson_3_calculator()
            elif choice == 4:
                self.lesson_4_advanced()
            elif choice == 5:
                self.lesson_5_language_learning()
            elif choice == 6:
                self.show_documentation()
            elif choice == 7:
                self.test_skills()
            elif choice == 8:
                self.show_help()
            elif choice == 9:
                self.goodbye()
                break

    def lesson_1_introduction(self):
        """Lekcja 1: Wprowadzenie do Skills"""
        self.clear_screen()
        self.print_header("Lekcja 1: Czym są Skills w Claude Code?")

        lessons = [
            {
                "title": "Definicja Skills",
                "content": """Skills w Claude Code to specjalne rozszerzenia, które dodają
nowe możliwości do Twojego asystenta AI.

Wyobraź sobie to jak 'supermoc' dla Claude'a - każdy skill
uczy go nowej umiejętności!"""
            },
            {
                "title": "Jak działają Skills?",
                "content": """Skills są zapisane w plikach markdown (.md) w specjalnym
katalogu .claude/skills/

Gdy uruchamiasz skill w Claude Code, jego instrukcje są
ładowane i Claude wie, jak wykonać nowe zadanie."""
            },
            {
                "title": "Przykłady zastosowań",
                "content": """Możesz stworzyć skills do:
• Przetwarzania danych (CSV, JSON, PDF)
• Generowania raportów
• Automatyzacji zadań
• Integracji z API
• Analizy kodu
• I wiele więcej!"""
            },
            {
                "title": "Struktura projektu",
                "content": """Typowa struktura:

projekt/
└── .claude/
    └── skills/
        └── nazwa-skillu/
            └── skill.md

Plik skill.md zawiera instrukcje dla Claude'a."""
            }
        ]

        for i, lesson in enumerate(lessons, 1):
            print(f"\n📝 Część {i}/4: {lesson['title']}\n")
            print(lesson['content'])

            if i < len(lessons):
                self.wait_for_enter("Naciśnij ENTER aby kontynuować...")
                print("\n" + "-"*70 + "\n")

        print("\n" + "="*70)
        self.print_box(
            "Gratulacje! Ukończyłeś Lekcję 1! ✅\n\n"
            "Teraz rozumiesz czym są Skills i jak działają.\n"
            "W następnej lekcji stworzymy Twój pierwszy Skill!",
            "green"
        )

        self.wait_for_enter()

    def lesson_2_first_skill(self):
        """Lekcja 2: Pierwszy Skill"""
        self.clear_screen()
        self.print_header("Lekcja 2: Stwórz swój pierwszy Skill")

        print(f"Świetnie {self.user_name}! Teraz stworzymy razem Twój pierwszy skill.\n")
        print("Będzie to prosty 'Hello World' skill, który nauczy Cię podstaw.\n")

        self.wait_for_enter("Naciśnij ENTER aby rozpocząć...")

        # Krok 1: Struktura katalogów
        self.clear_screen()
        print("\n🗂️  KROK 1: Tworzenie struktury katalogów\n")
        print("Najpierw musimy stworzyć odpowiednią strukturę folderów.\n")

        print("Wykonam teraz komendę:")
        print("  mkdir -p .claude/skills/hello-skill\n")

        if self.get_yes_no("Czy mogę stworzyć te katalogi?"):
            try:
                os.makedirs(".claude/skills/hello-skill", exist_ok=True)
                print("✅ Katalogi zostały utworzone!")
            except Exception as e:
                print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        # Krok 2: Tworzenie pliku skill.md
        self.clear_screen()
        print("\n📝 KROK 2: Tworzenie pliku skill.md\n")
        print("Teraz stworzymy główny plik skill.md z instrukcjami.\n")

        skill_content = """You are a friendly greeting expert. When this skill is activated, you will:

1. Greet the user warmly
2. Ask them how they are doing
3. Provide an interesting fact or motivational quote
4. Wish them a great day

Be enthusiastic and friendly in your responses!"""

        print("Zawartość pliku skill.md:")
        print("-" * 50)
        print(skill_content)
        print("-" * 50)

        if self.get_yes_no("\nCzy zapisać ten plik?"):
            try:
                skill_path = Path(".claude/skills/hello-skill/skill.md")
                skill_path.write_text(skill_content)
                print("✅ Plik skill.md został utworzony!")
            except Exception as e:
                print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        # Krok 3: Testowanie
        self.clear_screen()
        print("\n🧪 KROK 3: Testowanie Skillu\n")
        print("Twój pierwszy skill jest gotowy!\n")
        print("Aby go użyć w Claude Code, wpisz w terminalu:\n")
        print("  /hello-skill\n")
        print("lub jeśli używasz Claude Code z Python SDK:\n")
        print("  from claude import skill\n")
        print("  skill('hello-skill')\n")

        self.print_box(
            "Gratulacje! Stworzyłeś swój pierwszy Skill! 🎉\n\n"
            "To był prosty przykład, ale już wiesz jak to działa.\n"
            "W następnych lekcjach stworzymy bardziej zaawansowane skills!",
            "green"
        )

        self.wait_for_enter()

    def lesson_3_calculator(self):
        """Lekcja 3: Skill z parametrami"""
        self.clear_screen()
        self.print_header("Lekcja 3: Skill z parametrami - Kalkulator")

        print("W tej lekcji nauczysz się tworzyć skills, które przyjmują parametry.\n")
        print("Stworzymy zaawansowany kalkulator! 🧮\n")

        self.wait_for_enter("Naciśnij ENTER aby rozpocząć...")

        # Tworzenie struktury
        self.clear_screen()
        print("\n🗂️  Tworzenie struktury dla kalkulatora...\n")

        try:
            os.makedirs(".claude/skills/calculator", exist_ok=True)
            print("✅ Struktura utworzona!")
        except Exception as e:
            print(f"❌ Błąd: {e}")

        time.sleep(1)

        # Tworzenie skill.md
        calc_skill = """You are an advanced calculator skill. When activated, you can perform various mathematical operations.

## Capabilities

You can:
- Perform basic arithmetic (addition, subtraction, multiplication, division)
- Calculate percentages
- Work with exponents and roots
- Handle complex mathematical expressions
- Show step-by-step solutions

## Usage

When the user provides a mathematical expression or problem:
1. Parse the expression carefully
2. Perform the calculation
3. Show the result clearly
4. If helpful, explain the steps

## Examples

User: "Calculate 15% of 200"
Response:
- 15% of 200 = 0.15 × 200 = 30
- Answer: 30

User: "What's 2^8?"
Response:
- 2^8 = 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 256
- Answer: 256

Always be clear, precise, and helpful!"""

        try:
            skill_path = Path(".claude/skills/calculator/skill.md")
            skill_path.write_text(calc_skill)
            print("✅ Skill kalkulatora został utworzony!")
        except Exception as e:
            print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        self.clear_screen()
        print("\n📚 Czego się nauczyłeś:\n")
        print("1. ✅ Skills mogą mieć rozbudowane instrukcje")
        print("2. ✅ Możesz definiować różne tryby działania")
        print("3. ✅ Dobrze jest dodać przykłady użycia")
        print("4. ✅ Strukturyzacja instrukcji pomaga Claude'owi\n")

        print("Aby użyć kalkulatora, wpisz:")
        print("  /calculator\n")
        print("A następnie podaj wyrażenie matematyczne!\n")

        self.print_box("Lekcja 3 ukończona! ✅", "green")
        self.wait_for_enter()

    def lesson_4_advanced(self):
        """Lekcja 4: Zaawansowany Skill"""
        self.clear_screen()
        self.print_header("Lekcja 4: Zaawansowany Skill - Web Research")

        print("To jest najbardziej zaawansowana lekcja! 🚀\n")
        print("Stworzymy skill, który pomoże w research'u internetowym.\n")

        self.wait_for_enter()

        self.clear_screen()
        print("\n🗂️  Tworzenie zaawansowanego skillu...\n")

        try:
            os.makedirs(".claude/skills/web-research", exist_ok=True)

            advanced_skill = """You are a web research specialist skill. Your role is to help users gather, analyze, and synthesize information from the web.

## Core Capabilities

1. **Search Strategy**: Help users formulate effective search queries
2. **Source Evaluation**: Assess credibility and relevance of sources
3. **Information Synthesis**: Combine information from multiple sources
4. **Citation**: Provide proper references for all information

## Workflow

When activated, follow this process:

1. **Understand the Request**
   - What information is the user seeking?
   - What's the purpose (research, decision-making, learning)?
   - What level of depth is needed?

2. **Plan the Search**
   - Break down the topic into searchable components
   - Identify key terms and related concepts
   - Suggest search strategies

3. **Guide the Research**
   - Recommend reliable sources (academic, official, reputable)
   - Help evaluate information quality
   - Identify potential biases

4. **Synthesize Results**
   - Summarize key findings
   - Highlight important patterns or insights
   - Note conflicting information
   - Provide citations

## Best Practices

- Always verify information from multiple sources
- Distinguish between facts and opinions
- Note the date of information (important for time-sensitive topics)
- Be transparent about limitations and uncertainties
- Encourage critical thinking

## Example Usage

User: "I need to research renewable energy trends for 2024"

Your response should:
1. Clarify: What aspects? (technology, economics, policy?)
2. Suggest: Reputable sources (IEA, IRENA, academic journals)
3. Guide: Keywords to search for
4. Help: Organize and evaluate findings

Remember: Your goal is to make the user a better researcher!"""

            skill_path = Path(".claude/skills/web-research/skill.md")
            skill_path.write_text(advanced_skill)
            print("✅ Zaawansowany skill został utworzony!")

        except Exception as e:
            print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        self.clear_screen()
        print("\n🎓 Co wyróżnia zaawansowane skills:\n")
        print("1. 📋 Zdefiniowany workflow (przepływ pracy)")
        print("2. 🎯 Jasne capabilities (możliwości)")
        print("3. 📖 Szczegółowe instrukcje krok po kroku")
        print("4. ✨ Best practices (najlepsze praktyki)")
        print("5. 💡 Przykłady użycia\n")

        self.print_box(
            "Gratulacje! Ukończyłeś wszystkie główne lekcje! 🎉\n\n"
            "Teraz potrafisz tworzyć zarówno proste jak i\n"
            "zaawansowane skills dla Claude Code!",
            "green"
        )

        self.wait_for_enter()

    def lesson_5_language_learning(self):
        """Lekcja 5: Language Learning Skills"""
        self.clear_screen()
        self.print_header("Lekcja 5: Language Learning Skills - Nauka języków")

        print(f"Świetnie {self.user_name}! 🌍\n")
        print("W tej lekcji nauczysz się tworzyć interaktywnych nauczycieli języków.\n")
        print("Stworzymy dwa skills:")
        print("  1. 🇪🇸 Nauczyciel hiszpańskiego (A2)")
        print("  2. 🇬🇧 Nauczyciel angielskiego (A2)\n")

        self.wait_for_enter("Naciśnij ENTER aby rozpocząć...")

        # Wprowadzenie do koncepcji
        self.clear_screen()
        print("\n📚 Czym są Language Learning Skills?\n")
        print("To specjalne skills, które:")
        print("  • Prowadzą interaktywne lekcje")
        print("  • Generują teksty dostosowane do poziomu ucznia")
        print("  • Korygują wymowę i gramatykę")
        print("  • Budują pewność siebie w mówieniu\n")

        self.wait_for_enter()

        # Tworzenie Spanish Teacher
        self.clear_screen()
        print("\n🇪🇸 KROK 1: Tworzenie Spanish Teacher A2\n")

        if self.get_yes_no("Czy chcesz stworzyć nauczyciela hiszpańskiego?"):
            try:
                os.makedirs(".claude/skills/spanish-teacher-a2", exist_ok=True)

                spanish_skill = """Jesteś przyjaznym i cierpliwym nauczycielem języka hiszpańskiego 🇪🇸. Twój uczeń jest na poziomie A2.

## Twoja rola

Prowadzisz interaktywne lekcje czytania i konwersacji, pomagając uczniowi poprawić wymowę i płynność w mówieniu po hiszpańsku.

## Procedura lekcji

### 1. Generowanie tekstu 📖

Wygeneruj krótki, ciekawy akapit po hiszpańsku (3-4 zdania) dostosowany do poziomu A2.

**Tematyka codzienna:**
- Zakupy na rynku
- Podróż do nowego miasta
- Hobby i wolny czas
- Spotkanie z przyjaciółmi
- Jedzenie i restauracje
- Rodzina i dom
- Praca i nauka

**Format:**
```
📖 Texto para leer:

[Tekst po hiszpańsku]

🇵🇱 Tłumaczenie:

[Tłumaczenie na polski]
```

### 2. Słuchanie ucznia 🎧

Poczekaj na odpowiedź użytkownika, która może być:
- Nagranie audio (otrzymasz transkrypcję)
- Tekst napisany przez ucznia
- Informacja, że chce zacząć od konwersacji

### 3. Korekta i feedback ✅

**Jeśli odczyt był DOBRY:**
- ✨ Pochwal konkretnie: "¡Muy bien! Twoja wymowa słowa [słowo] była doskonała!"
- 🎯 Zadaj pytanie po hiszpańsku związane z tekstem
- 💬 Rozpocznij krótką konwersację

**Jeśli były BŁĘDY:**
- 📝 Wymień konkretne słowa z błędami
- 🔊 Podaj fonetyczną wymowę: `palabra → [pa-LA-bra]`
- 🔄 Poproś o powtórzenie tego fragmentu
- 💪 Zachęć: "No te preocupes, lo estás haciendo bien!"

### 4. Konwersacja 💬

Po poprawnym odczytaniu lub na życzenie ucznia:
- Zadawaj proste pytania po hiszpańsku związane z tekstem
- Używaj struktur gramatycznych poziomu A2
- Pomagaj formułować odpowiedzi
- Poprawiaj błędy delikatnie i konstruktywnie

**Przykładowe pytania:**
- ¿Qué compró María en el mercado?
- ¿Te gusta ir de compras? ¿Por qué?
- ¿Cuál es tu fruta favorita?

## Styl komunikacji 💫

### Bądź wspierający:
- Używaj emoji do wyrażania emocji
- Świętuj każdy sukces, nawet mały
- Traktuj błędy jako możliwość nauki
- Dostosuj tempo do ucznia

### Odpowiadaj krótko:
- Zwięzłe wyjaśnienia (2-3 zdania)
- Jedna koncepcja na raz
- Praktyczne przykłady
- Zachowaj dynamikę rozmowy

### Bądź pacjentny:
- Powtarzaj wyjaśnienia w różny sposób
- Daj czas na przemyślenie odpowiedzi
- Nie przytłaczaj zbyt wieloma informacjami
- Dopasuj poziom trudności

## Motto 💭

"¡Los errores son oportunidades para aprender! Cada palabra que practicas
te acerca a la fluidez. ¡Vamos!"

(Błędy to szanse na naukę! Każde słowo, które ćwiczysz, przybliża Cię
do płynności. Ruszamy!)"""

                skill_path = Path(".claude/skills/spanish-teacher-a2/skill.md")
                skill_path.write_text(spanish_skill)
                print("✅ Spanish Teacher A2 został utworzony!")
            except Exception as e:
                print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        # Tworzenie English Teacher
        self.clear_screen()
        print("\n🇬🇧 KROK 2: Tworzenie English Teacher A2\n")

        if self.get_yes_no("Czy chcesz stworzyć nauczyciela angielskiego?"):
            try:
                os.makedirs(".claude/skills/english-teacher-a2", exist_ok=True)

                english_skill = """You are a friendly and patient English teacher 🇬🇧🇺🇸. Your student is at A2 level (elementary).

## Your role

You conduct interactive reading and conversation lessons, helping the student improve their pronunciation and fluency in English.

## Lesson Procedure

### 1. Text Generation 📖

Generate a short, interesting paragraph in English (3-4 sentences) suitable for A2 level.

**Everyday topics:**
- Shopping at a supermarket
- Traveling to a new place
- Hobbies and free time
- Meeting friends
- Food and restaurants
- Family and home
- Work and study
- Daily routines

**Format:**
```
📖 Text to read:

[Text in English]

🇵🇱 Tłumaczenie:

[Polish translation]
```

### 2. Listening to the student 🎧

Wait for the user's response, which can be:
- Audio recording (you'll receive a transcription)
- Text written by the student
- Information that they want to start with conversation

### 3. Correction and feedback ✅

**If the reading was GOOD:**
- ✨ Give specific praise: "Great job! Your pronunciation of the word [word] was excellent!"
- 🎯 Ask a question in English related to the text
- 💬 Start a short conversation

**If there were ERRORS:**
- 📝 List specific words with mistakes
- 🔊 Provide phonetic pronunciation: `thought → [thawt]`
- 🔄 Ask to repeat that fragment
- 💪 Encourage: "Don't worry, you're doing great!"

### 4. Conversation 💬

After correct reading or at the student's request:
- Ask simple questions in English related to the text
- Use A2 level grammar structures
- Help formulate answers
- Correct mistakes gently and constructively

**Example questions:**
- What did Sarah buy at the store?
- Do you like shopping? Why or why not?
- What's your favorite type of food?

## Communication Style 💫

### Be supportive:
- Use emojis to express emotions
- Celebrate every success, even small ones
- Treat mistakes as learning opportunities
- Adjust pace to the student

### Keep it short:
- Concise explanations (2-3 sentences)
- One concept at a time
- Practical examples
- Maintain conversation flow

### Be patient:
- Repeat explanations in different ways
- Give time to think about answers
- Don't overwhelm with too much information
- Adjust difficulty level

## Motto 💭

"Mistakes are stepping stones to fluency! Every word you practice brings
you closer to speaking confidently. Let's go!"

(Błędy to kamienie milowe do płynności! Każde słowo, które ćwiczysz,
przybliża Cię do pewnego mówienia. Ruszamy!)"""

                skill_path = Path(".claude/skills/english-teacher-a2/skill.md")
                skill_path.write_text(english_skill)
                print("✅ English Teacher A2 został utworzony!")
            except Exception as e:
                print(f"❌ Błąd: {e}")

        self.wait_for_enter()

        # Podsumowanie
        self.clear_screen()
        print("\n🎓 Czego się nauczyłeś:\n")
        print("1. ✅ Tworzenie interaktywnych nauczycieli języków")
        print("2. ✅ Strukturyzacja lekcji (generowanie → słuchanie → korekta → konwersacja)")
        print("3. ✅ Konstruktywny feedback dla uczniów")
        print("4. ✅ Dostosowanie poziomu trudności (A2)")
        print("5. ✅ Budowanie wspierającego stylu komunikacji\n")

        print("Aby użyć nauczycieli, wpisz:")
        print("  /spanish-teacher-a2  - dla lekcji hiszpańskiego")
        print("  /english-teacher-a2  - dla lekcji angielskiego\n")

        self.print_box(
            "Gratulacje! Stworzyłeś language learning skills! 🎉\n\n"
            "Teraz możesz uczyć się języków z pomocą Claude!\n"
            "Możesz też stworzyć własne skills dla innych języków:\n"
            "niemiecki, francuski, włoski, japoński...",
            "green"
        )

        self.wait_for_enter()

    def show_documentation(self):
        """Pokazuje dokumentację"""
        self.clear_screen()
        self.print_header("Dokumentacja i Materiały")

        print("\n📚 Dostępne materiały:\n")
        print("1. Oficjalna dokumentacja Claude Code")
        print("   https://docs.claude.com/\n")
        print("2. Przykładowe skills w folderze:")
        print("   ./skills/\n")
        print("3. Szablony w folderze:")
        print("   ./templates/\n")
        print("4. README projektu")
        print("   ./README.md\n")

        self.print_box(
            "💡 Wskazówka:\n\n"
            "Najlepszym sposobem nauki jest praktyka!\n"
            "Eksperymentuj z własnymi pomysłami na skills.",
            "yellow"
        )

        self.wait_for_enter()

    def test_skills(self):
        """Testowanie skills"""
        self.clear_screen()
        self.print_header("Testowanie Skills")

        print("\n🧪 Jak testować swoje skills:\n")
        print("1. Upewnij się, że struktura katalogów jest prawidłowa:")
        print("   .claude/skills/nazwa-skillu/skill.md\n")
        print("2. Uruchom Claude Code w tym katalogu\n")
        print("3. Użyj komendy: /nazwa-skillu\n")
        print("4. Sprawdź czy skill działa zgodnie z oczekiwaniami\n")
        print("5. W razie problemów, sprawdź:\n")
        print("   • Czy plik skill.md istnieje")
        print("   • Czy instrukcje są jasne i jednoznaczne")
        print("   • Czy nazwa skillu jest poprawna\n")

        print("\n📝 Utworzone skills w tym projekcie:\n")

        claude_dir = Path(".claude/skills")
        if claude_dir.exists():
            skills = [d.name for d in claude_dir.iterdir() if d.is_dir()]
            if skills:
                for skill in skills:
                    print(f"  ✅ {skill}")
            else:
                print("  (brak utworzonych skills)")
        else:
            print("  (katalog .claude/skills nie istnieje jeszcze)")

        self.wait_for_enter()

    def show_help(self):
        """Pokazuje pomoc"""
        self.clear_screen()
        self.print_header("Pomoc")

        print("\n❓ Często zadawane pytania:\n")
        print("Q: Gdzie znajdują się pliki skills?")
        print("A: W katalogu .claude/skills/nazwa-skillu/skill.md\n")

        print("Q: Jak uruchomić skill?")
        print("A: W Claude Code użyj komendy /nazwa-skillu\n")

        print("Q: Czy mogę modyfikować istniejące skills?")
        print("A: Tak! Po prostu edytuj plik skill.md\n")

        print("Q: Co zrobić jeśli skill nie działa?")
        print("A: Sprawdź:\n")
        print("   1. Ścieżkę do pliku")
        print("   2. Poprawność składni w skill.md")
        print("   3. Czy nazwa skillu nie zawiera spacji\n")

        print("Q: Gdzie mogę znaleźć więcej przykładów?")
        print("A: W folderze ./skills/ oraz dokumentacji Claude Code\n")

        self.wait_for_enter()

    def get_yes_no(self, question):
        """Pobiera odpowiedź tak/nie"""
        while True:
            answer = input(f"{question} (t/n): ").strip().lower()
            if answer in ['t', 'tak', 'y', 'yes']:
                return True
            elif answer in ['n', 'nie', 'no']:
                return False
            else:
                print("Proszę odpowiedz 't' (tak) lub 'n' (nie)")

    def goodbye(self):
        """Pożegnanie"""
        self.clear_screen()
        print("\n\n")
        print("  ╔═══════════════════════════════════════════════════════════╗")
        print("  ║                                                           ║")
        print(f"  ║     Dziękuję za naukę, {self.user_name}! ✨                    ")
        print("  ║                                                           ║")
        print("  ║     Mam nadzieję, że kurs był pomocny!                   ║")
        print("  ║                                                           ║")
        print("  ║     Pamiętaj:                                             ║")
        print("  ║     • Praktyka czyni mistrza                              ║")
        print("  ║     • Eksperymentuj z własnymi pomysłami                  ║")
        print("  ║     • Nie bój się błędów - to najlepsza nauka!            ║")
        print("  ║                                                           ║")
        print("  ║     Powodzenia w tworzeniu swoich skills! 🚀              ║")
        print("  ║                                                           ║")
        print("  ╚═══════════════════════════════════════════════════════════╝")
        print("\n\n")

def main():
    """Główna funkcja programu"""
    try:
        instructor = SkillsInstructor()
        instructor.welcome()
        instructor.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Do zobaczenia!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Wystąpił błąd: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
