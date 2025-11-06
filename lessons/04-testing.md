# Lekcja 4: Testowanie i Debugowanie Skills

W tej lekcji nauczysz się jak testować, debugować i udoskonalać swoje skills.

## Dlaczego testowanie jest ważne?

Skills to instrukcje dla AI. AI interpretuje te instrukcje, ale:
- Może interpretować inaczej niż myślałeś
- Może pomijać niejednoznaczne fragmenty
- Może priorytetyzować niektóre instrukcje nad innymi

**Testowanie zapewnia, że skill działa jak zamierzasz!**

## Proces testowania skillu

```
1. Stwórz skill
      ↓
2. Przygotuj test cases
      ↓
3. Uruchom skill
      ↓
4. Porównaj z oczekiwaniami
      ↓
5. Zidentyfikuj problemy
      ↓
6. Popraw skill
      ↓
7. Testuj ponownie
```

## Przygotowanie test cases

### Test Case Template

Dla każdego skillu przygotuj:

```
Skill: [nazwa skillu]
Input: [co użytkownik mówi/pyta]
Expected Output: [czego oczekujesz]
Actual Output: [co faktycznie otrzymałeś]
Pass/Fail: [✅ / ❌]
Notes: [obserwacje]
```

### Przykład test cases dla "task-analyzer"

```markdown
## Test Case 1: Simple Task
Input: "I need to write a blog post"
Expected:
- Task breakdown into subtasks
- Time estimates
- Prioritization
- Clear next action
Pass: [To be filled after test]

## Test Case 2: Unclear Task
Input: "I need to do the thing"
Expected:
- Asks clarifying questions
- Doesn't make assumptions
- Helps user specify task
Pass: [To be filled after test]

## Test Case 3: Complex Task
Input: "I need to build a web app with auth, database, and API"
Expected:
- Breaks into major components
- Identifies dependencies
- Realistic time estimates
- Mentions potential risks
Pass: [To be filled after test]
```

## Testowanie krok po kroku

### Krok 1: Podstawowy test działania

Najpierw sprawdź czy skill w ogóle się uruchamia.

```bash
# W katalogu z .claude/skills/
claude
/task-analyzer
```

**Oczekiwany rezultat:**
- Skill się aktywuje (brak błędów)
- Claude odpowiada w kontekście skillu
- Nie ma błędów składni lub ładowania

**Jeśli to nie działa:** Zobacz sekcję "Debugowanie" poniżej.

### Krok 2: Test podstawowej funkcjonalności

Użyj najprostszego możliwego test case.

```
/task-analyzer
"I need to make dinner"
```

**Co sprawdzić:**
- ✅ Czy skill zrozumiał zadanie?
- ✅ Czy zastosował workflow ze skill.md?
- ✅ Czy output ma oczekiwany format?
- ✅ Czy ton komunikacji jest zgodny z instrukcjami?

### Krok 3: Test edge cases

Testuj nietypowe sytuacje:

**Niejasne zapytanie:**
```
/task-analyzer
"I need to do it"
```
Oczekiwane: Skill zadaje pytania doprecyzowujące

**Bardzo złożone zadanie:**
```
/task-analyzer
"Build a complete e-commerce platform"
```
Oczekiwane: Skill dzieli na zarządzalne komponenty

**Zadanie z ograniczeniami:**
```
/task-analyzer
"Write a blog post, but I only have 1 hour"
```
Oczekiwane: Skill uwzględnia constraint czasu

### Krok 4: Test consistency

Uruchom ten sam test kilka razy.

```
Test 1: /task-analyzer "Write a blog post"
Test 2: /task-analyzer "Write a blog post"
Test 3: /task-analyzer "Write a blog post"
```

**Co sprawdzić:**
- Czy format odpowiedzi jest spójny?
- Czy skill stosuje te same zasady?
- Czy jakość jest stabilna?

## Debugowanie - Częste problemy

### Problem 1: Skill się nie ładuje

**Symptom:** `Error: Skill 'xxx' not found`

