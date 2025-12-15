# Lekcja 5: Language Learning Skills - Nauka języków z Claude Code

## Wprowadzenie

Witaj w lekcji o tworzeniu skills do nauki języków! 🌍

W tej lekcji dowiesz się:
- Jak stworzyć interaktywnego nauczyciela języka
- Jak zaprojektować strukturę lekcji językowych
- Jak budować wspierający feedback dla uczniów
- Jak dostosować poziom trudności do ucznia

## Czym są Language Learning Skills?

Language Learning Skills to specjalistyczne skills, które:
- Prowadzą interaktywne lekcje języków obcych
- Korygują wymowę i gramatykę
- Dostosowują się do poziomu ucznia
- Budują pewność siebie w mówieniu

### Dlaczego warto tworzyć takie skills?

✅ **Personalizacja** - Każdy uczeń uczy się w swoim tempie
✅ **Dostępność** - Nauka 24/7, kiedy Ci wygodnie
✅ **Cierpliwość** - AI nie męczy się powtarzaniem
✅ **Brak stresu** - Bezpieczne środowisko do popełniania błędów
✅ **Interaktywność** - Natychmiastowy feedback

## Anatomia Language Learning Skill

### 1. Definicja roli nauczyciela

```markdown
You are a friendly and patient [LANGUAGE] teacher.
Your student is at [LEVEL] level.
```

**Kluczowe elementy:**
- Określ osobowość (friendly, patient, encouraging)
- Wskaż język nauczania
- Określ poziom ucznia (A1, A2, B1, B2, C1, C2)

### 2. Struktura lekcji

Typowa lekcja składa się z:

```markdown
## Lesson Procedure

1. Text Generation - Wygeneruj materiał do nauki
2. Student Input - Poczekaj na odpowiedź ucznia
3. Correction - Skoryguj błędy konstruktywnie
4. Conversation - Rozwijaj dialog
```

### 3. Format materiału

```markdown
📖 Text to read:
[Tekst w języku docelowym]

🇵🇱 Tłumaczenie:
[Tłumaczenie na polski]
```

### 4. System feedbacku

**Pozytywny feedback:**
```markdown
✨ Specific praise: "Great pronunciation of [word]!"
🎯 Follow-up question related to text
💬 Conversation starter
```

**Korekta błędów:**
```markdown
📝 List specific mistakes
🔊 Phonetic pronunciation: word → [pronunciation]
🔄 Ask for repetition
💪 Encouragement: "Don't worry, you're doing great!"
```

## Przykład: Spanish Teacher A2

Zobaczmy pełny przykład skutecznego language skill:

```markdown
Jesteś przyjaznym i cierpliwym nauczycielem języka hiszpańskiego 🇪🇸.
Twój uczeń jest na poziomie A2.

## Procedura lekcji

### 1. Generowanie tekstu 📖

Wygeneruj krótki akapit po hiszpańsku (3-4 zdania) z tematów:
- Zakupy
- Podróż
- Hobby
- Jedzenie
- Rodzina

Format:
📖 Texto para leer:
[Tekst hiszpański]

🇵🇱 Tłumaczenie:
[Polski]

### 2. Słuchanie ucznia 🎧
Czekaj na nagranie/transkrypcję/tekst

### 3. Korekta ✅

Jeśli dobrze:
- Pochwal konkretnie
- Zadaj pytanie po hiszpańsku
- Rozpocznij konwersację

Jeśli błędy:
- Wymień błędne słowa
- Podaj wymowę: palabra → [pa-LA-bra]
- Poproś o powtórzenie
- Zachęć!

### 4. Konwersacja 💬
- Proste pytania związane z tekstem
- Pomoc w formułowaniu odpowiedzi
- Delikatna korekta

## Styl komunikacji

- Używaj emoji
- Krótkie odpowiedzi (2-3 zdania)
- Świętuj sukcesy
- Traktuj błędy jako szansę
```

## Kluczowe zasady projektowania

### 1. Dostosowanie poziomu

**A1 (Beginner):**
- 2-3 proste zdania
- Słownictwo podstawowe (100-200 słów)
- Czas teraźniejszy głównie
- Tematy: przedstawienie się, rodzina, liczby

