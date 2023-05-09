# Диаграмма ограниченных контекстов

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()

Person(viewer, "Зритель", "Зритель на конференции")
Person(presenter, "Докладчик", "Докладчик на конференции")
Person(reviewer, "Рецензент", "Рецензирует доклады на конференции")

System(submission, "Submission Service", "Система подачи докладов на конференции")
System(viewing, "Viewing Service", "Система просмотра трансляций и записей докладов")
System(schedule, "Schedule Service", "Система расписаний трансляций докладов")
System(feedback, "Feedback Service", "Система получения обратной связи")

Rel(reviewer, submission, "Рецензирует поданные доклады на конференцию")
Rel(presenter, submission, "Подает заявку на доклад")
Rel(viewer, viewing, "Просматривает трансляции и записи докладов")
Rel(presenter, viewing, "Выступает на конференции")
Rel(viewer, schedule, "Узнает о времени проведении трансляции")
Rel(presenter, schedule, "Выбирает время проведения собственного доклада")
Rel(viewer, feedback, "Оставляет обратную связь о докладе")

note as N1
  Ограниченный контекст:
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