**Możliwe przyczyny:**
- Nieprawidłowa ścieżka
- Błąd w nazwie skillu
- Katalog .claude/ nie istnieje w obecnej lokalizacji

**Rozwiązanie:**
```bash
# Sprawdź strukturę
ls -la .claude/skills/

# Sprawdź czy plik skill.md istnieje
cat .claude/skills/[nazwa-skillu]/skill.md

# Sprawdź czy jesteś w poprawnym katalogu
pwd
```

### Problem 2: Skill działa, ale ignoruje instrukcje

**Symptom:** Claude odpowiada, ale nie przestrzega formatów/zasad

**Możliwe przyczyny:**
- Instrukcje są zbyt ogólne
- Brak konkretnych przykładów
- Sprzeczne instrukcje

**Rozwiązanie:**

❌ **Złe - zbyt ogólne:**
```markdown
Be helpful and organized.
```

✅ **Dobre - konkretne:**
```markdown
## Output Format

Always structure your response as:

1. **Summary** (2-3 sentences)
2. **Main Points** (bullet list)
3. **Action Items** (numbered list with deadlines)

Example:
**Summary**
This task involves...

**Main Points**
- Point 1
- Point 2
```

### Problem 3: Skill jest za bardzo "kreatywny"

**Symptom:** Claude dodaje treści nie określone w skillu

**Możliwe przyczyny:**
- Brak jasnych granic (boundaries)
- Zbyt ogólne instrukcje
- Brak "stay on topic" reminders

**Rozwiązanie:**

Dodaj do skillu:

```markdown
## Strict Guidelines

- Stay focused ONLY on [specific scope]
- Do NOT add information outside of [specific area]
- If user asks about unrelated topics, politely redirect to the skill's scope

## Scope Boundaries

✅ This skill handles:
- [Item 1]
- [Item 2]

❌ This skill does NOT handle:
- [Item 1] → refer to [other skill]
- [Item 2] → suggest [alternative]
```

### Problem 4: Inconsistent outputs

**Symptom:** Każde wywołanie daje różny format/styl

**Rozwiązanie:**

Dodaj sekcję z przykładami i szablonem:

```markdown
## Response Template

Use EXACTLY this structure for every response:

```
[Section 1 Header]
[Content guidelines]

[Section 2 Header]
[Content guidelines]

[Section 3 Header]
[Content guidelines]
```

Example:
[Pełny przykład używający tego template]

**IMPORTANT**: Always follow this template. Do not skip sections.
```

### Problem 5: Skill nie zadaje pytań

**Symptom:** Skill zakłada zamiast pytać

**Rozwiązanie:**

```markdown
## When Information is Missing

If you don't know:
- [Critical info 1] → ASK: "Could you clarify [...]?"
- [Critical info 2] → ASK: "What is [...]?"
- [Critical info 3] → ASK: "Do you have [...]?"

Do NOT make assumptions. Always ask first.

Example:
User: "Help me with the project"
Your response: "I'd be happy to help! To provide the best assistance, could you tell me:
1. What type of project is this?
2. What stage are you at currently?
3. What specific aspect do you need help with?"
```

## Iteracyjne udoskonalanie

Skills rzadko są perfekcyjne od pierwszej wersji. Użyj tego procesu:

### Wersja 1: Minimum Viable Skill
```markdown
You are X. Do Y.
```

**Test → Zbierz feedback**

### Wersja 2: Dodaj strukturę
```markdown
You are X.

## Scope
- Do Y
- In way Z

## Guidelines
- Rule 1
- Rule 2
```

**Test → Zbierz feedback**

### Wersja 3: Dodaj format i przykłady
```markdown
[Previous content]

## Output Format
[Template]

## Examples
[Full example]
```

**Test → Zbierz feedback**

### Wersja 4: Dodaj boundaries i edge cases
```markdown
[Previous content]

## Scope Boundaries
✅ / ❌

## Edge Cases
- If X, then Y
- If A, then B
```

## Checklist finalizacji skillu

Przed uznaniem skillu za "gotowy", sprawdź:

- [ ] Skill ładuje się bez błędów
- [ ] Podstawowa funkcjonalność działa
- [ ] Format outputu jest spójny
- [ ] Edge cases są obsługiwane
- [ ] Skill zadaje pytania gdy brak informacji
- [ ] Scope boundaries są jasne
- [ ] Przykłady są reprezentatywne
- [ ] Testowałeś 3+ razy dla consistency
- [ ] Inni mogą użyć skillu bez wyjaśnień (jeśli ma być współdzielony)

## Test suite template

Stwórz plik `test-[skill-name].md` obok skillu:

```markdown
# Test Suite: [Skill Name]

## Test 1: Basic Functionality
**Input**: [...]
**Expected**: [...]
**Actual**: [...]
**Pass**: ✅ / ❌
**Notes**: [...]

## Test 2: Edge Case - [Description]
**Input**: [...]
**Expected**: [...]
**Actual**: [...]
**Pass**: ✅ / ❌
**Notes**: [...]

## Test 3: Consistency Check
**Run**: 3 times
**Results**:
- Run 1: [consistent/inconsistent]
- Run 2: [consistent/inconsistent]
- Run 3: [consistent/inconsistent]
**Pass**: ✅ / ❌

## Test 4: Clarifying Questions
**Input**: [Vague request]
**Expected**: [Asks for clarification]
**Actual**: [...]
**Pass**: ✅ / ❌

## Test 5: Scope Boundaries
**Input**: [Out of scope request]
**Expected**: [Politely refuses, suggests alternative]
**Actual**: [...]
**Pass**: ✅ / ❌

## Overall Score: [X/5 tests passed]

## Issues to Fix:
1. [Issue 1]
2. [Issue 2]

## Improvements for Next Version:
1. [Improvement 1]
2. [Improvement 2]
```

## Metryki jakości skillu

Jak ocenić czy skill jest dobry?

### 1. Funkcjonalność (40%)
- ✅ Robi to co powinien
- ✅ Obsługuje edge cases
- ✅ Brak błędów

### 2. Spójność (30%)
- ✅ Konsistentny output format
- ✅ Przewidywalne zachowanie
- ✅ Stabilna jakość

### 3. Użyteczność (20%)
- ✅ Łatwy w użyciu
- ✅ Jasne instrukcje
- ✅ Pomaga osiągnąć cel

### 4. Maintainability (10%)
- ✅ Kod/instrukcje są czytelne
- ✅ Łatwo modyfikować
- ✅ Dobrze udokumentowany

**Cel: 80%+ w każdej kategorii**

## Ćwiczenie praktyczne

1. Wybierz jeden ze swoich skills
2. Stwórz test suite (min. 5 test cases)
3. Uruchom wszystkie testy
4. Zidentyfikuj co działa, co nie działa
5. Popraw skill
6. Uruchom testy ponownie
7. Powtarzaj aż 100% testów przechodzi

## Co dalej?

Gratulacje! Ukończyłeś wszystkie główne lekcje! 🎉

### Następne kroki:

1. **Eksperymentuj**: Twórz własne skills dla swoich potrzeb
2. **Udostępniaj**: Współdziel skills z zespołem/społecznością
3. **Ucz się**: Analizuj skills stwor by innych
4. **Iteruj**: Stale udoskonalaj swoje skills

### Zaawansowane tematy do eksploracji:

- Multi-mode skills (jeden skill, wiele trybów)
- Skill chains (łączenie wielu skills)
- Context-aware skills (skills świadome kontekstu projektu)
- Interactive skills (skills z interaktywnymi pytaniami)

---

**Gratulacje!** Ukończyłeś Lekcję 4 i cały kurs! 🎓🎉

Teraz jesteś w stanie:
- Tworzyć proste i zaawansowane skills ✅
- Strukturyzować instrukcje ✅
- Testować i debugować ✅
- Iteracyjnie udoskonalać ✅
- Oceniać jakość skills ✅

**Powodzenia w tworzeniu swoich skills!** 🚀