**A2 (Elementary):**
- 3-4 zdania
- Słownictwo rozszerzone (500+ słów)
- Czasy: teraźniejszy, przeszły, przyszły prosty
- Tematy: zakupy, podróż, hobby, praca

**B1 (Intermediate):**
- 5-6 zdań
- Bardziej złożone struktury
- Opinie i uzasadnienia
- Tematy: kultura, wiadomości, zainteresowania

### 2. Konstruktywny feedback

❌ **Źle:**
"This is wrong."
"You made a mistake."
"No, that's not correct."

✅ **Dobrze:**
"Almost perfect! Let me help with one word..."
"Great effort! Here's a small improvement..."
"You're doing well! Let's refine this part..."

### 3. Motywacja i wsparcie

```markdown
💪 Encouragement phrases:
- "¡Muy bien!" / "Great job!"
- "You're making progress!"
- "Don't worry, mistakes help us learn!"
- "Try again, you can do it!"

🎯 Progress recognition:
- "Your pronunciation is improving!"
- "I noticed you used [grammar] correctly!"
- "You remembered that word from last time!"
```

### 4. Interaktywność

**Dobre praktyki:**
- Zadawaj pytania związane z tekstem
- Zachęcaj do własnych zdań
- Proś o opinie i preferencje
- Twórz mini-dialogi

**Przykład dialogu:**
```
Teacher: "¿Te gusta ir de compras?"
Student: "Sí, me gusta."
Teacher: "¡Perfecto! ¿Qué te gusta comprar?"
Student: "Me gusta comprar... ropa?"
Teacher: "¡Excelente! ✨ 'Ropa' is correct! You can also say:
         'Me gusta comprar ropa nueva' (I like buying new clothes)"
```

## Dodatkowe funkcje

### 1. Słownictwo na żądanie

```markdown
When student asks about a word:
- Definition in target language (simple)
- Polish translation
- Phonetic pronunciation
- Example sentence in context
```

Przykład:
```
Student: "What does 'upset' mean?"

Teacher:
😟 "upset" [uhp-SET]
Definition: Feeling sad or worried
Polski: Zmartwiony, przygnębiony
Example: "I was upset when it rained."
```

### 2. Mini-quizy

```markdown
After 3-4 lessons:
- Quick vocabulary quiz (5 words)
- Fill in the blank exercises
- Simple translation practice
```

### 3. Ciekawostki kulturowe

```markdown
Include cultural notes:
- Holidays and traditions
- Food and cuisine
- Music and arts
- Useful expressions
- Regional differences
```

## Tworzenie własnego Language Skill

### Krok 1: Wybierz język i poziom

```bash
mkdir -p .claude/skills/[language]-teacher-[level]
cd .claude/skills/[language]-teacher-[level]
touch skill.md
```

Przykłady:
- `german-teacher-a1`
- `french-teacher-b1`
- `italian-teacher-a2`

### Krok 2: Napisz skill.md

```markdown
You are a friendly [LANGUAGE] teacher.
Your student is at [LEVEL] level.

## Lesson Procedure

1. Generate text (X sentences)
   Topics: [list topics]

2. Wait for student response

3. Provide feedback
   - If good: [praise + question]
   - If errors: [correction + encouragement]

4. Conversation
   - Ask questions
   - Help with answers
   - Gentle corrections

## Communication Style
- Use emojis
- Keep it short
- Be supportive
- Celebrate progress
```

### Krok 3: Dodaj specyficzne elementy języka

**Dla języka hiszpańskiego:**
```markdown
- Focus on: ser vs estar, por vs para
- Watch for: gender agreement
- Practice: rolling 'r', 'ñ' sound
```

**Dla języka niemieckiego:**
```markdown
- Focus on: der/die/das articles, cases
- Watch for: word order (verb second position)
- Practice: umlauts (ä, ö, ü), 'ch' sound
```

**Dla języka francuskiego:**
```markdown
- Focus on: tu vs vous, partitives
- Watch for: liaison, silent letters
- Practice: nasal vowels, 'r' sound
```

### Krok 4: Testuj i iteruj

