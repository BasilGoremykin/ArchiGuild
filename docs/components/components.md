# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783368
-->
## Контейнерная диаграмма

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(attendee, "Участник", "Участник конференции")
Person(speaker, "Докладчик", "Докладчик на конференции")

System_Boundary(c, "Платформа конференций") {
  Container(web_app, "Веб-приложение", "JavaScript, React", "Веб-интерфейс для платформы конференций")
  Container(mobile_app, "Мобильное приложение", "React Native", "Мобильный интерфейс для платформы конференций")
  Container(api_gateway, "API Gateway", "Java, Spring Cloud Gateway", "Входная точка для всех входящих запросов")
  
  Container(auth_service, "Сервис аутентификации", "Java, Spring-Security", "Обрабатывает аутентификацию и авторизацию пользователей")

  Container(speaker_service, "Сервис докладчиков", "Java, Spring Boot", "Управляет профилями спикеров и презентациями")
  ContainerDb(speaker_db, "База данных спикеров", "PostgreSQL", "Хранит профили спикеров и информацию о презентациях")

  Container(schedule_service, "Сервис расписания", "Java, Spring Boot", "Управляет расписанием конференции")
  ContainerDb(schedule_db, "База данных расписания", "PostgreSQL", "Хранит данные расписания конференции")

  Container(review_service, "Сервис отзывов", "Scala, Play", "Собирает и управляет отзывами о презентациях")
  ContainerDb(review_db, "База данных отзывов", "PostgreSQL", "Хранит отзывы о презентациях")
  
  Container(video_service, "Сервис видео", "Java, Quarkus", "Обрабатывает хранение видео и активные трансляции")
  ContainerDb(video_db, "База данных видео", "PostgreSQL", "Хранит видеозаписи докладов")
}

Rel(attendee, web_app, "Получает доступ к платформе конференций через")
Rel(attendee, mobile_app, "Получает доступ к платформе конференций через")
Rel(speaker, web_app, "Получает доступ к платформе конференций через")
Rel(speaker, mobile_app, "Получает доступ к платформе конференций через")

Rel(web_app, api_gateway, "HTTP", "REST")
Rel(mobile_app, api_gateway, "HTTP", "REST")

Rel(api_gateway, auth_service, "gRPC")
Rel(auth_service, speaker_service, "gRPC")
Rel(auth_service, schedule_service, "gRPC")
Rel(auth_service, review_service, "gRPC")
Rel(auth_service, video_service, "gRPC")

Rel(speaker_service, speaker_db, "JDBC, Spring-Data")
Rel(schedule_service, schedule_db, "JDBC, Spring-Data")
Rel(review_service, review_db, "JDBC, SQL")
Rel(video_service, video_db, "JDBC, SQL")

@enduml
```

## Список компонентов
| Компонент               | Роль/назначение                                         |
|:------------------------|:--------------------------------------------------------|
| Веб-приложение          | Веб-интерфейс для платформы конференций                 |
| Мобильное приложение    | Мобильный интерфейс для платформы конференций           |
| API Gateway             | Входная точка для всех входящих запросов                |
| Сервис аутентификации   | Обрабатывает аутентификацию и авторизацию пользователей |
| Сервис докладчиков      | Управляет профилями спикеров и презентациями            | 
| База данных докладчиков | Хранит профили спикеров и информацию о презентациях     |
| Сервис расписания       | Управляет расписанием конференции                       |
| База данных расписания  | Хранит данные расписания конференции                    |
| Сервис отзывов          | Собирает и управляет отзывами о презентациях            |
| База данных отзывов     | Хранит отзывы о презентациях                            |
| Сервис видео            | Обрабатывает хранение видео и активные трансляции       |
| База данных видео       | Хранит видеозаписи докладов                             |