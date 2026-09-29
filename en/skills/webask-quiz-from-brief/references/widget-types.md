# WebAsk question types and their fields

Reference for the `webask-quiz-from-brief` skill. Open it when the type you need is
not in the selection table inside `SKILL.md`, or when a question needs finer
configuration.

Only the fields that actually change behaviour are listed. The full schema comes
back from `get_quiz_structure` for an existing survey: if unsure about a field
name, look at a live example there.

## Text and numbers

| Type | What it is | Main fields |
|---|---|---|
| `input` | single or multi-line answer | `inputPlaceholder`, `inputIsTextarea`, `inputLimitMin`, `inputLimitMax` |
| `number` | a number | `numberMin`, `numberMax`, `inputPlaceholder` |
| `fio` | a name parsed into parts | `fioWithPatronymic`, `fioSurnamePlaceholder`, `fioNamePlaceholder` |
| `email` | email with format checking | `emailPlaceholder`, `emailWidth` |
| `phone` | phone with country selection | `phoneDefaultCountry`, `phoneStrictValidation`, `phoneAllowedCountries` |
| `datetime` | date and time | `dateTimeType`, `dateTimeFormatOfDate`, `dateTimeFormatOfTime` |

## Choice

| Type | What it is | Main fields |
|---|---|---|
| `dropdown` | single or multiple choice from a list | `dropdownMultiple`, `dropdownOther`, `dropdownRandomize`, `dropdownEntities`, `dropdownScores`, `noneOfAbove` |
| `yesno` | yes or no | `yesNoIcon`, `yesNoTextEntities` |
| `ranking` | put items in order | `rankingEntities`, `rankingRandomize`, `rankingWithImages` |
| `pair` | pairwise comparison | `pairItemEntities`, `pairShowImages`, `pairStepByStep` |

`carryForward` on `dropdown` and `ranking` brings forward the options a respondent
chose earlier.

## Ratings and scales

| Type | What it is | Main fields |
|---|---|---|
| `rating` | stars, hearts, smileys | `ratingCount`, `ratingFigure`, `ratingStartValue`, `ratingScores` |
| `scale` | numeric scale with edge labels | `scaleCount`, `scaleStartValue`, `scaleLabelLeft`, `scaleLabelRight` |
| `nps` | likelihood-to-recommend scale | same fields as `scale` |
| `slider` | slider | `sliderMin`, `sliderMax`, `sliderStep` |
| `matrix` | a set of ratings over one list of criteria | `matrixChoiceType`, `matrixRowEntities`, `matrixColEntities`, `matrixIsAllRequired` |

`nps` is not the same as a ten-point `scale`: it has its own analytics in reports.
For "how likely are you to recommend", use `nps`.

## Files, map, embedded

| Type | What it is | Main fields |
|---|---|---|
| `file` | file or photo upload | `fileFormats` |
| `map` | a pin on a map | `mapCenterLat`, `mapCenterLng`, `mapZoom`, `mapTheme`, `mapMinMarks`, `mapMaxMarks` |
| `html` | custom markup block | `htmlCode`, `htmlIsEmbedded` |
| `booking` | appointment booking against a schedule | `bookingSchedulerId`, `bookingNameWidgetId`, `bookingPhoneWidgetId` |
| `payment` | payment inside the survey | `paymentFixedAmount`, `paymentTypes`, `paymentYookassaAccountId` |

`booking` and `payment` depend on settings created in the web app: a schedule and a
merchant account. Without them the question will not work — warn the person rather
than adding it silently.

## Screens without a question

| Type | What it is | Main fields |
|---|---|---|
| `welcome` | welcome screen | `welcomeLabel`, `welcomeWithQuestionCount`, `welcomeWithResponseTime` |
| `message` | a text screen between questions | `messageLabel`, `messageWithButton` |
| `submit` | submit screen with consent | `submitTerms`, `submitTermsText`, `submitLabel` |
| `finish` | thank-you page | `finishLabel`, `finishAnswerText`, `finishNextUrl`, `promoCode`, `maxScore` |
| `screenout` | end of the road for unsuitable respondents | `finishLabel`, `finishNextUrl` |

`finish` is mandatory: without it the respondent hits a blank page after the last
question.

## Commonly confused

- **Ratings are not collected as text.** An `input` asking for "a score from 1 to
  5" destroys the analytics.
- **Option lists are not collected as text.** Free answers cannot be grouped.
- **Phone and email have their own types.** Contacts collected through `input` are
  half unusable.
- **Ten similar ratings are a `matrix`,** not ten `rating` questions in a row.