1. Uruchom skill: `/[your-skill-name]`
2. Przeprowadź przykładową lekcję
3. Sprawdź czy:
   - Teksty są odpowiedniego poziomu?
   - Feedback jest konstruktywny?
   - Konwersacja płynie naturalnie?
   - Uczeń czuje się wspierany?

## Zaawansowane techniki

### 1. Adaptive difficulty

```markdown
Track student progress:
- If 3+ correct in row → slightly increase difficulty
- If 3+ errors in row → simplify text
- Adjust vocabulary complexity dynamically
```

### 2. Tematyczne ścieżki

```markdown
Offer themed learning paths:

/spanish-travel - Travel vocabulary
/spanish-business - Business Spanish
/spanish-food - Culinary terms
/spanish-culture - Cultural immersion
```

### 3. Speaking practice techniques

```markdown
Pronunciation drills:
1. Minimal pairs: ship/sheep, bit/beat
2. Tongue twisters for difficult sounds
3. Shadowing: repeat after model
4. Record and compare
```

### 4. Gamification

```markdown
Add game elements:
- 🏆 Points for correct answers
- 🌟 Achievements (10 lessons, 50 words learned)
- 📊 Progress tracking
- 🎯 Daily goals
```

## Best Practices checklist

✅ **Content:**
- [ ] Appropriate level (A1-C2)
- [ ] Relevant topics for level
- [ ] Cultural context included
- [ ] Clear learning objectives

✅ **Interaction:**
- [ ] Waits for student input
- [ ] Asks follow-up questions
- [ ] Encourages speaking
- [ ] Builds on previous lessons

✅ **Feedback:**
- [ ] Specific praise
- [ ] Constructive corrections
- [ ] Phonetic pronunciation help
- [ ] Examples in context

✅ **User Experience:**
- [ ] Friendly, patient tone
- [ ] Uses emojis appropriately
- [ ] Short, clear explanations
- [ ] Celebrates progress

✅ **Structure:**
- [ ] Clear lesson flow
- [ ] Consistent format
- [ ] Manageable chunks
- [ ] Natural conversation

## Przykłady gotowych skills

W katalogu `skills/languages/` znajdziesz:

### 1. Spanish Teacher A2
- Poziom elementary
- 3-4 zdania na lekcję
- Tłumaczenia na polski
- Wymowa fonetyczna
- Lokalizacja: `skills/languages/spanish-teacher-a2.md`

### 2. English Teacher A2
- Poziom elementary
- Everyday topics
- British vs American notes
- Common A2 challenges
- Lokalizacja: `skills/languages/english-teacher-a2.md`

## Instalacja i użycie

### Instalacja Spanish Teacher

```bash
# Utwórz katalog
mkdir -p .claude/skills/spanish-teacher-a2

# Skopiuj zawartość z przykładu
# (znajdziesz ją w skills/languages/spanish-teacher-a2.md)
# Skopiuj sekcję "Zawartość skill.md" do pliku:

nano .claude/skills/spanish-teacher-a2/skill.md
# Wklej zawartość i zapisz (Ctrl+O, Enter, Ctrl+X)
```

### Instalacja English Teacher

```bash
# Utwórz katalog
mkdir -p .claude/skills/english-teacher-a2

# Skopiuj zawartość z przykładu
# (znajdziesz ją w skills/languages/english-teacher-a2.md)

nano .claude/skills/english-teacher-a2/skill.md
# Wklej zawartość i zapisz
```

### Użycie

```bash
# Uruchom lekcję hiszpańskiego
/spanish-teacher-a2

# Uruchom lekcję angielskiego
/english-teacher-a2
```

## Ćwiczenia praktyczne

### Ćwiczenie 1: Stwórz Basic Language Skill

Wybierz język który znasz i stwórz prosty A1 skill:

1. Utwórz katalog: `.claude/skills/[language]-basic/`
2. Napisz `skill.md` z:
   - Krótką rolą nauczyciela (2-3 zdania)
   - Prostym tekstem do przeczytania (2 zdania)
   - Tłumaczeniem
   - Jednym pytaniem follow-up
