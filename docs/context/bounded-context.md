# Диаграмма ограниченных контекстов

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()

Person(viewer, "Зритель", "Зритель на конференции")
Person(presenter, "Докладчик", "Докладчик на конференции")
Person(reviewer, "Рецензент", "Рецензирует доклады на конференции")

System(presentation, "Presentation Service", "Фронтенд приложения конференции")
System(submission, "Submission Service", "Система подачи докладов на конференции")
System(viewing, "Viewing Service", "Система просмотра трансляций и записей докладов")
System(schedule, "Schedule Service", "Система расписаний трансляций докладов")
System(feedback, "Feedback Service", "Система получения обратной связи")

Rel(reviewer, presentation, "Оценка докладов")
Rel(presenter, presentation, "Подает заявку, устанавливает расписание, выступает")
Rel(viewer, presentation, "Узнает расписание, смотрит доклады, оставляет обратную связь")

Rel(presentation, submission, "")
Rel(presentation, viewing, "")
Rel(presentation, schedule, "")
Rel(presentation, feedback, "")

note as N1
  Ограниченный контекст:
  * Presentation System
  * Submission System
  * Viewing System
  * Feedback System
  * Schedule System
end note

note as N3
  Пользователь системы:
  * Докладчик
  * Зритель
  * Рецензент
end note

@enduml
```