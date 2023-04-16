# Контекст решения
<!-- Окружение системы (роли, участники, внешние системы) и связи системы с ним. Диаграмма контекста C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783261
-->
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(organizer, "Conference Organizer", "An organizer responsible for managing speakers, reviews, and conference scheduling.")
Person(speaker, "Speaker", "A person presenting a talk at the conference.")
Person(reviewer, "Reviewer", "A person responsible for reviewing and rating presentations.")
Person(participant, "Participant", "An attendee of the conference, either in person or remotely.")

System(confSystem, "Conference Management System", "Allows organizers, speakers, and reviewers to manage conference-related tasks such as submissions, reviews, and scheduling.")
System_Ext(emailSystem, "E-mail System", "External email system for sending notifications and updates.")
System_Ext(liveStream, "Live Streaming Platform", "Platform to broadcast presentations online during the conference.")

Rel(organizer, confSystem, "Uses")
Rel(speaker, confSystem, "Submits presentations")
Rel(reviewer, confSystem, "Reviews and rates presentations")
Rel(participant, confSystem, "Views schedule and provides feedback")

Rel(confSystem, emailSystem, "Sends notifications and updates")
Rel(confSystem, liveStream, "Coordinates live streaming")
@enduml
```