3. Przetestuj skill
4. Zrób lekcję z prawdziwym tekstem

### Ćwiczenie 2: Dodaj cultural notes

Rozszerz istniejący skill o:
- 3 ciekawostki kulturowe
- Tradycyjne pozdrowienia
- Popularne wyrażenia idiomatyczne

### Ćwiczenie 3: Stwórz themed variant

Wybierz temat (np. travel, food, business) i:
1. Dostosuj słownictwo do tematu
2. Przygotuj 5 przykładowych tekstów
3. Dodaj specjalistyczne zwroty
4. Stwórz listę przydatnych fraz

### Ćwiczenie 4: Multi-level skill

Stwórz skill który:
- Pyta o poziom ucznia na początku
- Dostosowuje trudność tekstów
- Zmienia poziom bazując na wynikach
- Śledzi progres

## Troubleshooting

### Problem: Teksty za trudne/łatwe

**Rozwiązanie:**
```markdown
Add level indicators in prompt:

For A2:
- Use only present, past, future simple
- Vocabulary: 500 most common words
- Sentence length: 8-12 words max
- No idioms or complex grammar
```

### Problem: Brak spójności w lekcjach

**Rozwiązanie:**
```markdown
Add context tracking:

Remember from previous lessons:
- Words student struggled with
- Successfully learned vocabulary
- Preferred topics
- Common mistakes
```

### Problem: Za dużo tekstu na raz

**Rozwiązanie:**
```markdown
Chunk the content:

1. Short text (3-4 sentences)
2. One correction at a time
3. One follow-up question
4. Wait for response before continuing
```

## Inspiracje i zasoby

### Frameworks do nauki języków:

**CEFR Levels (A1-C2):**
- A1: Breakthrough
- A2: Waystage
- B1: Threshold
- B2: Vantage
- C1: Effective Operational Proficiency
- C2: Mastery

### Przydatne podejścia:

**Communicative Approach:**
- Focus on real-life communication
- Authentic materials
- Error tolerance
- Fluency over accuracy initially

**Task-Based Learning:**
- Complete meaningful tasks
- Use language as a tool
- Real-world relevance

**Natural Approach:**
- Comprehensible input
- Low-stress environment
- Focus on meaning not form

## Kolejne kroki

Po opanowaniu tworzenia language skills:

1. **Stwórz multi-skill suite**
   - Grammar teacher
   - Vocabulary builder
   - Pronunciation coach
   - Conversation partner

2. **Dodaj assessment**
   - Level testing
   - Progress tracking
   - Certification preparation

3. **Rozszerz o media**
   - Song lyrics analysis
   - Movie quote practice
   - News article reading

4. **Społeczność**
   - Share your skills
   - Collaborate on improvements
   - Build skill libraries

## Podsumowanie

Teraz wiesz jak:
- ✅ Tworzyć skuteczne language learning skills
- ✅ Dostosowywać poziom trudności (A1-C2)
- ✅ Budować konstruktywny feedback system
- ✅ Projektować interaktywne lekcje
- ✅ Dodawać cultural context
- ✅ Motywować i wspierać uczniów

### Key Takeaways:

1. **Patience is key** - Skill powinien być cierpliwy i wspierający
2. **Level-appropriate** - Dopasuj trudność do poziomu ucznia
3. **Interactive** - Pytaj, słuchaj, odpowiadaj
4. **Constructive** - Koryguj błędy delikatnie i konstruktywnie
5. **Cultural** - Wplątuj elementy kultury języka
6. **Consistent** - Zachowaj strukturę i format
7. **Fun** - Nauka powinna być przyjemnością! 🎉

## Zadanie domowe

1. Zainstaluj Spanish Teacher A2 lub English Teacher A2
2. Przeprowadź 3 lekcje
3. Zanotuj co działa, co można poprawić
4. Stwórz własny language skill dla języka który znasz
5. Podziel się swoim skillem z innymi!

---

**Następna lekcja:** Advanced Skills Patterns - Zaawansowane wzorce i techniki

**Poprzednia lekcja:** [04-testing.md](04-testing.md) - Testowanie skills

¡Buena suerte! Good luck! Powodzenia! 🌟
