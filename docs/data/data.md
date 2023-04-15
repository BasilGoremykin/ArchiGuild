# Модель предметной области
<!-- Логическая модель, содержащая бизнес-сущности предметной области, атрибуты и связи между ними. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375782602

Используется диаграмма классов UML. Документация: https://plantuml.com/class-diagram 
-->

```plantuml
@startuml
' Логическая модель данных в варианте UML Class Diagram (альтернатива ER-диаграмме).
namespace ConferenceSystem {

 class Speaker
 {
  id : string
  name : string
  contactInfo : string
  bio : string
  presentations : Presentation[]
 }

 class Presentation
 {
  id : string
  title : string
  abstract : string
  presentationFile : string
  status : PresentationStatus
  speaker : Speaker
  reviews : Review[]
  session : Session
 }

 enum PresentationStatus
 {
  NEW
  UNDER_REVIEW
  APPROVED
  REJECTED
 }

 class Reviewer
 {
  id : string
  name : string
  contactInfo : string
  expertiseArea : string
 }

 class Review
 {
  id : string
  rating : int
  comments : string
  recommendations : string
  presentation : Presentation
  reviewer : Reviewer
 }

 class Session
 {
  id : string
  date : datetime
  startTime : datetime
  duration : int
  presentations : Presentation[]
  track : Track
 }

 class Track
 {
  id : string
  name : string
  description : string
  sessions : Session[]
 }

 class Schedule
 {
  id : string
  date : datetime
  tracks : Track[]
  sessions : Session[]
 }

 class Broadcast
 {
  id : string
  broadcastUrl : string
  status : BroadcastStatus
  presentation : Presentation
 }

 enum BroadcastStatus
 {
  WAITING
  ACTIVE
  FINISHED
 }

 class Feedback
 {
  id : string
  rating : int
  comments : string
  presentation : Presentation
  participant : Participant
 }

 class Participant
 {
  id : string
  name : string
  contactInfo : string
  registrationData : string
 }

 Speaker *-- "0..*" Presentation
 Presentation *-- "0..*" Review
 Reviewer *-- "0..*" Review
 Session *-- "0..*" Presentation
 Track *-- "0..*" Session
 Schedule *-- "0..*" Track
 Schedule *-- "0..*" Session
 Broadcast *-- "1" Presentation
 Feedback *-- "1" Presentation
 Feedback *-- "1" Participant
}
@enduml
```
