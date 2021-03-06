# ЗАДАЧИ:

Общие требования:
 * Разрабатываемая ИС должна реализовывать функционал авторизации и регистрации пользователей.
 * Разрабатываемая ИС должна включать в себя краткую документацию (`README.md`), которая должна содержать скриншоты с примерами работы.

1. Разработать ИС "мини хабр".
 * Коллективный блог.
 * Новые пользователи становятся активными только после одобрения статьи.

2. Разработать ИС обмена сообщениями между пользователями.
 * У всех зарегистрированных пользователей должен быть список контактов.
 * Добавление пользователя в список контактов должно сопровождаться запросом о согласии.

3. Разработать ИС "музыкальный каталог".
 * Прослушивание музыки непосредственно с сайта.
 * Прослушивание музыки доступно только зарегистрированным пользователям.
 * Пользователь должен иметь возможность просмотреть последние прослушанные произведения.

4. Разработать ИС "платный каталог фильмов".
 * Просмотр фильмов с сайта.
 * Просмотр доступен только зарегистрированным пользователям.
 * Пользователь может просматривать фильм, если он его купил.
 * Пользователь может видеть каталог своих покупок.

5. Разработать ИС "форум".
 * Содержимое должно быть доступно не авторизованным пользователям.
 * Добавлять сообщения могут только зарегистрированные пользователи.
 * Редактировать сообщение может только его автор.

6. Разработать ИС "продажа контента".
 * Зарегистрированный пользователь может поместить в него любой файл с выставлением цены за доступ к нему.
 * Каталог предложений должен быть доступен только зарегистрированным пользователям.

7. Разработать ИС создание электронных таблиц.
 * Возможность выгружать созданные пользователем таблицы из БД.
 * Загружать пользовательские таблицы CVS в БД.
 * Просматривать созданные таблицы.
 * Должна быть возможность "расшарить таблицу" для не авторизованных пользователей.

8. Разработать ИС платного хранения и редактирования документов.
 * Создание и редактирование текстовых документов на сайте.
 * Плата взимается в зависимости от количества созданных документов.

9. Разработать ИС "опросники".
 * Только зарегистрированный пользователь может создавать опросы.
 * Возможность просматривать результаты опросов.
 * Возможность "расшаривать результаты опросов" для не авторизованных пользователей.
 
10. Разработать ИС "лав планет".
 * Каждый зарегистрированный пользователь может разместить на сайте свою анкету.
 * Другие зарегистрированные пользователи могут ее оценивать и писать свои комментарии.
 * Возможность загружать свою аватарку.

11. Разработать ИС "книжный интернет магазин".
 * Зарегистрированные пользователи - покупатели.
 * Список совершенных покупок.
 * Выбор способа доставки.

### ПРИМЕЧАНИЕ ###

 * Покупка может предполагать интеграцию с какой-либо платежной системой.
 * Пополнение денежных средств может быть реализовано как переход на адрес `/get-my-money`.
 * Задачи должны быть выполнены с использованием Django framework. 
