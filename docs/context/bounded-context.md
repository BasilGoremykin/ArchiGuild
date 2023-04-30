# Диаграмма ограниченных контекстов

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()

Person(viewer, "Зритель", "Зритель на конференции")
Person(presenter, "Докладчик", "Докладчик на конференции")
Person(reviewer, "Рецензент", "Рецензирует доклады на конференции")

System(submission, "Submission System", "Система подачи докладов на конференции")
System(viewing, "Viewing System", "Система просмотра трансляций и записей докладов")
System(schedule, "Schedule Service", "Система расписаний трансляций докладов")
System(feedback, "Feedback Service", "Система получения обратной связи")

Container(submissionDb, "Submission Database", "Database", "Хранит информацию о поданных докладах")
Container(viewingDb, "Viewing Database", "Database", "Хранит метаданные о трансляциях, а так же записи выступлений")
Container(scheduleDb, "Schedule Database", "Database", "Хранит информацию о расписании трансляций")
Container(feedbackDb, "Feedback Database", "Datebase", "Хранит информацию от обратной связи")

Rel(reviewer, submission, "Рецензирует поданные доклады на конференцию")
Rel(presenter, submission, "Подает заявку на доклад")
Rel(viewer, viewing, "Просматривает трансляции и записи докладов")
Rel(presenter, viewing, "Выступает на конференции")
Rel(viewer, schedule, "Узнает о времени проведении трансляции")
Rel(presenter, schedule, "Выбирает время проведения собственного доклада")
Rel(viewer, feedback, "Оставляет обратную связь о докладе")

Rel(submission, submissionDb, "Read and writes to")
Rel(viewing, viewingDb, "Read and writes to")
Rel(schedule, scheduleDb, "Read and writes to")
Rel(feedback, feedbackDb, "Read and writes to")

note as N1
  Ограниченный контекст:
  * Submission System
  * Viewing System
  * Feedback System
  * Schedule System
end note

note as N2
  Платформенный компонент:
  * Submission Database
  * Viewing Database
  * Feedback Database
  * Schedule Database
end note

note as N3
  Пользователь системы:
  * Докладчик
  * Зритель
  * Рецензент
end note

@enduml
```