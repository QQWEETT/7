# Магазин на django rest framework

<h3> Установка </h3>
<ol>
  <li>Установить python <a href=https://www.python.org/downloads/>здесть</a></li>
 <li>pip install -r requirements.txt</li>
 <li>В settings.py внести свои данные в "DATABASES" </li>
 <li>python manage.py makemigrations</li>
 <li>python manage.py migrate</li>
 <li>python manage.py createsuperuser </li>
 <li>python manage.py runserver </li>
</ol>

# Пути API
<ol>
  <li> <a href=#apiv1> api/v1/</a> </li>
  <li> <a href=#apiv1product> api/v1/product/</a> </li>
  <ol><a href=#apiv1productslug> api/v1/product/{slug}</a> </ol>
  <ol><a href=#apiv1productsearch> api/v1/product/?search={query}</a> </ol>
  <li> <a href=#apiv1category>api/v1/category/</a> </li>
  <ol><a href=#apiv1categoryslug> api/v1/category/{slug}</a> </ol>
  <ol> <a href=#apiv1categorysearch>api/v1/category/?search={query}</a> </ol>
  <li> <a href=#apiv1cart>api/v1/cart/</a> </li>
  <ol> <a href=#apiv1cartsearch>api/v1/cart/?search={query}</a> </ol>
  <li> <a href=#apiv1cartadd>api/v1/cart/add/</a> </li>
  <li> <a href=#apiv1cartdelete>api/v1/cart/delete/{pk}/</a> </li>
  <li> <a href=#apiv1cartaddone>api/v1/cart/add_one/{pk}/</a> </li>
  <li> <a href=#apiv1cartreduce>api/v1/cart/reduce_one/{pk}/</a> </li>
  <li> <a href=#apiv1login>api/v1/drf-auth/login/</a> </li>
  <li> <a href=#apiv1logout>api/v1/drf-auth/logout/</a> </li>
  <li> <a href=#apiv1authusers>api/v1/authusers</a> </li>
  <li> <a href=#apiv1token>api/v1/token/</a> </li>
  <ol> <a href=#apiv1tokenrefresh>api/v1/token/refresh</a> </ol>
  <ol> <a href=#apiv1tokenverify>api/v1/token/verify</a> </ol>
  </ol>
  
  #API
  <h2><a name=apiv1>api/v1/ </a></h2>
  <hr>
  <h3> <a name=apiv1product>api/v1/product/ </a></h3>
  Разрешенные методы : GET, POST<br>
Уровень доступа : для чтения: общедоступный, для создания: только администратор<br>
возвращает объекты всех продуктов в базе данных, которые помечены как доступные. а также имеет вложенный внутренний объект категории, связанный с ним как отношение ForeignKey.
Вы можете получить конкретный объект продукта, передав slug в конец пути.
<h3> <a name=apiv1productslug>api/v1/product/{slug} </a></h3>
 Разрешенные методы : GET, PUT, PATCH, DELETE<br>
Уровень доступа :для чтения: общедоступный, для изменения и удаления: только администратор <br>
  возвращает конкретный объект продукта по слагу
  <h3> <a name=apiv1productsearch>api/v1/product/?search={query} </a></h3>
  Разрешенные методы : GET<br>
Уровень доступа : Общедоступный<br>
поиск продуктов по заданным ключевым словам
   <h3> <a name=apiv1category>api/v1/category/ </a></h3>
  Разрешенные методы : GET, POST<br>
Уровень доступа : для чтения: общедоступный, для создания: только администратор<br>
возвращаемые объекты категорий, созданные администратором.
Вы можете получить конкретный объект категории, передав slug в конец пути.
<h3> <a name=apiv1categoryslug>api/v1/category/{slug} </a></h3>
 Разрешенные методы : GET, PUT, PATCH, DELETE<br>
Уровень доступа :для чтения: общедоступный, для изменения и удаления: только администратор <br>
  возвращает конкретный объект категории по слагу
  <h3> <a name=apiv1categorysearch>api/v1/category/?search={query} </a></h3>
 Разрешенные методы : GET<br>
Уровень доступа :Общедоступный <br>
  поиск категории по заданным ключевым словам
   <h3> <a name=apiv1cart>api/v1/cart </a></h3>
 Разрешенные методы : GET<br>
Уровень доступа :Авторизованным пользователям <br>
  Возвращает список продуктов в корзину авторизированного пользователя
   <h3> <a name=apiv1cartsearch>api/v1/cart/?search={query} </a></h3>
 Разрешенные методы : GET<br>
Уровень доступа :Авторизованным пользователям <br>
  Поиск в корзине по заданным ключевым словам
  <h3> <a name=apiv1cartadd>api/v1/cart/add </a></h3>
 Разрешенные методы : POST<br>
Уровень доступа :Авторизованным пользователям <br>
  Добавляет продукт в корзину, если его количество больше нуля
   <h3> <a name=apiv1cartdelete>api/v1/cart/delete/{pk} </a></h3>
 Разрешенные методы : DELETE<br>
Уровень доступа :Авторизованным пользователям <br>
  Удаляет продукт из корзины 
   <h3> <a name=apiv1cartaddone>api/v1/cart/add_one/{pk}/ </a></h3>
 Разрешенные методы : GET<br>
Уровень доступа :Авторизованным пользователям <br>
  Добавляет 1 к количеству продукта, который уже находится в корзине пользователя
  <h3> <a name=apiv1cartreduce>api/v1/cart/reduce_one/{pk}/ </a></h3>
 Разрешенные методы : GET<br>
Уровень доступа :Авторизованным пользователям <br>
  Уменьшает на 1 количества продукта, который уже находится в корзине пользователя
    <h3> <a name=apiv1login>api/v1/cart/drf-auth/login/ </a></h3>
Уровень доступа : Общедоступный <br>
  Позволяет залогиниться на сайт
  <h3> <a name=apiv1logout>api/v1/cart/drf-auth/logout/ </a></h3>
Уровень доступа : Общедоступный <br>
  Позволяет разлогиниться на сайте
   <h3> <a name=apiv1authusers>api/v1/authusers/ </a></h3>
 Разрешенные методы : GET, POST<br>
Уровень доступа : для чтение: только администратору, для создания: общедоступный<br>
  Для администратора позволяет посмотреть список всех пользователей. <br>
  Позволяет регистрироваться на сайте
     <h3> <a name=apiv1token>api/v1/token/ </a></h3>
 Разрешенные методы :  POST<br>
Уровень доступа : общедоступный<br>
  Принимает набор учетных данных пользователя и возвращает
пару веб-токенов доступа и обновления JSON для подтверждения подлинности этих учетных данных.
    <h3> <a name=apiv1tokenrefresh>api/v1/token/refresh </a></h3>
 Разрешенные методы :  POST<br>
Уровень доступа : общедоступный<br>
  Принимает веб-маркер JSON типа обновления и возвращает веб-
маркер JSON типа доступа, если маркер обновления действителен.
    <h3> <a name=apiv1tokenverify>api/v1/token/verify </a></h3>
 Разрешенные методы :  POST<br>
Уровень доступа : общедоступный<br>
  Принимает токен и указывает, действителен ли он. Это представление не предоставляет
информации о пригодности токена для конкретного использования.
  
  
  
 # Осталось сделать
 Создать кабинет пользователя<br>
 Добавить систему оплаты<br>
 Добавить интерфейс
