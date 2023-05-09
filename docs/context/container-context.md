# Контекстная диаграмма контейнеров

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_TOP_DOWN()

Person(viewer, "Viewer", "Зритель")
Person(presenter, "Presenter", "Докладчик")
Person(reviewer, "Reviewer", "Рецензент")

System_Boundary(Level1, "Точка входа в систему") {
    Container(webApp, "Web App", "JavaScript + React")
    Container(mobileApp, "Mobile App", "JavaScript + React Native")
}

System_Boundary(Level2, "Распределение запросов") {
    Container(apiGateway, "API Gateway", "Java + Spring Cloud Gateway")
    Container(authService, "Authorization Service", "Java + Spring Security")
    Container(authDb, "Auth DB", "Postgres", "Хранит информацию о правах пользователей системы")
}

System_Boundary(Level3_View, "Просмотр докладов") {
    Container(viewService, "Viewing Service", "Java + Quarkus")
    Container(viewDb, "View DB", "Postgres", "Хранит метаданные трансляций и записей докладов")
}

System_Boundary(Level3_Schedule, "Расписание конференции") {
    Container(scheduleService, "Schedule Service", "Java + Spring Boot")
    Container(scheduleDb, "Schedule DB", "Postgres", "Хранит информацию о расписании")
}

System_Boundary(Level3_Feedback, "Обратная связь о докладах") {
    Container(feedbackService, "Feedback Service", "Scala + Spark")
    Container(feedbackDb, "Feedback DB", "Postgres", "Хранит информацию об обратной связи")
}

System_Boundary(Level3_Submission, "Подача заявок на доклад") {
    Container(submissionService, "Submission Service", "Java + Spring Boot")
    Container(submissionDb, "Submission DB", "Postgres", "Хранит информацию о заявках на доклад")
}

Rel(viewer, Level1, "Получает интерфейс просмотра трансляций/записей")
Rel(presenter, Level1, "Получает интерфейс для подачи заявки и выступления")
Rel(reviewer, Level1, "Получает интерфейс для рецензирования заявки на выступление")

Rel(Level1, Level2, "")

Rel(apiGateway, authService, "Проверка возможности совершения действия")

Rel(Level2, Level3_View, "")
Rel(Level2, Level3_Schedule, "")
Rel(Level2, Level3_Feedback, "")
Rel(Level2, Level3_Submission, "")

Rel(viewService, viewDb, "Сохраняет и читает данные")
Rel(scheduleService, scheduleDb, "Сохраняет и читает данные")
Rel(feedbackService, feedbackDb, "Сохраняет и читает данные")
Rel(submissionService, submissionDb, "Сохраняет и читает данные")
Rel(authService, authDb, "сохраняет и читает данные")

@enduml
```