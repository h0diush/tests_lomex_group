# Тестовое задание от Lomex Group 

#### Работа с исходной БД и реализация простого ETL процесса.
#### Реализовано на Django, для получения следующих пачек данных на основе заполненных моделей в формате JSON. Используется django rest framework

```GET api/genres/``` - <i>Название жанра; кол-во фильмов этого жанра; средняя оценка фильмов данного жанра.</i>

```GET api/actors/``` - <i>Имя актера; кол-во фильмов в которых снимался этот актер; название жанра с лучшим средним рейтингом фильмов, в которых снимался актер.</i>

```GET api/directors/``` - <i>Имя режиссера; имена актеров, которые чаще всего снимались с этим режиссером в порядке убывания количества фильмов и само количество фильмов. До первых трёх записей.
Напр. [ 
  {“name”: “Actor Actorson”, “movie_count”: 5},
  {“name”: “John Smith”, “movie_count”: 3},
  {“name”: “Anna Smith”, “movie_count”: 1}
]; до первых трёх названий фильмов режиссера по рейтингу.
</i>