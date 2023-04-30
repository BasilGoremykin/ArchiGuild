# Контекстная диаграмма контейнеров

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()

Person(viewer, "Viewer", "Зритель")
Person(presenter, "Presenter", "Докладчик")
Person(reviewer, "Reviewer", "Рецензент")

System_Boundary(Level1, "Presentation") {
    Container(webApp, "Web App", "JavaScript + React")
    Container(mobileApp, "Mobile App", "JavaScript + React Native")
}

System_Boundary(Level2, "Auth + Gateway") {
    Container(apiGateway, "API Gateway", "Java + Spring Cloud Gateway")
    Container(authService, "Authorization Service", "Java + Spring Security")
}

System_Boundary(Level3, "Services") {
    Container(viewService, "Viewing System", "Java + Quarkus")
    Container(scheduleService, "Schedule System", "Java + Spring Boot")
    Container(feedbackService, "Feedback System", "Sacala + Spark")
    Container(submissionService, "Submission System", "Java + Spring Boot")
}

System_Boundary(Level4, "DB") {
    Container(viewDb, "View DB", "Postgres", "Хранит метадату трансляций и записи докладов")
    Container(scheduleDb, "Schedule DB", "Postgres", "Хранит информацию о расписании")
    Container(feedbackDb, "Feedback DB", "Postgres", "Хранит информацию об обратной связи")
    Container(submissionDb, "Submission DB", "Postgres", "Хранит информацию о докладах")
}

Rel(viewer, Level1, "")
Rel(presenter, Level1, "")
Rel(reviewer, Level1, "")

Rel(Level1, Level2, "")
Rel(Level2, Level3, "")
Rel(Level3, Level4, "")

@enduml
```