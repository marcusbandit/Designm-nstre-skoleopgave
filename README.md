# Quiz Program README

## Om programmet

Dette program er et simpelt quizspil, der tillader brugeren at svare på multiple choice-spørgsmål. Det er designet med brug af Model-View-Controller (MVC) arkitekturen, hvilket sikrer en klar adskillelse mellem programmets data (Model), brugergrænsefladen (View), og logikken der forbinder de to (Controller). Denne struktur gør programmet nemmere at vedligeholde og udvide i fremtiden.

## Valg af designmønstre

### Model-View-Controller (MVC)

MVC-mønstret er valgt for at skabe en velorganiseret og modulær kodebase. Dette mønster tillader en effektiv separation af ansvarsområder:

- **Model (`QuizModel`)**: Indeholder data og logik for programmet. Dette inkluderer spørgsmål, svarmuligheder, og den korrekte svarmulighed. Modellen er ansvarlig for at administrere applikationens data og forretningslogik.

- **View (`QuizView`)**: Præsenterer data for brugeren og indsamler brugerinput. Dette omfatter at vise spørgsmål, svarmuligheder, og feedback på brugerens svar. View'et er ansvarlig for den visuelle repræsentation af programmet.

- **Controller (`QuizController`)**: Fungerer som bindeleddet mellem model og view. Controlleren håndterer brugerinput, opdaterer modellen og refresher view'et baseret på brugerens interaktioner. Dette sikrer, at dataflyden i programmet er velorganiseret og effektiv.

### Fordelene ved MVC

- **Modularitet**: MVC-mønstret tillader udviklere at modificere eller opdatere enkelte dele af programmet (model, view, eller controller) uafhængigt af hinanden, hvilket gør det nemmere at vedligeholde og udvide.
- **Genanvendelighed**: Komponenter, især modeller og views, kan genbruges i forskellige dele af programmet eller i andre projekter.
- **Separation af ansvar**: Klar adskillelse mellem brugergrænsefladen og forretningslogikken gør koden mere læsbar og lettere at forstå.

## Programfunktioner

- Viser et udvalg af multiple choice-spørgsmål om programmering og Python.
- Tillader brugeren at vælge et svar og giver feedback på, om det valgte svar er korrekt eller ej.
- Holder styr på brugerens score gennem quizzen.
- Viser brugerens endelige score ved afslutningen af quizzen.

Programmet demonstrerer effektiv anvendelse af MVC-designmønstret i en real-world applikation, hvilket gør det til et fremragende eksempel på, hvordan softwareudviklingsprincipper kan anvendes til at skabe velstrukturerede og vedligeholdelsesvenlige applikationer.
